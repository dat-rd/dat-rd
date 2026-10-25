import os
import io
import base64
from PIL import Image, ImageFilter, ImageDraw

# Hark Pro / Apple Neo-Minimalism Design System Generator
# Builds:
# 1. hero-dark.svg & hero-light.svg (Atmospheric Cloudscape Hero)
# 2. footer-dark.svg & footer-light.svg (Live Status HUD Bar)
# 3. btn-twitter-dark.svg, btn-twitter-light.svg, btn-email-dark.svg, btn-email-light.svg

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO BANNER ASSETS (1200 x 420)
# -------------------------------------------------------------
HW, HH = 1200, 420

def generate_hark_dark_cloud():
    img = Image.new("RGBA", (HW, HH), (15, 20, 32, 255))
    draw = ImageDraw.Draw(img)
    for y in range(HH):
        t = y / HH
        r = int(52 * (1 - t) + 16 * t)
        g = int(68 * (1 - t) + 22 * t)
        b = int(108 * (1 - t) + 36 * t)
        draw.line([(0, y), (HW, y)], fill=(r, g, b, 255))
    
    cloud_img = Image.new("RGBA", (HW, HH), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cloud_img)
    cdraw.ellipse([HW*0.28, HH*0.42, HW*0.82, HH*1.28], fill=(98, 105, 136, 210))
    cdraw.ellipse([HW*0.02, HH*0.46, HW*0.54, HH*1.22], fill=(88, 95, 126, 195))
    cdraw.ellipse([HW*0.62, HH*0.18, HW*1.18, HH*0.92], fill=(68, 86, 138, 180))
    cdraw.ellipse([-HW*0.15, HH*0.15, HW*0.42, HH*0.85], fill=(62, 78, 126, 185))
    cdraw.ellipse([HW*0.25, -HH*0.28, HW*0.75, HH*0.48], fill=(92, 118, 175, 135))
    cdraw.ellipse([HW*0.12, HH*0.62, HW*0.88, HH*1.38], fill=(112, 116, 145, 215))
    
    cloud_blurred = cloud_img.filter(ImageFilter.GaussianBlur(radius=64))
    final_img = Image.alpha_composite(img, cloud_blurred)
    buf = io.BytesIO()
    final_img.save(buf, format="WEBP", quality=88)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def generate_hark_light_cloud():
    img = Image.new("RGBA", (HW, HH), (235, 242, 250, 255))
    draw = ImageDraw.Draw(img)
    for y in range(HH):
        t = y / HH
        r = int(88 * (1 - t) + 236 * t)
        g = int(128 * (1 - t) + 243 * t)
        b = int(182 * (1 - t) + 252 * t)
        draw.line([(0, y), (HW, y)], fill=(r, g, b, 255))
        
    cloud_img = Image.new("RGBA", (HW, HH), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cloud_img)
    cdraw.ellipse([HW*0.20, HH*0.28, HW*0.68, HH*0.96], fill=(255, 255, 255, 230))
    cdraw.ellipse([HW*0.06, HH*0.42, HW*0.94, HH*1.28], fill=(255, 255, 255, 250))
    cdraw.ellipse([HW*0.56, -HH*0.15, HW*1.10, HH*0.65], fill=(110, 150, 202, 150))
    cdraw.ellipse([-HW*0.10, HH*0.18, HW*0.45, HH*0.88], fill=(245, 250, 255, 210))
    cdraw.ellipse([HW*0.28, HH*0.02, HW*0.80, HH*0.62], fill=(255, 255, 255, 185))
    
    cloud_blurred = cloud_img.filter(ImageFilter.GaussianBlur(radius=60))
    final_img = Image.alpha_composite(img, cloud_blurred)
    buf = io.BytesIO()
    final_img.save(buf, format="WEBP", quality=88)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def build_heroes():
    dark_b64 = generate_hark_dark_cloud()
    light_b64 = generate_hark_light_cloud()
    
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {HW} {HH}" width="{HW}" height="{HH}" role="img" aria-labelledby="t d">
<title id="t">Nguyen Thanh Dat</title>
<desc id="d">Building software with AI, agents and modern engineering workflows.</desc>
<defs>
  <clipPath id="cardClip">
    <rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" rx="24"/>
  </clipPath>
  <linearGradient id="rimStroke" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#ABC0E4" stop-opacity="0.55"/>
    <stop offset="25%" stop-color="#6B82A8" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#243144" stop-opacity="0.15"/>
  </linearGradient>
  <linearGradient id="pillBg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#202A3D" stop-opacity="0.88"/>
    <stop offset="100%" stop-color="#121824" stop-opacity="0.88"/>
  </linearGradient>
  <linearGradient id="pillStroke" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#8EA8D4" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#344663" stop-opacity="0.3"/>
  </linearGradient>
  <radialGradient id="pillAura" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#7397D4" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#7397D4" stop-opacity="0"/>
  </radialGradient>
