#!/usr/bin/env python3
"""
ENERGY EDIT V3 - Zoom punches, speed ramping, flash cuts, hard-hitting music
"""
import subprocess, os, sys, json

TEMP = "C:/Users/info/OneDrive/Desktop/video_edit_temp"
VIDEO = "C:/Users/info/OneDrive/Desktop/short_business_chat.mp4"
MUSIC = f"{TEMP}/music_hiphop.mp3"
OUTPUT_DIR = "C:/Users/info/OneDrive/Desktop/business meeting"
OUTPUT_BASE = f"{TEMP}/v3_energy_base.mp4"
OUTPUT_FINAL = f"{OUTPUT_DIR}/final_energy_edit.mp4"

# === AGGRESSIVE COLOR GRADE ===
# Crushed blacks, high contrast, warm tones, desaturated, sharp, vignette
COLOR_GRADE = (
    "eq=brightness=-0.02:contrast=1.28:saturation=0.70,"
    "colorbalance=rs=0.08:gs=0.02:bs=-0.06:rm=0.06:gm=0.01:bm=-0.04,"
    "unsharp=5:5:0.6,"
    "vignette=angle=PI/5"
)

# === CLIP DEFINITIONS ===
# (start, end, speed, zoom_spec, description)
# zoom_spec: None = wide, or (crop_w, crop_h, crop_x, crop_y)
CLIPS = [
    # 1. WIDE opening - setting the scene
    (0, 2.5, 1.0, None,
     "wide opening"),

    # 2. TIGHT zoom left person writing - SLOW MO
    (3, 5.5, 0.60, (1067, 600, 46, 80),
     "slow-mo close-up writing"),

    # 3. WIDE both on laptops - FAST energy
    (10, 12.5, 1.35, None,
     "wide laptops fast"),

    # 4. TIGHT zoom right person typing
    (12.5, 14.5, 1.0, (1200, 675, 720, 82),
     "zoom right typing"),

    # 5. MEDIUM zoom pointing at laptop - FAST
    (16, 18.5, 1.40, (1477, 831, 211, 34),
     "medium zoom pointing fast"),

    # 6. TIGHT zoom left - DRAMATIC SLOW MO (pointing up moment)
    (22, 24.5, 0.50, (1067, 600, 46, 120),
     "DRAMATIC slow-mo"),

    # 7. WIDE pitching - energy
    (30, 32.5, 1.25, None,
     "wide pitch energy"),

    # 8. MEDIUM zoom both - slow finale
    (36, 39, 0.60, (1477, 831, 211, 34),
     "slow zoom finale"),
]

FLASH_DUR = 0.083  # ~2 frames at 24fps - SNAPPY flash


def run(cmd, timeout=120):
    r = subprocess.run(cmd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr[-800:]}")
        return False
    return True


def get_duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True
    )
    return float(r.stdout.strip())


def step1_process_clips():
    """Extract and process each clip with zoom + speed + color grade"""
    print("\n[STEP 1] Processing clips...")
    files = []

    for i, (start, end, speed, zoom, desc) in enumerate(CLIPS):
        out = f"{TEMP}/clip_{i:02d}.mp4"
        files.append(out)

        # Build filter chain
        vf_parts = [
            f"trim=start={start}:end={end}",
            "setpts=PTS-STARTPTS",
        ]

        # Speed change
        if speed != 1.0:
            vf_parts.append(f"setpts=PTS/{speed}")

        # Zoom (crop + scale)
        if zoom:
            cw, ch, cx, cy = zoom
            vf_parts.append(f"crop={cw}:{ch}:{cx}:{cy}")
            vf_parts.append("scale=1920:1080:flags=lanczos")

        # Color grade
        vf_parts.append(COLOR_GRADE)

        vf = ",".join(vf_parts)
        out_dur = (end - start) / speed

        cmd = [
            "ffmpeg", "-y", "-i", VIDEO,
            "-vf", vf, "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "16",
            "-pix_fmt", "yuv420p", "-r", "24000/1001",
            out
        ]

        print(f"  Clip {i}: {desc} ({out_dur:.1f}s) ", end="", flush=True)
        if run(cmd):
            print("OK")
        else:
            return None

    return files


def step2_create_flash():
    """Create a quick white flash clip"""
    print("\n[STEP 2] Creating flash transition...")
    out = f"{TEMP}/flash.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i",
        f"color=white:s=1920x1080:d={FLASH_DUR}:r=24000/1001",
        "-c:v", "libx264", "-preset", "fast", "-crf", "16",
        "-pix_fmt", "yuv420p", out
    ]
    if run(cmd):
        print("  Flash OK")
        return out
    return None


def step3_assemble(clip_files, flash_file):
    """Concatenate clips with flash transitions between them"""
    print("\n[STEP 3] Assembling with flash cuts...")
    concat_list = f"{TEMP}/concat_list.txt"

    with open(concat_list, 'w') as f:
        for i, clip in enumerate(clip_files):
            # Use Windows paths with forward slashes
            f.write(f"file '{clip}'\n")
            if i < len(clip_files) - 1:
                f.write(f"file '{flash_file}'\n")

    out = f"{TEMP}/assembled.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy", out
    ]

    if run(cmd):
        dur = get_duration(out)
        print(f"  Assembled: {dur:.1f}s")
        return out
    return None


