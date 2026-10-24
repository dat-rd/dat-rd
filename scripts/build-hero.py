import math, os, random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

W, H, S = 1600, 560, 12
BASE, X0, TARGET = 340, 96, 1330
A, TAU = 7, 26
TEXT = "Nguyễn Thành Đạt"
FONT_PATH = "/tmp/Inter.ttf"

clamp = lambda v, a, b: max(a, min(b, v))

# Font setup
f = ImageFont.truetype(FONT_PATH, 150)
vals = [800 if "eight" in (a["name"] if isinstance(a["name"], str) else a["name"].decode()) else 32 for a in f.get_variation_axes()]
f.set_variation_by_axes(vals)
font_size = int(150 * TARGET / f.getlength(TEXT))
f = ImageFont.truetype(FONT_PATH, font_size)
f.set_variation_by_axes(vals)

# Mask
img = Image.new("L", (W, H), 0)
ImageDraw.Draw(img).text((X0, BASE), TEXT, font=f, fill=255, anchor="ls")
m = np.array(img) > 127
d_out = ndi.distance_transform_edt(~m)
gy, gx = np.gradient(d_out)

# Find dot below of 'ạ'
cx, cy = 1322, 362
ar = 14

# Vector contours of letters (excluding accent dot)
m_uint8 = m.astype(np.uint8)
contours, _ = cv2.findContours(m_uint8, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
path_segments = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.45, True)
    if len(approx) < 3: continue
    pts = approx.reshape(-1, 2)
    if np.linalg.norm(pts.mean(axis=0) - np.array([cx, cy])) < 25:
        continue
    seg = f"M{pts[0][0]} {pts[0][1]}" + "".join(f" L{p[0]} {p[1]}" for p in pts[1:]) + " Z"
    path_segments.append(seg)
text_vector_path = " ".join(path_segments)

# Dot field
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
        t = clamp((x0 - 600) / 1000, 0, 1)
        rim_preserve = clamp(d / 28, 0, 1)
        jit = t * t * S * 0.7 * (0.15 + 0.85 * rim_preserve)
        x += rng.uniform(-1, 1) * jit
        y += rng.uniform(-1, 1) * jit
        if not (0 <= x < W and 0 <= y < H): continue
        vig = 1 - clamp(abs(y0 - H / 2) / (H / 2), 0, 1) ** 3
        pts.append((x, y, 1 + 2.2 * math.exp(-d / 12), vig))

THEMES = {
    "dark": {
        "dot": "#8B949E",
        "acc": "#F39C42",
        "acc_glow": "#FFB74D",
        "hud": "#30363D",
        "hud_text": "#484F58",
        "shimmer_base": "#8B949E",
        "shimmer_peak": "#8B949E",
        "shimmer_text": "#C9D1D9",
        "k": 0.50,
        "bg_test": "#0D1117"
    },
    "light": {
        "dot": "#57606A",
        "acc": "#4F46E5",
        "acc_glow": "#6366F1",
        "hud": "#D0D7DE",
        "hud_text": "#8C959F",
        "shimmer_base": "#E1E4E8",
        "shimmer_peak": "#24292F",
        "shimmer_text": "#24292F",
        "k": 0.55,
        "bg_test": "#FFFFFF"
    }
}

for name, c in THEMES.items():
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
    
    # Advanced Architectural + Specular Shimmer SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Nguyễn Thành Đạt — Autonomous System Field</title>
<defs>
  <!-- Moving Shimmer Gradient across Name -->
  <linearGradient id="shimmer_{name}" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{c["shimmer_base"]}" stop-opacity="0.16"/>
    <stop offset="35%" stop-color="{c["shimmer_base"]}" stop-opacity="0.22"/>
    <stop offset="50%" stop-color="{c["shimmer_text"]}" stop-opacity="0.75"/>
    <stop offset="65%" stop-color="{c["shimmer_base"]}" stop-opacity="0.22"/>
    <stop offset="100%" stop-color="{c["shimmer_base"]}" stop-opacity="0.16"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="-1600 0" to="1600 0" dur="5s" repeatCount="indefinite" ease="ease-in-out"/>
  </linearGradient>

  <!-- Flowing Signal Dash -->
  <linearGradient id="beam_{name}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{c["acc"]}" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="{c["acc"]}" stop-opacity="0"/>
  </linearGradient>
</defs>

