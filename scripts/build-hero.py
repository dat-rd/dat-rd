import os
import io
import base64
from PIL import Image, ImageFilter, ImageDraw

# Hark Pro / Apple Neo-Minimalism Architecture:
# - Organic billowing cloudscape / twilight smoke (recreating Hark's exact theme background)
# - Chamfered specular glass rim highlight
# - Frosted Dynamic Island status pill with live emerald beacon
# - Pure typographic discipline, no visual noise

W, H = 1200, 420
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")

def generate_hark_dark_cloud():
    """Generates Hark Pro dark theme midnight-twilight cloudscape."""
    img = Image.new("RGBA", (W, H), (15, 20, 32, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Base sky gradient: rich indigo dusk down to midnight slate
    for y in range(H):
        t = y / H
        r = int(52 * (1 - t) + 16 * t)
        g = int(68 * (1 - t) + 22 * t)
        b = int(108 * (1 - t) + 36 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
    
    cloud_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cloud_img)
    
    # 2. Billowing violet-slate clouds and mist (matching Hark screenshot)
    cdraw.ellipse([W*0.28, H*0.42, W*0.82, H*1.28], fill=(98, 105, 136, 210))
    cdraw.ellipse([W*0.02, H*0.46, W*0.54, H*1.22], fill=(88, 95, 126, 195))
    cdraw.ellipse([W*0.62, H*0.18, W*1.18, H*0.92], fill=(68, 86, 138, 180))
    cdraw.ellipse([-W*0.15, H*0.15, W*0.42, H*0.85], fill=(62, 78, 126, 185))
    cdraw.ellipse([W*0.25, -H*0.28, W*0.75, H*0.48], fill=(92, 118, 175, 135))
    cdraw.ellipse([W*0.12, H*0.62, W*0.88, H*1.38], fill=(112, 116, 145, 215))
    
    cloud_blurred = cloud_img.filter(ImageFilter.GaussianBlur(radius=64))
    final_img = Image.alpha_composite(img, cloud_blurred)
    
    buf = io.BytesIO()
    final_img.save(buf, format="WEBP", quality=88)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def generate_hark_light_cloud():
    """Generates Hark Pro light theme ethereal daylight cloudscape."""
    img = Image.new("RGBA", (W, H), (235, 242, 250, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Base sky gradient: cornflower azure down to pure pearl
    for y in range(H):
        t = y / H
        r = int(88 * (1 - t) + 236 * t)
        g = int(128 * (1 - t) + 243 * t)
        b = int(182 * (1 - t) + 252 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
        
    cloud_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cloud_img)
    
    # 2. Billowing soft white clouds and sunlit haze
    cdraw.ellipse([W*0.20, H*0.28, W*0.68, H*0.96], fill=(255, 255, 255, 230))
    cdraw.ellipse([W*0.06, H*0.42, W*0.94, H*1.28], fill=(255, 255, 255, 250))
    cdraw.ellipse([W*0.56, -H*0.15, W*1.10, H*0.65], fill=(110, 150, 202, 150))
    cdraw.ellipse([-W*0.10, H*0.18, W*0.45, H*0.88], fill=(245, 250, 255, 210))
    cdraw.ellipse([W*0.28, H*0.02, W*0.80, H*0.62], fill=(255, 255, 255, 185))
    
    cloud_blurred = cloud_img.filter(ImageFilter.GaussianBlur(radius=60))
    final_img = Image.alpha_composite(img, cloud_blurred)
    
    buf = io.BytesIO()
    final_img.save(buf, format="WEBP", quality=88)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def build_svgs():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    
    dark_b64 = generate_hark_dark_cloud()
    light_b64 = generate_hark_light_cloud()
    
    # Dark Mode SVG
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Nguyen Thanh Dat</title>
<desc id="d">Building software with AI, agents and modern engineering workflows.</desc>
<defs>
  <clipPath id="cardClip">
    <rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="24"/>
  </clipPath>

  <!-- Specular Glass Rim Stroke -->
  <linearGradient id="rimStroke" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#ABC0E4" stop-opacity="0.55"/>
    <stop offset="25%" stop-color="#6B82A8" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#243144" stop-opacity="0.15"/>
  </linearGradient>

  <!-- Pill Frosted Surface -->
  <linearGradient id="pillBg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#202A3D" stop-opacity="0.88"/>
    <stop offset="100%" stop-color="#121824" stop-opacity="0.88"/>
  </linearGradient>
  <linearGradient id="pillStroke" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#8EA8D4" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#344663" stop-opacity="0.3"/>
  </linearGradient>

  <!-- Diffuse Glow behind Pill -->
  <radialGradient id="pillAura" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#7397D4" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#7397D4" stop-opacity="0"/>
  </radialGradient>
</defs>

<style>
  .f {{ font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Segoe UI", Helvetica, Arial, sans-serif; }}
  .mono {{ font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }}
  
  .pulse-dot {{
    animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }}
  @keyframes livePulse {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.45; transform: scale(0.85); }}
  }}

  .halo {{
    animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite;
    transform-origin: center;
  }}
  @keyframes ring {{
    0% {{ r: 4px; opacity: 0.8; stroke-width: 1.5px; }}
    100% {{ r: 14px; opacity: 0; stroke-width: 0.5px; }}
  }}

  @media (prefers-reduced-motion: reduce) {{
    .pulse-dot, .halo {{ animation: none; }}
  }}
</style>

<!-- 1. Hark Atmospheric Cloudscape Background (Clipped) -->
<g clip-path="url(#cardClip)">
  <image href="data:image/webp;base64,{dark_b64}" x="12" y="12" width="{W - 24}" height="{H - 24}" preserveAspectRatio="none"/>
  
  <!-- Subtle Vignette Scrim (Light, preserves vivid cloud shapes) -->
  <rect x="12" y="12" width="{W - 24}" height="{H - 24}" fill="#080C14" fill-opacity="0.18"/>
  
  <!-- Diffuse Glow behind status pill -->
  <ellipse cx="{W/2}" cy="74" rx="230" ry="44" fill="url(#pillAura)"/>
</g>

<!-- 2. Specular Rim Stroke -->
<rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="24" fill="none" stroke="url(#rimStroke)" stroke-width="1.2"/>

<!-- 3. Top Status Pill (Hark Pro Style) -->
<g class="f" transform="translate({W/2}, 74)">
  <rect x="-174" y="-19" width="348" height="38" rx="19" fill="url(#pillBg)" stroke="url(#pillStroke)" stroke-width="1"/>
  
  <!-- Live Signal Indicator -->
  <g transform="translate(-144, 0)">
    <circle class="halo" cx="0" cy="0" r="4" fill="none" stroke="#3FB950"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4.2" fill="#3FB950"/>
  </g>
  
  <!-- Pill Label -->
  <text x="-124" y="4" font-size="12" font-weight="500" fill="#E2E8F0" letter-spacing="0.4px">
    SOFTWARE × AI × ENTERPRISE
  </text>
  <text x="146" y="4" text-anchor="end" font-size="11" font-weight="600" fill="#B4C6FF" letter-spacing="1px" class="mono">
    DAT-RD
  </text>
</g>

<!-- 4. Main Headline Typography -->
<g class="f" text-anchor="middle">
  <text x="{W/2}" y="196" font-size="54" font-weight="700" fill="#FFFFFF" letter-spacing="-1.2px">
    Nguyen Thanh Dat
  </text>
  
  <text x="{W/2}" y="254" font-size="22" font-weight="400" fill="#E2E8F0" letter-spacing="-0.3px">
    Building software with AI, agents &amp; modern engineering workflows.
  </text>

  <text x="{W/2}" y="295" font-size="15" font-weight="400" fill="#A8B7CD" letter-spacing="0.2px">
    Exploring the intersection of deterministic enterprise software &amp; autonomous AI systems.
  </text>
</g>

<!-- 5. Hairline Divider for Metadata -->
<line x1="48" y1="{H - 64}" x2="{W - 48}" y2="{H - 64}" stroke="#475569" stroke-opacity="0.35" stroke-width="1"/>

<!-- 6. Bottom Metadata / Architecture Ticks -->
<g class="f mono" font-size="11" fill="#94A3B8">
  <text x="48" y="{H - 38}">SYS.STATUS // ACTIVE</text>
  <text x="{W/2}" y="{H - 38}" text-anchor="middle">FPT UNIVERSITY → FPT SOFTWARE → AI SYSTEMS</text>
  <text x="{W - 48}" y="{H - 38}" text-anchor="end">VIETNAM // 2026</text>
</g>

</svg>'''

    # Light Mode SVG
    light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Nguyen Thanh Dat</title>
<desc id="d">Building software with AI, agents and modern engineering workflows.</desc>
<defs>
  <clipPath id="cardClipLight">
    <rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="24"/>
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
  
  .pulse-dot {{
    animation: livePulse 2.8s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }}
  @keyframes livePulse {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.45; transform: scale(0.85); }}
  }}

  .halo {{
    animation: ring 2.8s cubic-bezier(0, 0.2, 0.8, 1) infinite;
    transform-origin: center;
  }}
  @keyframes ring {{
    0% {{ r: 4px; opacity: 0.8; stroke-width: 1.5px; }}
    100% {{ r: 14px; opacity: 0; stroke-width: 0.5px; }}
  }}

  @media (prefers-reduced-motion: reduce) {{
    .pulse-dot, .halo {{ animation: none; }}
  }}
</style>

<g clip-path="url(#cardClipLight)">
  <image href="data:image/webp;base64,{light_b64}" x="12" y="12" width="{W - 24}" height="{H - 24}" preserveAspectRatio="none"/>
  <rect x="12" y="12" width="{W - 24}" height="{H - 24}" fill="#FFFFFF" fill-opacity="0.18"/>
</g>

<rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="24" fill="none" stroke="url(#rimStrokeLight)" stroke-width="1.2"/>

<g class="f" transform="translate({W/2}, 74)">
  <rect x="-174" y="-19" width="348" height="38" rx="19" fill="url(#pillBgLight)" stroke="url(#pillStrokeLight)" stroke-width="1"/>
  
  <g transform="translate(-144, 0)">
    <circle class="halo" cx="0" cy="0" r="4" fill="none" stroke="#1A7F37"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4.2" fill="#1A7F37"/>
  </g>
  
  <text x="-124" y="4" font-size="12" font-weight="600" fill="#334155" letter-spacing="0.4px">
    SOFTWARE × AI × ENTERPRISE
  </text>
  <text x="146" y="4" text-anchor="end" font-size="11" font-weight="700" fill="#4338CA" letter-spacing="1px" class="mono">
    DAT-RD
  </text>
</g>

<g class="f" text-anchor="middle">
  <text x="{W/2}" y="196" font-size="54" font-weight="700" fill="#0F172A" letter-spacing="-1.2px">
    Nguyen Thanh Dat
  </text>
  
  <text x="{W/2}" y="254" font-size="22" font-weight="500" fill="#334155" letter-spacing="-0.3px">
    Building software with AI, agents &amp; modern engineering workflows.
  </text>

  <text x="{W/2}" y="295" font-size="15" font-weight="400" fill="#64748B" letter-spacing="0.2px">
    Exploring the intersection of deterministic enterprise software &amp; autonomous AI systems.
  </text>
</g>

<line x1="48" y1="{H - 64}" x2="{W - 48}" y2="{H - 64}" stroke="#CBD5E1" stroke-opacity="0.8" stroke-width="1"/>

<g class="f mono" font-size="11" fill="#64748B">
  <text x="48" y="{H - 38}">SYS.STATUS // ACTIVE</text>
  <text x="{W/2}" y="{H - 38}" text-anchor="middle">FPT UNIVERSITY → FPT SOFTWARE → AI SYSTEMS</text>
  <text x="{W - 48}" y="{H - 38}" text-anchor="end">VIETNAM // 2026</text>
</g>

</svg>'''

    dark_path = os.path.join(ASSETS_DIR, "hero-dark.svg")
    light_path = os.path.join(ASSETS_DIR, "hero-light.svg")
    
    with open(dark_path, "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(light_path, "w", encoding="utf-8") as f:
        f.write(light_svg)
        
    print(f"Generated {dark_path} ({os.path.getsize(dark_path)} bytes)")
    print(f"Generated {light_path} ({os.path.getsize(light_path)} bytes)")

if __name__ == "__main__":
    build_svgs()