def step4_add_music(assembled):
    """Add letterbox, fades, and hard-hitting music"""
    print("\n[STEP 4] Adding music + letterbox + fades...")
    dur = get_duration(assembled)

    fg_file = f"{TEMP}/fg_energy.txt"
    fg = (
        # Video: thin letterbox + fades
        f"[0:v]drawbox=x=0:y=0:w=1920:h=70:color=black:t=fill,"
        f"drawbox=x=0:y=1010:w=1920:h=70:color=black:t=fill,"
        f"fade=t=in:st=0:d=0.6,"
        f"fade=t=out:st={dur - 1.0:.4f}:d=1.0[vout];\n"
        # Audio: music, louder for energy
        f"[1:a]atrim=0:{dur:.4f},asetpts=PTS-STARTPTS,"
        f"afade=t=in:d=0.8,"
        f"afade=t=out:st={dur - 1.5:.4f}:d=1.5,"
        f"volume=0.45[aout]"
    )

    with open(fg_file, 'w') as f:
        f.write(fg)

    cmd = [
        "ffmpeg", "-y",
        "-i", assembled, "-i", MUSIC,
        "-filter_complex_script", fg_file,
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "17",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        OUTPUT_BASE
    ]

    if run(cmd, timeout=300):
        dur = get_duration(OUTPUT_BASE)
        mb = os.path.getsize(OUTPUT_BASE) / 1048576
        print(f"  Base video: {dur:.1f}s, {mb:.1f} MB")
        return True
    return False


def step5_add_captions():
    """Add animated captions via pycaps"""
    print("\n[STEP 5] Adding animated captions (pycaps)...")

    dur = get_duration(OUTPUT_BASE)

    # Create SRT with punchy motivational captions
    srt = f"{TEMP}/energy_captions.srt"
    # Shorter, punchier phrases synced to the cuts
    # Calculate rough clip boundaries
    clip_times = []
    t = 0
    for i, (start, end, speed, zoom, desc) in enumerate(CLIPS):
        clip_dur = (end - start) / speed
        clip_times.append((t, t + clip_dur))
        t += clip_dur + FLASH_DUR  # account for flash

    captions = [
        (clip_times[1][0] + 0.2, clip_times[1][1] - 0.2, "every empire starts here"),
        (clip_times[2][0] + 0.1, clip_times[3][1] - 0.1, "deep in the zone"),
        (clip_times[4][0] + 0.1, clip_times[4][1] - 0.1, "execute relentlessly"),
        (clip_times[5][0] + 0.3, clip_times[5][1] - 0.3, "while they sleep we grind"),
        (clip_times[6][0] + 0.1, clip_times[7][0] - 0.1, "from vision to reality"),
        (clip_times[7][0] + 0.3, clip_times[7][1] - 0.5, "never stop building"),
    ]

    with open(srt, 'w') as f:
        for i, (s, e, text) in enumerate(captions):
            s = max(0, min(s, dur - 0.5))
            e = max(s + 0.5, min(e, dur - 0.2))
            sh, sm, ss = int(s//3600), int((s%3600)//60), s%60
            eh, em, es = int(e//3600), int((e%3600)//60), e%60
            f.write(f"{i+1}\n")
            f.write(f"{sh:02d}:{sm:02d}:{ss:06.3f} --> {eh:02d}:{em:02d}:{es:06.3f}\n".replace('.', ','))
            f.write(f"{text}\n\n")

    print(f"  Captions: {[c[2] for c in captions]}")

    # Run pycaps with hype template
    cmd_str = (
        f'pycaps render --input "{OUTPUT_BASE}" --output "{OUTPUT_FINAL}" '
        f'--template hype --transcript "{srt}" --transcript-format srt '
        f'--lang en --video-quality high'
    )

    result = subprocess.run(
        cmd_str, shell=True, capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=300,
        cwd=TEMP
    )

    if result.returncode != 0:
        print(f"  pycaps ERROR: {result.stderr[-500:]}")
        # Fallback: copy base video without pycaps captions
        import shutil
        shutil.copy2(OUTPUT_BASE, OUTPUT_FINAL)
        print(f"  Fallback: copied base video (no animated captions)")
        return True

    mb = os.path.getsize(OUTPUT_FINAL) / 1048576
    print(f"  Final: {OUTPUT_FINAL} ({mb:.1f} MB)")
    return True


# === MAIN ===
if __name__ == "__main__":
    print("=" * 50)
    print("  ENERGY EDIT V3 - ZOOM PUNCHES + SPEED RAMP")
    print("=" * 50)

    clips = step1_process_clips()
    if not clips:
        sys.exit(1)

    flash = step2_create_flash()
    if not flash:
        sys.exit(1)

    assembled = step3_assemble(clips, flash)
    if not assembled:
        sys.exit(1)

    if not step4_add_music(assembled):
        sys.exit(1)

    if not step5_add_captions():
        sys.exit(1)

    dur = get_duration(OUTPUT_FINAL)
    mb = os.path.getsize(OUTPUT_FINAL) / 1048576
    print("\n" + "=" * 50)
    print(f"  DONE! {dur:.1f}s | {mb:.1f} MB")
    print(f"  {OUTPUT_FINAL}")
    print("=" * 50)