<style>
  /* Pulse Beacon */
  .beacon {{ transform-box: fill-box; transform-origin: center; animation: pulse 4s ease-in-out infinite; }}
  @keyframes pulse {{
    0%, 100% {{ transform: scale(0.9); opacity: 0.8; }}
    50% {{ transform: scale(1.18); opacity: 1; }}
  }}

  /* Radar Ripple Waves expanding from the accent mark */
  .wave {{
    transform-box: fill-box;
    transform-origin: center;
    animation: ripple 6s cubic-bezier(0.1, 0.4, 0.3, 1) infinite;
  }}
  .w2 {{ animation-delay: 2s; }}
  .w3 {{ animation-delay: 4s; }}
  @keyframes ripple {{
    0% {{ r: {ar}px; opacity: 0.75; stroke-width: 2.2px; }}
    60% {{ opacity: 0.25; stroke-width: 1.2px; }}
    100% {{ r: 160px; opacity: 0; stroke-width: 0.5px; }}
  }}

  /* Datum flow */
  .flow-line {{
    stroke-dasharray: 4 8;
    animation: flow 1.8s linear infinite;
  }}
  @keyframes flow {{
    from {{ stroke-dashoffset: 0; }}
    to {{ stroke-dashoffset: -24; }}
  }}

  .mono {{
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    font-size: 10px;
    letter-spacing: 1.8px;
    fill: {c["hud_text"]};
  }}

  @media (prefers-reduced-motion: reduce) {{
    .beacon, .wave, .flow-line {{ animation: none; }}
  }}
</style>

<!-- 1. Architectural Calibration Marks & Grid Borders -->
<g stroke="{c["hud"]}" stroke-width="1" fill="none" opacity="0.65">
  <!-- Corner Crosshairs -->
  <path d="M40 32 V48 M32 40 H48" />
  <path d="M1560 32 V48 M1552 40 H1568" />
  <path d="M40 512 V528 M32 520 H48" />
  <path d="M1560 512 V528 M1552 520 H1568" />
  
  <!-- Subtle Datum axis extending from the beacon to right edge -->
  <line x1="{cx + ar + 6}" y1="{cy}" x2="1540" y2="{cy}" stroke="{c["hud"]}" stroke-width="0.8" />
</g>

<!-- Animated Flow Vector on Datum Axis -->
<line x1="{cx + ar + 6}" y1="{cy}" x2="1520" y2="{cy}" stroke="url(#beam_{name})" stroke-width="1.4" class="flow-line"/>

<!-- Subtle HUD Metadata -->
<g class="mono">
  <text x="60" y="44">SYS.FORMATION // 04.STRATA</text>
  <text x="1420" y="44" text-anchor="start">LAT: 10.4 / LNG: 14.2</text>
  <text x="1440" y="{cy - 8}">SIGNAL &gt;&gt;</text>
  <text x="60" y="524">ORIGIN: DETERMINISTIC</text>
  <text x="1390" y="524" text-anchor="start">HORIZON: PROBABILISTIC</text>
</g>

<!-- 2. Name Silhouette with Dynamic Specular Shimmer -->
<path d="{text_vector_path}" fill="url(#shimmer_{name})" fill-rule="evenodd"/>

<!-- 3. The Particle Displacement Field -->
<g fill="none" stroke="{c["dot"]}" stroke-width="3.6" stroke-linecap="round">
  {paths_svg}
</g>

<!-- 4. The Beacon: Expanding Radar Shockwaves -->
<circle class="wave w1" cx="{cx}" cy="{cy}" r="{ar}" fill="none" stroke="{c["acc"]}" />
<circle class="wave w2" cx="{cx}" cy="{cy}" r="{ar}" fill="none" stroke="{c["acc"]}" />
<circle class="wave w3" cx="{cx}" cy="{cy}" r="{ar}" fill="none" stroke="{c["acc"]}" />

<!-- 5. Beacon Core -->
<circle class="beacon" cx="{cx}" cy="{cy}" r="{ar * 2.8:.1f}" fill="{c["acc"]}" fill-opacity="0.22" />
<circle cx="{cx}" cy="{cy}" r="{ar * 1.5:.1f}" fill="{c["acc"]}" fill-opacity="0.45" />
<circle cx="{cx}" cy="{cy}" r="{ar}" fill="{c["acc"]}" />

</svg>'''
    
    with open(f"hero-levelup-{name}.svg", "w") as out_f:
        out_f.write(svg)
    print(f"Generated {name} levelup -> {len(svg)} bytes")

