#!/usr/bin/env python3
"""
3 VIDEO VERSIONS - All with BRIGHT color grades (no dark crushing)
V1: Breakbeat Energy - fast cuts, zoom punches, breakbeat music
V2: Cinematic Epic  - dramatic slow-mo, epic orchestral, smooth transitions
V3: Clean Soul      - smooth flow, soul music, minimal effects
"""
import subprocess, os, sys, shutil

TEMP = "C:/Users/info/OneDrive/Desktop/video_edit_temp"
VIDEO = "C:/Users/info/OneDrive/Desktop/short_business_chat.mp4"
OUTPUT_DIR = "C:/Users/info/OneDrive/Desktop/business meeting"

FLASH_DUR = 0.083  # ~2 frames


def run(cmd, timeout=180):
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


# =====================================================================
# COLOR GRADES - ALL BRIGHT, no vignette, no crushed blacks
# =====================================================================
GRADE_ENERGY = (
    "eq=brightness=0.06:contrast=1.15:saturation=0.90,"
    "colorbalance=rs=0.06:gs=0.02:bs=-0.04:rm=0.04:gm=0.01:bm=-0.02,"
    "unsharp=5:5:0.5"
)

GRADE_CINEMATIC = (
    "eq=brightness=0.04:contrast=1.10:saturation=0.82,"
    "colorbalance=rs=0.08:gs=0.03:bs=-0.03:rm=0.05:gm=0.02:bm=-0.02,"
    "unsharp=3:3:0.4"
)

GRADE_CLEAN = (
    "eq=brightness=0.05:contrast=1.08:saturation=0.95,"
    "colorbalance=rs=0.04:gs=0.02:bs=-0.02:rm=0.03:gm=0.01:bm=-0.01,"
    "unsharp=3:3:0.3"
)


# =====================================================================
# VERSION 1: BREAKBEAT ENERGY
# Fast cuts, zoom punches, flash transitions, breakbeat music
# =====================================================================
V1_CLIPS = [
    # (start, end, speed, zoom_spec, description)
    (0, 2.0, 1.2, None, "wide opening fast"),
    (3, 5.0, 0.65, (1067, 600, 46, 80), "slow-mo writing zoom"),
    (7, 9.0, 1.5, None, "wide quick energy"),
    (10, 12.0, 1.0, (1200, 675, 720, 82), "tight right person"),
    (14, 16.0, 1.5, (1477, 831, 211, 34), "medium zoom fast"),
    (18, 20.0, 1.3, None, "wide discussion"),
    (22, 24.5, 0.50, (1067, 600, 46, 120), "dramatic slow-mo point"),
    (28, 30.0, 1.4, (1200, 675, 720, 82), "zoom right fast"),
    (32, 34.0, 1.3, None, "wide pitch"),
    (36, 39.0, 0.55, (1477, 831, 211, 34), "slow zoom finale"),
]

V1_CAPTIONS = [
    "every empire starts here",
    "deep in the zone",
    "execute relentlessly",
    "no days off",
    "while they sleep we grind",
    "never stop building",
]

V1_MUSIC = f"{TEMP}/music_breakbeat.mp3"
V1_OUTPUT = f"{OUTPUT_DIR}/v1_breakbeat_energy.mp4"


# =====================================================================
# VERSION 2: CINEMATIC EPIC
# Longer clips, dramatic slow-mo, smooth fades, epic orchestral
# =====================================================================
V2_CLIPS = [
    (0, 3.5, 0.85, None, "wide opening slow"),
    (4, 7.5, 0.55, (1067, 600, 46, 80), "extreme slow-mo writing"),
    (10, 14.0, 1.0, None, "wide both working"),
    (16, 19.0, 0.60, (1200, 675, 720, 82), "slow zoom right person"),
    (22, 26.0, 0.50, (1067, 600, 46, 120), "dramatic pointing slow-mo"),
    (30, 34.0, 0.80, None, "wide pitch moment"),
    (36, 40.0, 0.50, (1477, 831, 211, 34), "epic slow finale"),
]

V2_CAPTIONS = [
    "the vision begins",
    "where legends are forged",
    "building something greater",
    "every detail matters",
    "from nothing to everything",
    "this is just the start",
]

