# AI Video Editor

Professional multi-version video editing pipeline powered by **Claude Code + FFmpeg + Python + pycaps**.

Turn raw footage into multiple professional edits using nothing but AI prompts.

## What It Does

Takes a raw video and produces multiple professionally edited versions with:
- **Color grading** (bright energy, cinematic warm, clean natural)
- **Zoom punches** (simulated camera cuts via crop + upscale)
- **Speed ramping** (0.5x slow-mo to 1.5x fast)
- **Transitions** (white flash cuts, smooth crossfades)
- **Royalty-free music** (auto-mixed with fades)
- **Animated captions** (TikTok/Reels-style word-by-word via pycaps)

## Quick Start

```bash
# Install dependencies
pip install pycaps fpdf2

# FFmpeg must be installed and in PATH
# https://ffmpeg.org/download.html

# In Claude Code, just type:
/video-edit
```

Then give it your video file path and describe what you want.

## Scripts

| Script | Purpose |
|--------|---------|
| `energy_edit.py` | Single high-energy edit (zoom punches, flash cuts, hip-hop) |
| `three_versions.py` | 3 versions at once (breakbeat, cinematic, soul) |
| `create_pdf.py` | Generate lead magnet PDF guide |
| `config.py` | Shared presets (color grades, zoom levels, speed ramps) |

## Edit Styles

### Breakbeat Energy
Fast cuts (1-2s each), aggressive zoom punches, white flash transitions, breakbeat music. Speed: 0.5x-1.5x.

### Cinematic Epic
Longer clips (4-8s), heavy slow-motion (0.5x-0.85x), smooth crossfades, orchestral music.

### Clean Soul
Medium clips (3-5s), gentle zooms, smooth crossfades, soul/lo-fi music. Natural feel.

### Hip-Hop Energy
Mixed speed ramping, tight crops, flash cuts, hip-hop track. High contrast.

## Color Grade Presets

```python
ENERGY    = "eq=brightness=0.06:contrast=1.15:saturation=0.90,colorbalance=rs=0.06:gs=0.02:bs=-0.04,unsharp=5:5:0.5"
CINEMATIC = "eq=brightness=0.04:contrast=1.10:saturation=0.82,colorbalance=rs=0.08:gs=0.03:bs=-0.03,unsharp=3:3:0.4"
CLEAN     = "eq=brightness=0.05:contrast=1.08:saturation=0.95,colorbalance=rs=0.04:gs=0.02:bs=-0.02,unsharp=3:3:0.3"
```

## Requirements

- Python 3.8+
- FFmpeg (with libx264)
- pycaps (`pip install pycaps`)
- fpdf2 (`pip install fpdf2`) - for PDF generation only

## Author

**Waseem Nasir** - [skynetjoe.com](https://skynetjoe.com) | [waseemnasir.com](https://waseemnasir.com)

Built with Claude Code by Anthropic.

---

<!-- SEO-HIRE-ME-BLOCK -->

## Hire Me

> **Need automated video editing for reels, shorts, or YouTube?**

I'm **Waseem Nasir** — founder of [Skynet Labs / SkynetJoe](https://www.skynetjoe.com), an AI Automation Agency. Multi-version AI video editing pipelines with Claude Code + FFmpeg + pycaps.

**50+ live projects across:** Healthcare · Legal · Real Estate · E-Commerce · Logistics · HVAC · SaaS · Consulting

### Hire me
- 📅 **[Book a free strategy call](https://calendly.com/skynetlabs/schedule-a-free-consultation)**
- 💼 **[Hire on Fiverr](https://fiverr.com/agencies/skynetjoellc)**
- 🌐 **[skynetjoe.com](https://www.skynetjoe.com)**
- 📧 **info@skynetjoe.com**
- 💬 **[WhatsApp](https://wa.me/923001001957)**

### Related projects on my GitHub
- [ai-motivational-posts](https://github.com/waseemnasir2k26/ai-motivational-posts)
- [fiverr-gig-optimizer](https://github.com/waseemnasir2k26/fiverr-gig-optimizer)
- [aeo-content-engine](https://github.com/waseemnasir2k26/aeo-content-engine)
- [→ See all 50+ projects](https://github.com/waseemnasir2k26)

### Tags
`AI automation` · `n8n` · `GoHighLevel` · `Claude Code` · `Next.js` · `React` · `Python` · `freelance` · `hire me` · `agency`
