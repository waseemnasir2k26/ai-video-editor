# Changelog

All notable changes to this project are documented in this file.

## [2026.10] - 2026-10-12

- Public MIT Python + FFmpeg pipeline (`energy_edit.py`, `three_versions.py`, `config.py`, `create_pdf.py`) that turns one raw clip into several graded, captioned edits via pycaps.
- Reviewed October 2026: README links checked (ffmpeg.org, Calendly, Fiverr, sibling repos, skynetjoe.com, WhatsApp all respond 200); no dead links found. No script or preset changes.
- Hire section links normalised to the three canonical SkynetLabs destinations (Fiverr agency, Upwork profile, Calendly) and the Fiverr URL moved to the www form.
- Known gaps: no `pyproject.toml`/setup, unpinned dependencies in `requirements.txt`, no tests, CI or sample input/output; last functional commit was July 2026 (MIT license added).

## [2026.09] - 2026-09-16

- Maintenance review of ai-video-editor — a public, MIT-licensed Python + FFmpeg video-editing pipeline that turns one raw clip into several professionally graded edits.
- Status: four scripts and a requirements file — `energy_edit.py` (single high-energy edit), `three_versions.py` (three variants: breakbeat, cinematic, soul), `config.py` (shared colour-grade, zoom and speed-ramp presets) and `create_pdf.py` (lead-magnet PDF). Depends on pycaps and fpdf2 plus FFmpeg on PATH, and is driven from Claude Code via a `/video-edit` prompt.
- Reviewed September 2026: README Status section added and a CHANGELOG created; the repo is versioned as v2026.09. No script, preset or dependency changes.
- Known gaps: no CHANGELOG before this release; no packaging metadata (`setup.py`/`pyproject.toml`) and no pinned dependency versions in `requirements.txt`; no tests, no CI, and no sample input/output committed; last functional commit was July 2026.