V2_MUSIC = f"{TEMP}/music_epic.mp3"
V2_OUTPUT = f"{OUTPUT_DIR}/v2_cinematic_epic.mp4"


# =====================================================================
# VERSION 3: CLEAN SOUL
# Smooth cuts, natural zoom, soul music, relaxed but cool
# =====================================================================
V3_CLIPS = [
    (0, 4.0, 1.0, None, "wide natural opening"),
    (5, 8.0, 0.80, (1280, 720, 30, 60), "gentle zoom left"),
    (10, 14.0, 1.0, None, "wide both laptops"),
    (15, 18.0, 0.85, (1280, 720, 610, 60), "gentle zoom right"),
    (22, 26.0, 0.75, (1477, 831, 211, 34), "medium both smooth"),
    (30, 34.0, 1.0, None, "wide discussion"),
    (36, 40.0, 0.70, (1280, 720, 320, 80), "smooth zoom finale"),
]

V3_CAPTIONS = [
    "two minds one mission",
    "where it all begins",
    "the quiet grind",
    "ideas into reality",
    "built different",
    "the journey continues",
]

V3_MUSIC = f"{TEMP}/music_soul.mp3"
V3_OUTPUT = f"{OUTPUT_DIR}/v3_clean_soul.mp4"


def process_clips(clips, grade, prefix):
    """Extract and process each clip with zoom + speed + color grade"""
    files = []
    for i, (start, end, speed, zoom, desc) in enumerate(clips):
        out = f"{TEMP}/{prefix}_clip_{i:02d}.mp4"
        files.append(out)

        vf_parts = [
            f"trim=start={start}:end={end}",
            "setpts=PTS-STARTPTS",
        ]
        if speed != 1.0:
            vf_parts.append(f"setpts=PTS/{speed}")
        if zoom:
            cw, ch, cx, cy = zoom
            vf_parts.append(f"crop={cw}:{ch}:{cx}:{cy}")
            vf_parts.append("scale=1920:1080:flags=lanczos")
        vf_parts.append(grade)

        vf = ",".join(vf_parts)
        cmd = [
            "ffmpeg", "-y", "-i", VIDEO,
            "-vf", vf, "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "16",
            "-pix_fmt", "yuv420p", "-r", "24000/1001",
            out
        ]

        out_dur = (end - start) / speed
        print(f"  {prefix} clip {i}: {desc} ({out_dur:.1f}s) ", end="", flush=True)
        if run(cmd):
            print("OK")
        else:
            return None
    return files


def create_flash():
    """Create a quick white flash clip"""
    out = f"{TEMP}/flash.mp4"
    if os.path.exists(out):
        return out
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i",
        f"color=white:s=1920x1080:d={FLASH_DUR}:r=24000/1001",
        "-c:v", "libx264", "-preset", "fast", "-crf", "16",
        "-pix_fmt", "yuv420p", out
    ]
    if run(cmd):
        return out
    return None


def assemble_with_flash(clip_files, flash_file, prefix):
    """Concatenate clips with flash transitions"""
    concat_list = f"{TEMP}/{prefix}_concat.txt"
    with open(concat_list, 'w') as f:
        for i, clip in enumerate(clip_files):
            f.write(f"file '{clip}'\n")
            if i < len(clip_files) - 1:
                f.write(f"file '{flash_file}'\n")

    out = f"{TEMP}/{prefix}_assembled.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy", out
    ]
    if run(cmd):
        return out
    return None


