# AI Video Editor

**FFmpeg + Python scripts that cut one raw clip into several styled edits: color grade, zoom punches, speed ramps, flash cuts, music and word-by-word captions.**

Editing the same footage three ways by hand takes an afternoon. These scripts are the pipeline behind a Claude Code-driven editing workflow, shared as working reference code.

## What it does

- Color grade presets (energy, cinematic, clean) as FFmpeg filter strings in `config.py`.
- Zoom punches done by crop and upscale, and speed ramps from 0.5x to 1.5x.
- Flash-cut and crossfade transitions.
- Music mixed under the clip with fades.
- TikTok/Reels-style animated captions through `pycaps`.
- `energy_edit.py` builds one high-energy edit; `three_versions.py` builds three styles at once (breakbeat, cinematic, soul); `create_pdf.py` builds a PDF guide.

## Quickstart

Requires Python, FFmpeg on your PATH, and the packages in `requirements.txt` (`pip install pycaps fpdf2`).

```bash
git clone https://github.com/waseemnasir2k26/ai-video-editor
cd ai-video-editor
pip install pycaps fpdf2
# edit the path constants at the top of the script first (VIDEO, MUSIC, TEMP, OUTPUT_DIR)
python three_versions.py
```

The scripts currently contain hard-coded Windows paths from the author's machine. Change them to your own files before running; they will not work as-is. Music files are not included, so supply your own royalty-free tracks.

## For you if

You are comfortable reading Python and FFmpeg commands and want a starting point for scripted, repeatable short-form edits.

## Status and limits

- Reference code, not a polished CLI. No tests, no argument parsing.
- A `/video-edit` Claude Code skill is mentioned in earlier docs but is not part of this repo.
- Check the license of any music you add.
- Last reviewed October 2026.

## Built by SkynetLabs

Built by [SkynetLabs](https://skynetjoe.com). Questions: info@skynetjoe.com

Need this wired into your business? SkynetLabs builds voice agents, n8n back offices and sites that convert → https://skynetjoe.com