</defs>
<style>
  .f {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Segoe UI", Helvetica, Arial, sans-serif; }}
  .mono {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }}
  .pulse-dot {{ animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
  @keyframes livePulse {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.45; transform: scale(0.85); }} }}
  .halo {{ animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: center; }}
  @keyframes ring {{ 0% {{ r: 4px; opacity: 0.8; stroke-width: 1.5px; }} 100% {{ r: 14px; opacity: 0; stroke-width: 0.5px; }} }}
  @media (prefers-reduced-motion: reduce) {{ .pulse-dot, .halo {{ animation: none; }} }}
</style>
<g clip-path="url(#cardClip)">
  <image href="data:image/webp;base64,{dark_b64}" x="12" y="12" width="{HW - 24}" height="{HH - 24}" preserveAspectRatio="none"/>
  <rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" fill="#080C14" fill-opacity="0.18"/>
  <ellipse cx="{HW/2}" cy="74" rx="230" ry="44" fill="url(#pillAura)"/>
</g>
<rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" rx="24" fill="none" stroke="url(#rimStroke)" stroke-width="1.2"/>
<g class="f" transform="translate({HW/2}, 74)">
  <rect x="-174" y="-19" width="348" height="38" rx="19" fill="url(#pillBg)" stroke="url(#pillStroke)" stroke-width="1"/>
  <g transform="translate(-144, 0)">
    <circle class="halo" cx="0" cy="0" r="4" fill="none" stroke="#3FB950"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4.2" fill="#3FB950"/>
  </g>
  <text x="-124" y="4" font-size="12" font-weight="500" fill="#E2E8F0" letter-spacing="0.4px">SOFTWARE × AI × ENTERPRISE</text>
  <text x="146" y="4" text-anchor="end" font-size="11" font-weight="600" fill="#B4C6FF" letter-spacing="1px" class="mono">DAT-RD</text>
</g>
<g class="f" text-anchor="middle">
  <text x="{HW/2}" y="196" font-size="54" font-weight="700" fill="#FFFFFF" letter-spacing="-1.2px">Nguyen Thanh Dat</text>
  <text x="{HW/2}" y="254" font-size="22" font-weight="400" fill="#E2E8F0" letter-spacing="-0.3px">Building software with AI, agents &amp; modern engineering workflows.</text>
  <text x="{HW/2}" y="295" font-size="15" font-weight="400" fill="#A8B7CD" letter-spacing="0.2px">Exploring the intersection of deterministic enterprise software &amp; autonomous AI systems.</text>
</g>
<line x1="48" y1="{HH - 64}" x2="{HW - 48}" y2="{HH - 64}" stroke="#475569" stroke-opacity="0.35" stroke-width="1"/>
<g class="f mono" font-size="11" fill="#94A3B8">
  <text x="48" y="{HH - 38}">SYS.STATUS // ACTIVE</text>
  <text x="{HW/2}" y="{HH - 38}" text-anchor="middle">FPT UNIVERSITY → FPT SOFTWARE → AI SYSTEMS</text>
  <text x="{HW - 48}" y="{HH - 38}" text-anchor="end">VIETNAM // 2026</text>
</g>
</svg>'''

    light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {HW} {HH}" width="{HW}" height="{HH}" role="img" aria-labelledby="t d">
<title id="t">Nguyen Thanh Dat</title>
<desc id="d">Building software with AI, agents and modern engineering workflows.</desc>
<defs>
  <clipPath id="cardClipLight">
    <rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" rx="24"/>
  </clipPath>
  <linearGradient id="rimStrokeLight" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.9"/>
    <stop offset="40%" stop-color="#CBD5E1" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#94A3B8" stop-opacity="0.25"/>
  </linearGradient>
  <linearGradient id="pillBgLight" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.92"/>
    <stop offset="100%" stop-color="#F1F5F9" stop-opacity="0.92"/>
  </linearGradient>
  <linearGradient id="pillStrokeLight" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#CBD5E1" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#94A3B8" stop-opacity="0.4"/>
  </linearGradient>
</defs>
<style>
  .f {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Segoe UI", Helvetica, Arial, sans-serif; }}
  .mono {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }}
  .pulse-dot {{ animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
  @keyframes livePulse {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.45; transform: scale(0.85); }} }}
  .halo {{ animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: center; }}
  @keyframes ring {{ 0% {{ r: 4px; opacity: 0.8; stroke-width: 1.5px; }} 100% {{ r: 14px; opacity: 0; stroke-width: 0.5px; }} }}
  @media (prefers-reduced-motion: reduce) {{ .pulse-dot, .halo {{ animation: none; }} }}
</style>
<g clip-path="url(#cardClipLight)">
  <image href="data:image/webp;base64,{light_b64}" x="12" y="12" width="{HW - 24}" height="{HH - 24}" preserveAspectRatio="none"/>
  <rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" fill="#FFFFFF" fill-opacity="0.18"/>
</g>
<rect x="12" y="12" width="{HW - 24}" height="{HH - 24}" rx="24" fill="none" stroke="url(#rimStrokeLight)" stroke-width="1.2"/>
<g class="f" transform="translate({HW/2}, 74)">
  <rect x="-174" y="-19" width="348" height="38" rx="19" fill="url(#pillBgLight)" stroke="url(#pillStrokeLight)" stroke-width="1"/>
  <g transform="translate(-144, 0)">
    <circle class="halo" cx="0" cy="0" r="4" fill="none" stroke="#1A7F37"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4.2" fill="#1A7F37"/>
  </g>
  <text x="-124" y="4" font-size="12" font-weight="600" fill="#334155" letter-spacing="0.4px">SOFTWARE × AI × ENTERPRISE</text>
  <text x="146" y="4" text-anchor="end" font-size="11" font-weight="700" fill="#4338CA" letter-spacing="1px" class="mono">DAT-RD</text>
</g>
<g class="f" text-anchor="middle">
  <text x="{HW/2}" y="196" font-size="54" font-weight="700" fill="#0F172A" letter-spacing="-1.2px">Nguyen Thanh Dat</text>
  <text x="{HW/2}" y="254" font-size="22" font-weight="500" fill="#334155" letter-spacing="-0.3px">Building software with AI, agents &amp; modern engineering workflows.</text>
  <text x="{HW/2}" y="295" font-size="15" font-weight="400" fill="#64748B" letter-spacing="0.2px">Exploring the intersection of deterministic enterprise software &amp; autonomous AI systems.</text>
</g>
<line x1="48" y1="{HH - 64}" x2="{HW - 48}" y2="{HH - 64}" stroke="#CBD5E1" stroke-opacity="0.8" stroke-width="1"/>
<g class="f mono" font-size="11" fill="#64748B">
  <text x="48" y="{HH - 38}">SYS.STATUS // ACTIVE</text>
  <text x="{HW/2}" y="{HH - 38}" text-anchor="middle">FPT UNIVERSITY → FPT SOFTWARE → AI SYSTEMS</text>
  <text x="{HW - 48}" y="{HH - 38}" text-anchor="end">VIETNAM // 2026</text>
</g>
</svg>'''

    with open(os.path.join(ASSETS_DIR, "hero-dark.svg"), "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(os.path.join(ASSETS_DIR, "hero-light.svg"), "w", encoding="utf-8") as f:
        f.write(light_svg)

# -------------------------------------------------------------
# 2. STATUS HUD FOOTER ASSETS (1200 x 64)
# -------------------------------------------------------------
FW, FH = 1200, 64

def generate_footer_bg(theme="dark"):
    if theme == "dark":
        img = Image.new("RGBA", (FW, FH), (15, 20, 32, 255))
        draw = ImageDraw.Draw(img)
        for y in range(FH):
            t = y / FH
            r = int(42 * (1 - t) + 16 * t)
            g = int(54 * (1 - t) + 22 * t)
            b = int(88 * (1 - t) + 36 * t)
            draw.line([(0, y), (FW, y)], fill=(r, g, b, 255))
            
        cimg = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        cdraw = ImageDraw.Draw(cimg)
        cdraw.ellipse([FW*0.06, -FH*0.4, FW*0.46, FH*1.4], fill=(92, 102, 136, 145))
        cdraw.ellipse([FW*0.60, -FH*0.3, FW*0.96, FH*1.3], fill=(100, 110, 146, 135))
        cdraw.ellipse([FW*0.30, FH*0.2, FW*0.75, FH*1.5], fill=(78, 88, 122, 110))
        cblur = cimg.filter(ImageFilter.GaussianBlur(radius=24))
        final = Image.alpha_composite(img, cblur)
    else:
        img = Image.new("RGBA", (FW, FH), (238, 243, 250, 255))
        draw = ImageDraw.Draw(img)
        for y in range(FH):
            t = y / FH
            r = int(205 * (1 - t) + 242 * t)
            g = int(222 * (1 - t) + 246 * t)
            b = int(242 * (1 - t) + 252 * t)
            draw.line([(0, y), (FW, y)], fill=(r, g, b, 255))
            
        cimg = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        cdraw = ImageDraw.Draw(cimg)
        cdraw.ellipse([FW*0.10, -FH*0.4, FW*0.52, FH*1.4], fill=(255, 255, 255, 210))
        cdraw.ellipse([FW*0.58, -FH*0.2, FW*0.92, FH*1.3], fill=(155, 192, 235, 110))
        cblur = cimg.filter(ImageFilter.GaussianBlur(radius=20))
        final = Image.alpha_composite(img, cblur)
        
    buf = io.BytesIO()
    final.save(buf, format="WEBP", quality=88)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def build_footers():
    dark_bg = generate_footer_bg("dark")
    light_bg = generate_footer_bg("light")
    
    footer_dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {FW} {FH}" width="{FW}" height="{FH}" role="img" aria-label="Status HUD: Open for SE &amp; AI Roles">
<defs>
  <clipPath id="fClip">
    <rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" rx="16"/>
  </clipPath>
  <linearGradient id="fRim" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#ABC0E4" stop-opacity="0.50"/>
    <stop offset="35%" stop-color="#556985" stop-opacity="0.22"/>
    <stop offset="100%" stop-color="#1E2736" stop-opacity="0.10"/>
  </linearGradient>
</defs>
<style>
  .f {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
  .pulse-dot {{ animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
  @keyframes livePulse {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.45; transform: scale(0.85); }} }}
  .halo {{ animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: center; }}
  @keyframes ring {{ 0% {{ r: 3.5px; opacity: 0.8; stroke-width: 1.5px; }} 100% {{ r: 12px; opacity: 0; stroke-width: 0.5px; }} }}
  @media (prefers-reduced-motion: reduce) {{ .pulse-dot, .halo {{ animation: none; }} }}
</style>
<g clip-path="url(#fClip)">
  <image href="data:image/webp;base64,{dark_bg}" x="10" y="8" width="{FW - 20}" height="{FH - 16}" preserveAspectRatio="none"/>
  <rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" fill="#080C14" fill-opacity="0.18"/>
</g>
<rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" rx="16" fill="none" stroke="url(#fRim)" stroke-width="1.2"/>
<g class="f" font-size="12" font-weight="500">
  <g transform="translate(36, 32)">
    <circle class="halo" cx="0" cy="0" r="3.5" fill="none" stroke="#3FB950"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4" fill="#3FB950"/>
    <text x="16" y="4" fill="#E2E8F0" letter-spacing="0.4px">STATUS // OPEN FOR SE &amp; AI ROLES</text>
  </g>
  <g transform="translate({FW/2}, 36)" text-anchor="middle">
    <text fill="#94A3B8" letter-spacing="0.5px">BASE // VIETNAM &#160;&#160;·&#160;&#160; TIMEZONE // ICT (UTC+7)</text>
  </g>
  <g transform="translate({FW - 36}, 36)" text-anchor="end">
    <text fill="#B4C6FF" font-weight="600" letter-spacing="0.8px">DAT-RD // 2026</text>
  </g>
</g>
</svg>'''

    footer_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {FW} {FH}" width="{FW}" height="{FH}" role="img" aria-label="Status HUD: Open for SE &amp; AI Roles">
<defs>
  <clipPath id="fClipLight">
    <rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" rx="16"/>
  </clipPath>
  <linearGradient id="fRimLight" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.9"/>
    <stop offset="40%" stop-color="#CBD5E1" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#94A3B8" stop-opacity="0.25"/>
  </linearGradient>
</defs>
<style>
  .f {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
  .pulse-dot {{ animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
  @keyframes livePulse {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.45; transform: scale(0.85); }} }}
  .halo {{ animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: center; }}
  @keyframes ring {{ 0% {{ r: 3.5px; opacity: 0.8; stroke-width: 1.5px; }} 100% {{ r: 12px; opacity: 0; stroke-width: 0.5px; }} }}
  @media (prefers-reduced-motion: reduce) {{ .pulse-dot, .halo {{ animation: none; }} }}
</style>
<g clip-path="url(#fClipLight)">
  <image href="data:image/webp;base64,{light_bg}" x="10" y="8" width="{FW - 20}" height="{FH - 16}" preserveAspectRatio="none"/>
  <rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" fill="#FFFFFF" fill-opacity="0.22"/>
</g>
<rect x="10" y="8" width="{FW - 20}" height="{FH - 16}" rx="16" fill="none" stroke="url(#fRimLight)" stroke-width="1.2"/>
<g class="f" font-size="12" font-weight="500">
  <g transform="translate(36, 32)">
    <circle class="halo" cx="0" cy="0" r="3.5" fill="none" stroke="#1A7F37"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4" fill="#1A7F37"/>
    <text x="16" y="4" fill="#0F172A" font-weight="600" letter-spacing="0.4px">STATUS // OPEN FOR SE &amp; AI ROLES</text>
  </g>
  <g transform="translate({FW/2}, 36)" text-anchor="middle">
    <text fill="#475569" letter-spacing="0.5px">BASE // VIETNAM &#160;&#160;·&#160;&#160; TIMEZONE // ICT (UTC+7)</text>
  </g>
  <g transform="translate({FW - 36}, 36)" text-anchor="end">
    <text fill="#4338CA" font-weight="600" letter-spacing="0.8px">DAT-RD // 2026</text>
  </g>
</g>
</svg>'''

    with open(os.path.join(ASSETS_DIR, "footer-dark.svg"), "w", encoding="utf-8") as f:
        f.write(footer_dark_svg)
    with open(os.path.join(ASSETS_DIR, "footer-light.svg"), "w", encoding="utf-8") as f:
        f.write(footer_light_svg)

# -------------------------------------------------------------
# 3. ACTION BUTTON ASSETS (Twitter & Email)
# -------------------------------------------------------------
def make_btn_svg(text, icon_type, theme="dark", width=180, height=36):
    if theme == "dark":
        bg = "#182132"
        stroke = "#344563"
        color = "#F0F6FC"
        icon_color = "#A5B4FC"
    else:
        bg = "#FFFFFF"
        stroke = "#CBD5E1"
        color = "#0F172A"
        icon_color = "#4338CA"
        
    icon_svg = ""
    if icon_type == "twitter":
        icon_svg = f'<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" fill="{color}" transform="translate(18, 9) scale(0.8)"/>'
    elif icon_type == "email":
        icon_svg = f'<g fill="none" stroke="{icon_color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" transform="translate(16, 11)"><rect width="18" height="14" rx="3"/><path d="m2 3 7 5 7-5"/></g>'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
<style>
  .f {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", Helvetica, Arial, sans-serif; }}
</style>
<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="{height/2}" fill="{bg}" stroke="{stroke}" stroke-width="1"/>
{icon_svg}
<text class="f" x="38" y="{height/2 + 4.5}" font-size="12" font-weight="500" fill="{color}" letter-spacing="0.2px">
  {text}
</text>
<path d="M{width - 20} {height/2 - 3} L{width - 15} {height/2 + 2} M{width - 15} {height/2 - 3} L{width - 15} {height/2 + 2} L{width - 20} {height/2 + 2}" stroke="{stroke}" stroke-width="1.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

def build_buttons():
    btn_tw_dark = make_btn_svg("Twitter / X", "twitter", "dark", width=145, height=36)
    btn_tw_light = make_btn_svg("Twitter / X", "twitter", "light", width=145, height=36)
    btn_em_dark = make_btn_svg("thanhdat.rd.70369@gmail.com", "email", "dark", width=255, height=36)
    btn_em_light = make_btn_svg("thanhdat.rd.70369@gmail.com", "email", "light", width=255, height=36)
    
    with open(os.path.join(ASSETS_DIR, "btn-twitter-dark.svg"), "w", encoding="utf-8") as f:
        f.write(btn_tw_dark)
    with open(os.path.join(ASSETS_DIR, "btn-twitter-light.svg"), "w", encoding="utf-8") as f:
        f.write(btn_tw_light)
    with open(os.path.join(ASSETS_DIR, "btn-email-dark.svg"), "w", encoding="utf-8") as f:
        f.write(btn_em_dark)
    with open(os.path.join(ASSETS_DIR, "btn-email-light.svg"), "w", encoding="utf-8") as f:
        f.write(btn_em_light)

if __name__ == "__main__":
    print("Building full Hark Design System assets...")
    build_heroes()
    build_footers()
    build_buttons()
    print("All assets successfully built in:", ASSETS_DIR)