def assemble_with_crossfade(clip_files, prefix, fade_dur=0.5):
    """Concatenate clips with crossfade transitions (no flash)"""
    if len(clip_files) < 2:
        return clip_files[0] if clip_files else None

    # Build xfade chain
    fg_parts = []
    # Get durations
    durs = []
    for cf in clip_files:
        durs.append(get_duration(cf))

    # Input labels
    inputs = " ".join(f"-i \"{cf}\"" for cf in clip_files)

    # Build xfade filter chain
    filter_parts = []
    offsets = []
    acc = durs[0]
    for i in range(len(clip_files) - 1):
        offsets.append(acc - fade_dur)
        acc = acc + durs[i + 1] - fade_dur

    # Chain xfades
    chain = ""
    for i in range(len(clip_files) - 1):
        if i == 0:
            src = "[0:v]"
        else:
            src = f"[x{i}]"
        nxt = f"[{i+1}:v]"
        out_label = f"[x{i+1}]" if i < len(clip_files) - 2 else "[vout]"
        # Alternate between transitions
        transitions = ["fade", "fadeblack", "smoothleft", "smoothright", "fade", "dissolve"]
        trans = transitions[i % len(transitions)]
        chain += f"{src}{nxt}xfade=transition={trans}:duration={fade_dur}:offset={offsets[i]:.4f}{out_label};\n"

    # Write filtergraph
    fg_file = f"{TEMP}/{prefix}_xfade_fg.txt"
    with open(fg_file, 'w') as f:
        f.write(chain.rstrip(";\n"))

    out = f"{TEMP}/{prefix}_assembled.mp4"
    cmd = ["ffmpeg", "-y"]
    for cf in clip_files:
        cmd.extend(["-i", cf])
    cmd.extend([
        "-filter_complex_script", fg_file,
        "-map", "[vout]", "-an",
        "-c:v", "libx264", "-preset", "fast", "-crf", "16",
        "-pix_fmt", "yuv420p", "-r", "24000/1001",
        out
    ])

    if run(cmd, timeout=300):
        return out
    return None


def add_music_and_finish(assembled, music, output, prefix, letterbox_h=60, music_vol=0.40, fade_in=0.6, fade_out=1.0):
    """Add letterbox, fades, and music"""
    dur = get_duration(assembled)

    fg_file = f"{TEMP}/{prefix}_final_fg.txt"
    fg = (
        f"[0:v]drawbox=x=0:y=0:w=1920:h={letterbox_h}:color=black:t=fill,"
        f"drawbox=x=0:y={1080-letterbox_h}:w=1920:h={letterbox_h}:color=black:t=fill,"
        f"fade=t=in:st=0:d={fade_in},"
        f"fade=t=out:st={dur - fade_out:.4f}:d={fade_out}[vout];\n"
        f"[1:a]atrim=0:{dur:.4f},asetpts=PTS-STARTPTS,"
        f"afade=t=in:d={fade_in + 0.3},"
        f"afade=t=out:st={dur - fade_out - 0.5:.4f}:d={fade_out + 0.5},"
        f"volume={music_vol}[aout]"
    )

    with open(fg_file, 'w') as f:
        f.write(fg)

    cmd = [
        "ffmpeg", "-y",
        "-i", assembled, "-i", music,
        "-filter_complex_script", fg_file,
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "17",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        output
    ]

    if run(cmd, timeout=300):
        dur = get_duration(output)
        mb = os.path.getsize(output) / 1048576
        print(f"  Output: {dur:.1f}s, {mb:.1f} MB")
        return True
    return False


