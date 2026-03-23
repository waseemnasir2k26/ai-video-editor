#!/usr/bin/env python3
"""
Shared configuration and presets for AI Video Editor.
Import these into your edit scripts to keep settings consistent.
"""

# =====================================================================
# COLOR GRADE PRESETS (all bright, no crushed blacks)
# =====================================================================
GRADES = {
    "energy": (
        "eq=brightness=0.06:contrast=1.15:saturation=0.90,"
        "colorbalance=rs=0.06:gs=0.02:bs=-0.04:rm=0.04:gm=0.01:bm=-0.02,"
        "unsharp=5:5:0.5"
    ),
    "cinematic": (
        "eq=brightness=0.04:contrast=1.10:saturation=0.82,"
        "colorbalance=rs=0.08:gs=0.03:bs=-0.03:rm=0.05:gm=0.02:bm=-0.02,"
        "unsharp=3:3:0.4"
    ),
    "clean": (
        "eq=brightness=0.05:contrast=1.08:saturation=0.95,"
        "colorbalance=rs=0.04:gs=0.02:bs=-0.02:rm=0.03:gm=0.01:bm=-0.01,"
        "unsharp=3:3:0.3"
    ),
    "dark_mood": (
        "eq=brightness=-0.01:contrast=1.20:saturation=0.75,"
        "colorbalance=rs=0.06:gs=0.02:bs=-0.05:rm=0.04:gm=0.01:bm=-0.03,"
        "unsharp=4:4:0.5,"
        "vignette=angle=PI/5"
    ),
}

# =====================================================================
# ZOOM PRESETS (for 1920x1080 source)
# crop_w, crop_h -> then scale back to 1920x1080
# =====================================================================
ZOOMS = {
    "wide":         None,                        # Full frame, no crop
    "medium":       (1477, 831),                 # ~1.3x zoom
    "medium_tight": (1280, 720),                 # ~1.5x zoom
    "tight":        (1067, 600),                 # ~1.8x zoom
    "extreme":      (960, 540),                  # ~2.0x zoom
}

# =====================================================================
# SPEED PRESETS
# =====================================================================
SPEEDS = {
    "dramatic_slow": 0.50,     # Key moments, reactions
    "smooth_slow":   0.65,     # Detail shots, writing
    "subtle_slow":   0.80,     # Cinematic feel
    "normal":        1.00,     # Natural speed
    "slight_fast":   1.20,     # Energy boost
    "fast":          1.35,     # Quick establishing shots
    "very_fast":     1.50,     # Rapid cuts, high energy
}

# =====================================================================
# TRANSITION SETTINGS
# =====================================================================
FLASH_DURATION = 0.083           # ~2 frames at 24fps
CROSSFADE_DURATION = 0.4         # seconds
CROSSFADE_TYPES = [
    "fade", "fadeblack", "smoothleft", "smoothright", "dissolve", "fadewhite"
]

# =====================================================================
# ENCODING DEFAULTS
# =====================================================================
ENCODE = {
    "codec": "libx264",
    "preset_fast": "fast",       # For individual clips
    "preset_final": "medium",    # For final output
    "crf_clips": "16",           # Quality for clips
    "crf_final": "17",           # Quality for final
    "audio_codec": "aac",
    "audio_bitrate": "192k",
    "pixel_format": "yuv420p",
    "framerate": "24000/1001",   # 23.976fps
}

# =====================================================================
# LETTERBOX & STYLE
# =====================================================================
LETTERBOX_HEIGHT = 55            # px top and bottom
MUSIC_VOLUME = {
    "background": 0.35,         # With voiceover/dialogue
    "medium": 0.40,             # Default for no-dialogue
    "dominant": 0.50,           # Music video feel
}

# =====================================================================
# PYCAPS CAPTION SETTINGS
# =====================================================================
CAPTION_TEMPLATES = {
    "energy": "hype",
    "cinematic": "gentle",
    "clean": "default",
}
