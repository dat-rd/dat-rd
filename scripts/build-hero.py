import math, os, random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

W, H, S = 1600, 560, 12            # canvas, grid spacing
BASE, X0, TARGET = 340, 96, 1330   # baseline y, left margin, name width
A, TAU = 7, 26                     # push-out amplitude / falloff
TEXT = "Nguyễn Thành Đạt"
FONT_PATH = "/tmp/Inter.ttf"

THEMES = {
    "dark": {
        "dot": "#8B949E",
        "acc": "#8B93FF",
        "fill": "#8B949E",
        "fill_opacity": 0.08,
        "k": 0.50,
        "name": "hero-dark.svg"
    },
    "light": {
        "dot": "#57606A",
        "acc": "#4F46E5",
        "fill": "#57606A",
        "fill_opacity": 0.09,
        "k": 0.55,
        "name": "hero-light.svg"
    }
}
clamp = lambda v, a, b: max(a, min(b, v))

# 1. Load font with wght=800
f = ImageFont.truetype(FONT_PATH, 150)
vals = [800 if "eight" in (a["name"] if isinstance(a["name"], str) else a["name"].decode()) else 32 for a in f.get_variation_axes()]
f.set_variation_by_axes(vals)
font_size = int(150 * TARGET / f.getlength(TEXT))
f = ImageFont.truetype(FONT_PATH, font_size)
f.set_variation_by_axes(vals)

# 2. Raster mask
img = Image.new("L", (W, H), 0)
ImageDraw.Draw(img).text((X0, BASE), TEXT, font=f, fill=255, anchor="ls")
m = np.array(img) > 127
d_out = ndi.distance_transform_edt(~m)
gy, gx = np.gradient(d_out)

# 3. Connected components - find accent dot (component below baseline under 'ạ')
lab, n = ndi.label(m, structure=np.ones((3, 3)))
cands = []
for k in range(1, n + 1):
    ys, xs = np.where(lab == k)
    if ys.min() > BASE - 5:
        cands.append((abs(xs.mean() - 1322), xs.mean(), ys.mean(), len(xs)))
_, cx, cy, area = min(cands)
ar = max(math.sqrt(area / math.pi) * 1.15, 5)

# 4. Extract vector contours for subtle fill (excluding the accent dot)
m_uint8 = m.astype(np.uint8)
contours, _ = cv2.findContours(m_uint8, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
path_segments = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.45, True)
    if len(approx) < 3: continue
    pts = approx.reshape(-1, 2)
    # Check if this contour is the accent dot below
    if np.linalg.norm(pts.mean(axis=0) - np.array([cx, cy])) < 25:
        continue
    seg = f"M{pts[0][0]} {pts[0][1]}" + "".join(f" L{p[0]} {p[1]}" for p in pts[1:]) + " Z"
    path_segments.append(seg)
text_vector_path = " ".join(path_segments)

# 5. Generate dot field with rim-preserving scatter
rng = random.Random(7)
pts = []
for j in range(H // S + 1):
    for i in range(W // S + 1):
        x0, y0 = i * S + S / 2, j * S + S / 2
        if x0 >= W or y0 >= H or m[int(y0), int(x0)]: continue
        d = d_out[int(y0), int(x0)]
        gxv, gyv = gx[int(y0), int(x0)], gy[int(y0), int(x0)]
        nn = math.hypot(gxv, gyv) or 1
        u = A * math.exp(-d / TAU)
        x, y = x0 + gxv / nn * u, y0 + gyv / nn * u
        
        # Order -> looseness from left to right, but crisp near letters
        t = clamp((x0 - 600) / 1000, 0, 1)
        rim_preserve = clamp(d / 28, 0, 1) # dots within 28px of letter outline stay firmly anchored to the rim!
        jit = t * t * S * 0.7 * (0.15 + 0.85 * rim_preserve)
        x += rng.uniform(-1, 1) * jit
        y += rng.uniform(-1, 1) * jit
        
        if not (0 <= x < W and 0 <= y < H): continue
        vig = 1 - clamp(abs(y0 - H / 2) / (H / 2), 0, 1) ** 3
        pts.append((x, y, 1 + 2.2 * math.exp(-d / 12), vig))

# 6. Build production SVGs
for theme, c in THEMES.items():
    b = {}
    for x, y, rim, vig in pts:
        q = round(clamp(c["k"] * rim * vig, 0, .95) * 20) / 20
        if q >= .05:
            b.setdefault(q, []).append((round(y), round(x)))
    
    def enc(v):
        v.sort()
        px = py = 0
        o = []
        for y, x in v:
            o.append(f"m{x-px} {y-py}h0")
            px, py = x, y
        return "".join(o)
    
    paths_svg = "".join(f'<path stroke-opacity="{q}" d="M0 0{enc(v)}"/>' for q, v in sorted(b.items()))
    
    # SVG has transparent background (no <rect>) for seamless integration into GitHub!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Nguyễn Thành Đạt</title>
<style>
.b{{transform-box:fill-box;transform-origin:center;animation:b 5s ease-in-out infinite}}
@keyframes b{{0%,100%{{transform:scale(.8);opacity:.5}}50%{{transform:scale(1.15);opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.b{{animation:none}}}}
</style>
<path d="{text_vector_path}" fill="{c["fill"]}" fill-opacity="{c["fill_opacity"]}" fill-rule="evenodd"/>
<g fill="none" stroke="{c["dot"]}" stroke-width="3.6" stroke-linecap="round">{paths_svg}</g>
<circle class="b" cx="{cx:.0f}" cy="{cy:.0f}" r="{ar*3.2:.0f}" fill="{c["acc"]}" fill-opacity=".18"/>
<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{ar:.0f}" fill="{c["acc"]}"/>
</svg>'''
    
    target_path = f"/mnt/Data/CV Profile & Portfolio/github-profile/assets/{c['name']}"
    with open(target_path, "w", encoding="utf-8") as out_f:
        out_f.write(svg)
    print(f"Generated {c['name']} -> {len(svg)} bytes at {target_path}")

print("Success! Dots:", len(pts), "Accent at:", round(cx), round(cy))