def add_pycaps(input_path, output_path, captions, clips, prefix):
    """Add animated captions via pycaps"""
    dur = get_duration(input_path)

    # Calculate clip timing in output
    clip_times = []
    t = 0
    for i, (start, end, speed, zoom, desc) in enumerate(clips):
        clip_dur = (end - start) / speed
        clip_times.append((t, t + clip_dur))
        t += clip_dur + FLASH_DUR

    # Create SRT
    srt = f"{TEMP}/{prefix}_captions.srt"

    # Distribute captions across clips (skip first clip usually)
    cap_assignments = []
    clip_indices = list(range(1, len(clips)))  # skip first clip
    step = max(1, len(clip_indices) // len(captions))

    for ci, cap_text in enumerate(captions):
        idx = min(clip_indices[ci * step] if ci * step < len(clip_indices) else clip_indices[-1],
                  len(clip_times) - 1)
        cs, ce = clip_times[idx]
        s = cs + 0.15
        e = ce - 0.15
        if e <= s:
            e = s + 0.8
        cap_assignments.append((s, e, cap_text))

    with open(srt, 'w') as f:
        for i, (s, e, text) in enumerate(cap_assignments):
            s = max(0, min(s, dur - 0.5))
            e = max(s + 0.5, min(e, dur - 0.2))
            sh, sm, ss_val = int(s // 3600), int((s % 3600) // 60), s % 60
            eh, em, es_val = int(e // 3600), int((e % 3600) // 60), e % 60
            f.write(f"{i + 1}\n")
            f.write(f"{sh:02d}:{sm:02d}:{ss_val:06.3f} --> {eh:02d}:{em:02d}:{es_val:06.3f}\n".replace('.', ','))
            f.write(f"{text}\n\n")

    # Run pycaps
    cmd_str = (
        f'pycaps render --input "{input_path}" --output "{output_path}" '
        f'--template hype --transcript "{srt}" --transcript-format srt '
        f'--lang en --video-quality high'
    )

    result = subprocess.run(
        cmd_str, shell=True, capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=600,
        cwd=TEMP
    )

    if result.returncode != 0:
        print(f"  pycaps failed: {result.stderr[-300:]}")
        shutil.copy2(input_path, output_path)
        print(f"  Fallback: copied without animated captions")
        return True

    mb = os.path.getsize(output_path) / 1048576
    print(f"  Captions done: {mb:.1f} MB")
    return True


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    flash = create_flash()
    if not flash:
        print("Flash creation failed!")
        sys.exit(1)

    versions = [
        ("V1_BREAKBEAT", V1_CLIPS, GRADE_ENERGY, V1_MUSIC, V1_OUTPUT, V1_CAPTIONS,
         "flash", 0.45, 0.5, 0.8),
        ("V2_CINEMATIC", V2_CLIPS, GRADE_CINEMATIC, V2_MUSIC, V2_OUTPUT, V2_CAPTIONS,
         "crossfade", 0.35, 1.0, 1.5),
        ("V3_SOUL", V3_CLIPS, GRADE_CLEAN, V3_MUSIC, V3_OUTPUT, V3_CAPTIONS,
         "crossfade", 0.38, 0.8, 1.2),
    ]

    for name, clips, grade, music, output, captions, transition_type, vol, fi, fo in versions:
        print(f"\n{'=' * 55}")
        print(f"  {name}")
        print(f"{'=' * 55}")

        # Step 1: Process clips
        prefix = name.lower()
        print(f"\n  [1/4] Processing {len(clips)} clips...")
        clip_files = process_clips(clips, grade, prefix)
        if not clip_files:
            print(f"  {name} FAILED at clip processing")
            continue

        # Step 2: Assemble
        print(f"\n  [2/4] Assembling...")
        if transition_type == "flash":
            assembled = assemble_with_flash(clip_files, flash, prefix)
        else:
            assembled = assemble_with_crossfade(clip_files, prefix, fade_dur=0.4)

        if not assembled:
            print(f"  {name} FAILED at assembly")
            continue

        dur = get_duration(assembled)
        print(f"  Assembled: {dur:.1f}s")

        # Step 3: Add music + letterbox + fades
        base_output = f"{TEMP}/{prefix}_base.mp4"
        print(f"\n  [3/4] Adding music + finishing...")
        if not add_music_and_finish(assembled, music, base_output, prefix,
                                     letterbox_h=55, music_vol=vol,
                                     fade_in=fi, fade_out=fo):
            print(f"  {name} FAILED at music stage")
            continue

        # Step 4: Add pycaps captions
        print(f"\n  [4/4] Adding animated captions...")
        if add_pycaps(base_output, output, captions, clips, prefix):
            final_dur = get_duration(output)
            final_mb = os.path.getsize(output) / 1048576
            print(f"\n  {name} DONE: {final_dur:.1f}s | {final_mb:.1f} MB")
            print(f"  -> {output}")
        else:
            print(f"  {name} FAILED at captions")

    print(f"\n{'=' * 55}")
    print(f"  ALL VERSIONS COMPLETE")
    print(f"{'=' * 55}")
    for _, _, _, _, output, _, _, _, _, _ in versions:
        if os.path.exists(output):
            d = get_duration(output)
            m = os.path.getsize(output) / 1048576
            print(f"  {os.path.basename(output)}: {d:.1f}s | {m:.1f} MB")
    print(f"  Folder: {OUTPUT_DIR}")
