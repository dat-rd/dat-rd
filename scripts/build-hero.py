import os

# Hark / Apple Style:
# Extreme typographic restraint, tactile status pill, generous spatial balance.
# No particle noise, no pseudo-flowchart. Just pure, expensive-looking clarity.

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "card_bg": "#161B22",
        "card_border": "#30363D",
        "text_primary": "#F0F6FC",
        "text_secondary": "#8B949E",
        "text_muted": "#6E7681",
        "pill_bg": "#1C2128",
        "pill_border": "#383E47",
        "pill_text": "#C9D1D9",
        "dot_live": "#3FB950",
        "accent": "#7C86FF",
        "file": "hero-hark-dark.svg"
    },
    "light": {
        "bg": "#FFFFFF",
        "card_bg": "#F6F8FA",
        "card_border": "#D0D7DE",
        "text_primary": "#1F2328",
        "text_secondary": "#57606A",
        "text_muted": "#8C959F",
        "pill_bg": "#EFF1F3",
        "pill_border": "#D8DEE4",
        "pill_text": "#424A53",
        "dot_live": "#1A7F37",
        "accent": "#4F46E5",
        "file": "hero-hark-light.svg"
    }
}

W, H = 1200, 420

for theme, c in THEMES.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Nguyen Thanh Dat</title>
<desc id="d">Building software with AI, agents and modern engineering workflows.</desc>
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

<!-- Background Subtle Card Surface -->
<rect x="16" y="16" width="{W - 32}" height="{H - 32}" rx="24" fill="{c["card_bg"]}" stroke="{c["card_border"]}" stroke-width="1"/>

<!-- Top Status Pill (Hark Pro / Apple Dynamic Island Style) -->
<g class="f" transform="translate({W/2}, 76)">
  <!-- Pill Background -->
  <rect x="-170" y="-18" width="340" height="36" rx="18" fill="{c["pill_bg"]}" stroke="{c["pill_border"]}" stroke-width="1"/>
  
  <!-- Live Signal Indicator -->
  <g transform="translate(-142, 0)">
    <circle class="halo" cx="0" cy="0" r="4" fill="none" stroke="{c["dot_live"]}"/>
    <circle class="pulse-dot" cx="0" cy="0" r="4.2" fill="{c["dot_live"]}"/>
  </g>
  
  <!-- Pill Label -->
  <text x="-124" y="4" font-size="12" font-weight="500" fill="{c["pill_text"]}" letter-spacing="0.3px">
    SOFTWARE × AI × ENTERPRISE
  </text>
  <text x="142" y="4" text-anchor="end" font-size="11" font-weight="600" fill="{c["accent"]}" letter-spacing="1px" class="mono">
    DAT-RD
  </text>
</g>

<!-- Main Headline Typography -->
<g class="f" text-anchor="middle">
  <!-- Name -->
  <text x="{W/2}" y="196" font-size="54" font-weight="700" fill="{c["text_primary"]}" letter-spacing="-1.2px">
    Nguyen Thanh Dat
  </text>
  
  <!-- Primary Positioning Statement -->
  <text x="{W/2}" y="254" font-size="22" font-weight="400" fill="{c["text_secondary"]}" letter-spacing="-0.3px">
    Building software with AI, agents &amp; modern engineering workflows.
  </text>

  <!-- Secondary Anchor -->
  <text x="{W/2}" y="294" font-size="15" font-weight="400" fill="{c["text_muted"]}" letter-spacing="0.2px">
    Exploring the intersection of deterministic enterprise software &amp; autonomous AI systems.
  </text>
</g>

<!-- Bottom Metadata / Architecture Ticks -->
<g class="f mono" font-size="11" fill="{c["text_muted"]}">
  <text x="48" y="{H - 42}">SYS.STATUS // ACTIVE</text>
  <text x="{W/2}" y="{H - 42}" text-anchor="middle">FPT UNIVERSITY → FPT SOFTWARE → AI SYSTEMS</text>
  <text x="{W - 48}" y="{H - 42}" text-anchor="end">VIETNAM // 2026</text>
</g>

</svg>'''
    with open(f"{c['file']}", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {c['file']}")

