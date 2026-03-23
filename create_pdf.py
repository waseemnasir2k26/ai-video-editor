#!/usr/bin/env python3
"""
Generate a professional lead magnet PDF:
"AI Video Editing with Claude Code - The Complete Beginner's Guide"
"""
from fpdf import FPDF
import os

OUTPUT_DIR = "C:/Users/info/OneDrive/Desktop/business meeting"
OUTPUT_PDF = f"{OUTPUT_DIR}/AI_Video_Editing_Guide.pdf"
TEMP = "C:/Users/info/OneDrive/Desktop/video_edit_temp"


class GuidePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "AI Video Editing with Claude Code  |  The Complete Guide", align="C")
            self.ln(4)
            # Thin line
            self.set_draw_color(200, 200, 200)
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(6)

    def footer(self):
        self.set_y(-20)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(140, 140, 140)
        if self.page_no() > 1:
            self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def cover_page(self):
        self.add_page()
        self.ln(40)
        # Title background block
        self.set_fill_color(18, 18, 24)
        self.rect(0, 50, 210, 90, "F")

        self.set_y(58)
        self.set_font("Helvetica", "B", 32)
        self.set_text_color(255, 255, 255)
        self.cell(0, 14, "AI VIDEO EDITING", align="C")
        self.ln(14)
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(0, 180, 255)
        self.cell(0, 12, "WITH CLAUDE CODE", align="C")
        self.ln(16)
        self.set_font("Helvetica", "", 13)
        self.set_text_color(200, 200, 200)
        self.cell(0, 8, "The Complete Beginner's Guide to Professional Video Editing Using AI", align="C")

        # Author block
        self.set_y(160)
        self.set_text_color(60, 60, 60)
        self.set_font("Helvetica", "", 12)
        self.cell(0, 8, "From raw footage to 4 professional edits", align="C")
        self.ln(6)
        self.cell(0, 8, "using nothing but prompts + Python + FFmpeg", align="C")

        self.ln(25)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(40, 40, 40)
        self.cell(0, 8, "WHAT YOU'LL LEARN:", align="C")
        self.ln(10)

        items = [
            "Exact prompts to give Claude Code for video editing",
            "FFmpeg filters: color grading, zoom punches, speed ramping",
            "4 distinct editing styles broken down step-by-step",
            "How to add royalty-free music and animated captions",
            "Professional techniques used by content creators",
        ]
        self.set_font("Helvetica", "", 10)
        self.set_text_color(70, 70, 70)
        for item in items:
            self.cell(55)
            self.cell(0, 7, f"  {item}")
            self.ln(7)

        # Bottom
        self.set_y(260)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(150, 150, 150)
        self.cell(0, 6, "by Waseem Nasir  |  skynetjoe.com", align="C")

    def section_title(self, num, title):
        self.ln(4)
        self.set_fill_color(18, 18, 24)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 12, f"  {num}. {title}", fill=True)
        self.ln(10)
        self.set_text_color(30, 30, 30)

    def sub_title(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(0, 120, 200)
        self.cell(0, 8, title)
        self.ln(8)
        self.set_text_color(30, 30, 30)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def body_bold(self, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def code_block(self, code):
        self.set_font("Courier", "", 8.5)
        self.set_fill_color(240, 240, 245)
        self.set_text_color(30, 30, 30)
        # Add padding
        x = self.get_x()
        self.set_x(x + 5)
        for line in code.strip().split("\n"):
            if self.get_y() > 265:
                self.add_page()
                self.set_font("Courier", "", 8.5)
                self.set_fill_color(240, 240, 245)
                self.set_text_color(30, 30, 30)
            self.cell(170, 5.5, f"  {line}", fill=True)
            self.ln(5.5)
        self.ln(4)
        self.set_x(x)

    def prompt_box(self, prompt_text):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(0, 50, 80)
        self.set_text_color(255, 255, 255)
        self.cell(170, 7, "  PROMPT TO CLAUDE CODE:", fill=True)
        self.ln(7)
        self.set_font("Helvetica", "I", 9.5)
        self.set_fill_color(230, 242, 255)
        self.set_text_color(0, 50, 100)
        self.set_x(self.get_x() + 5)
        self.multi_cell(165, 6, f'"{prompt_text}"', fill=True)
        self.ln(4)
        self.set_text_color(30, 30, 30)

    def tip_box(self, text):
        self.set_fill_color(255, 248, 220)
        self.set_draw_color(220, 180, 50)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(120, 90, 0)
        x = self.get_x()
        self.set_x(x + 5)
        self.cell(165, 7, "  PRO TIP", fill=True, border="L")
        self.ln(7)
        self.set_font("Helvetica", "", 9)
        self.set_x(x + 5)
        self.multi_cell(165, 5.5, f"  {text}", fill=True, border="L")
        self.ln(4)
        self.set_text_color(30, 30, 30)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        x = self.get_x()
        self.set_x(x + 8)
        self.cell(4, 6, "-")
        self.multi_cell(155, 6, text)
        self.ln(1)

    def numbered(self, num, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 120, 200)
        x = self.get_x()
        self.set_x(x + 5)
        self.cell(8, 6, f"{num}.")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(155, 6, text)
        self.ln(1)

    def divider(self):
        self.ln(3)
        self.set_draw_color(200, 200, 200)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(5)


def build_pdf():
    pdf = GuidePDF()

    # ============================================================
    # COVER PAGE
    # ============================================================
    pdf.cover_page()

    # ============================================================
    # TABLE OF CONTENTS
    # ============================================================
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(18, 18, 24)
    pdf.cell(0, 12, "TABLE OF CONTENTS")
    pdf.ln(16)

    toc = [
        ("1", "Introduction - Why AI Video Editing?"),
        ("2", "Tools You'll Need (Free Setup)"),
        ("3", "The Workflow Overview"),
        ("4", "Step 1: Analyze Your Raw Footage"),
        ("5", "Step 2: Define Your Edit Style"),
        ("6", "Step 3: Color Grading with FFmpeg"),
        ("7", "Step 4: Zoom Punches & Speed Ramping"),
        ("8", "Step 5: Transitions (Flash Cuts & Crossfades)"),
        ("9", "Step 6: Royalty-Free Music"),
        ("10", "Step 7: Animated Captions with pycaps"),
        ("11", "The 4 Edit Styles Breakdown"),
        ("12", "All Prompts Used (Copy & Paste Ready)"),
        ("13", "The Complete Python Scripts"),
        ("14", "Pro Tips & Common Mistakes"),
        ("15", "Next Steps & Resources"),
    ]
    for num, title in toc:
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(70, 70, 70)
        pdf.cell(10, 8, num + ".")
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 8, title)
        pdf.ln(8)

    # ============================================================
    # SECTION 1: INTRODUCTION
    # ============================================================
    pdf.add_page()
    pdf.section_title("1", "INTRODUCTION - WHY AI VIDEO EDITING?")

    pdf.body(
        "What if you could turn raw footage into multiple professional-looking edits "
        "without touching a single video editor? No Premiere Pro. No DaVinci Resolve. "
        "No After Effects. Just your terminal, a few prompts, and AI."
    )
    pdf.body(
        "This guide documents the exact process I used to take a 49-second raw clip of "
        "a business meeting and produce 4 completely different professional edits - each "
        "with unique color grading, zoom punches, speed ramping, transitions, royalty-free "
        "music, and animated captions."
    )
    pdf.body(
        "The entire process was done using Claude Code (Anthropic's AI coding assistant) "
        "writing Python scripts that control FFmpeg, the industry-standard open-source "
        "video processing tool."
    )

    pdf.sub_title("What We Built")
    pdf.bullet("V1: Breakbeat Energy - Fast cuts, zoom punches, flash transitions, breakbeat music (25s)")
    pdf.bullet("V2: Cinematic Epic - Dramatic slow-mo, smooth crossfades, orchestral music (38s)")
    pdf.bullet("V3: Clean Soul - Smooth flow, gentle zooms, soul music (28s)")
    pdf.bullet("V4: Original Energy Edit - Hip-hop, aggressive cuts, dramatic speed ramps (25s)")

    pdf.sub_title("Who This Is For")
    pdf.bullet("Content creators who want fast, repeatable video editing workflows")
    pdf.bullet("Developers curious about AI-assisted creative work")
    pdf.bullet("Anyone who wants professional video output without learning complex software")
    pdf.bullet("Marketers who need multiple video variants for A/B testing")

    # ============================================================
    # SECTION 2: TOOLS
    # ============================================================
    pdf.add_page()
    pdf.section_title("2", "TOOLS YOU'LL NEED (FREE SETUP)")

    pdf.body("Everything used in this workflow is free or open-source:")
    pdf.ln(2)

    tools = [
        ("Claude Code", "Anthropic's AI coding CLI. This is the brain - you give it prompts, it writes the scripts. Install: npm install -g @anthropic-ai/claude-code"),
        ("FFmpeg", "The Swiss Army knife of video processing. Handles cutting, color grading, transitions, zoom, speed changes, music mixing - everything. Install: ffmpeg.org/download.html"),
        ("Python 3", "Runs the editing scripts that Claude Code generates. Any version 3.8+ works. Install: python.org"),
        ("pycaps", "Open-source tool for animated word-by-word captions (TikTok/Reels style). Install: pip install pycaps"),
        ("FFprobe", "Comes with FFmpeg. Used to analyze video properties (duration, resolution, codec info)."),
    ]

    for name, desc in tools:
        pdf.body_bold(name)
        pdf.body(desc)
        pdf.ln(1)

    pdf.tip_box("You don't need to know how any of these tools work. Claude Code will write all the commands for you. You just need them installed on your system.")

    # ============================================================
    # SECTION 3: WORKFLOW OVERVIEW
    # ============================================================
    pdf.add_page()
    pdf.section_title("3", "THE WORKFLOW OVERVIEW")

    pdf.body("Here's the high-level process from raw footage to finished edit:")
    pdf.ln(2)

    steps = [
        "ANALYZE - Give Claude Code your raw video file. It analyzes resolution, duration, framerate, and content.",
        "DEFINE STYLE - Tell Claude what vibe you want (energetic, cinematic, clean, etc). Be specific about mood and pacing.",
        "CLIP SELECTION - Claude picks the best moments from your footage and defines start/end times for each clip.",
        "COLOR GRADE - FFmpeg filters adjust brightness, contrast, saturation, color balance, and sharpness.",
        "ZOOM & SPEED - Each clip gets its own zoom level (crop + upscale) and speed (slow-mo or fast-forward).",
        "TRANSITIONS - Clips are joined with flash cuts, crossfades, or other FFmpeg transitions.",
        "MUSIC - Royalty-free music is mixed in with proper fade-in/fade-out and volume balancing.",
        "CAPTIONS - Animated word-by-word captions are rendered on top using pycaps.",
        "OUTPUT - Final MP4 with H.264 encoding, AAC audio, optimized for social media upload.",
    ]

    for i, step in enumerate(steps, 1):
        pdf.numbered(i, step)

    pdf.ln(3)
    pdf.tip_box("The entire pipeline runs in under 3 minutes on a modern laptop. Each version is generated by a single Python script that Claude Code writes for you.")

    # ============================================================
    # SECTION 4: ANALYZE FOOTAGE
    # ============================================================
    pdf.add_page()
    pdf.section_title("4", "STEP 1: ANALYZE YOUR RAW FOOTAGE")

    pdf.body(
        "Before any editing, you need to understand what you're working with. "
        "Give Claude Code your video file path and ask it to analyze the footage."
    )

    pdf.prompt_box(
        "Here's my video file: C:/path/to/your/video.mp4 - Analyze it and tell me "
        "the resolution, duration, framerate, codec, and describe what you see in the footage. "
        "I want to turn this into a professional short-form edit."
    )

    pdf.body("Claude Code will run FFprobe to extract technical details:")

    pdf.code_block(
        'ffprobe -v quiet -show_entries format=duration,size \\\n'
        '  -show_entries stream=width,height,r_frame_rate,codec_name \\\n'
        '  -of json "your_video.mp4"'
    )

    pdf.body("For our project, the analysis revealed:")
    pdf.bullet("Resolution: 1920x1080 (Full HD)")
    pdf.bullet("Duration: 49 seconds")
    pdf.bullet("Framerate: 24fps (23.976)")
    pdf.bullet("Codec: H.264")
    pdf.bullet("Content: Two people at a cafe/lounge discussing over laptops")

    pdf.sub_title("Why This Matters")
    pdf.body(
        "Knowing the resolution tells us how much we can zoom (crop) before losing quality. "
        "At 1920x1080, we can do a 1.5x-1.8x zoom and still have a sharp image. The framerate "
        "(24fps) determines our flash cut duration and slow-motion limits."
    )

    # ============================================================
    # SECTION 5: EDIT STYLE
    # ============================================================
    pdf.add_page()
    pdf.section_title("5", "STEP 2: DEFINE YOUR EDIT STYLE")

    pdf.body(
        "This is the most important step. The style you choose determines every technical "
        "decision that follows - clip selection, speed, color grade, music choice, and transitions."
    )

    pdf.sub_title("The 4 Styles We Created")

    styles = [
        ("ENERGY / BREAKBEAT",
         "Fast cuts (1-2 seconds each), aggressive zoom punches, white flash transitions, "
         "high-tempo music. Speed varies between 0.5x (slow-mo for impact) and 1.5x (fast for energy). "
         "10+ clips. Best for: motivational content, hustle culture, TikTok/Reels."),
        ("CINEMATIC EPIC",
         "Longer clips (4-8 seconds), heavy slow-motion (0.5x-0.85x), smooth crossfade transitions, "
         "orchestral/epic music. Fewer cuts, more dramatic. 7 clips. "
         "Best for: brand films, dramatic storytelling, YouTube intros."),
        ("CLEAN SOUL",
         "Medium clips (3-5 seconds), gentle zooms (1.0x-1.3x), smooth crossfades, "
         "soul/lo-fi music. Natural feel, not over-edited. 7 clips. "
         "Best for: lifestyle content, behind-the-scenes, authentic branding."),
        ("HIP-HOP ENERGY (Original V3)",
         "Mixed speed ramping, tight crop zooms, white flash cuts, hip-hop track. "
         "Aggressive color grade. 8 clips. "
         "Best for: high-energy social content, promo videos, attention-grabbing ads."),
    ]

    for name, desc in styles:
        pdf.body_bold(name)
        pdf.body(desc)
        pdf.divider()

    pdf.prompt_box(
        "I want 3 different versions of this edit: one with breakbeat energy and fast cuts, "
        "one cinematic with dramatic slow-mo and epic music, and one clean/smooth with soul music. "
        "Don't darken the video too much - keep it bright and natural."
    )

    pdf.tip_box("Be specific about what you DON'T want. Saying 'don't darken the video' saved us from over-processing. AI tends to go heavy on color grading - tell it to keep things natural.")

    # ============================================================
    # SECTION 6: COLOR GRADING
    # ============================================================
    pdf.add_page()
    pdf.section_title("6", "STEP 3: COLOR GRADING WITH FFMPEG")

    pdf.body(
        "Color grading transforms the look and feel of your video. FFmpeg's eq, colorbalance, "
        "and unsharp filters give you full control. Here are the 3 grades we used:"
    )

    pdf.sub_title("Bright Energy Grade")
    pdf.code_block(
        "eq=brightness=0.06:contrast=1.15:saturation=0.90,\n"
        "colorbalance=rs=0.06:gs=0.02:bs=-0.04:rm=0.04:gm=0.01:bm=-0.02,\n"
        "unsharp=5:5:0.5"
    )
    pdf.body("Slightly boosted brightness, punchy contrast, slightly desaturated for that 'film' look. Warm tones pushed via red/green highlights. Strong sharpening for crisp detail.")

    pdf.sub_title("Cinematic Warm Grade")
    pdf.code_block(
        "eq=brightness=0.04:contrast=1.10:saturation=0.82,\n"
        "colorbalance=rs=0.08:gs=0.03:bs=-0.03:rm=0.05:gm=0.02:bm=-0.02,\n"
        "unsharp=3:3:0.4"
    )
    pdf.body("More desaturated for a filmic look. Warmer color balance. Moderate sharpening. This gives that Hollywood 'orange and teal' vibe.")

    pdf.sub_title("Clean Natural Grade")
    pdf.code_block(
        "eq=brightness=0.05:contrast=1.08:saturation=0.95,\n"
        "colorbalance=rs=0.04:gs=0.02:bs=-0.02:rm=0.03:gm=0.01:bm=-0.01,\n"
        "unsharp=3:3:0.3"
    )
    pdf.body("Minimal processing. Slight brightness boost, near-original saturation. Subtle warmth. Light sharpening. The video looks enhanced but still natural.")

    pdf.sub_title("What Each Parameter Does")
    pdf.bullet("brightness: -1.0 to 1.0 (0 = no change, 0.05 = slightly brighter)")
    pdf.bullet("contrast: 0.0 to 2.0 (1.0 = no change, 1.15 = punchy)")
    pdf.bullet("saturation: 0.0 to 2.0 (1.0 = normal, 0.8 = desaturated/filmic)")
    pdf.bullet("colorbalance rs/gs/bs: Shadow color shift (positive red = warm shadows)")
    pdf.bullet("colorbalance rm/gm/bm: Midtone color shift (where skin tones live)")
    pdf.bullet("unsharp: width:height:strength (5:5:0.5 = strong sharpening)")

    pdf.tip_box("AVOID going below brightness=-0.02 or above contrast=1.3 - it will crush your blacks and make the video look dark and muddy. Keep it bright and natural unless you specifically want a dark mood.")

    # ============================================================
    # SECTION 7: ZOOM & SPEED
    # ============================================================
    pdf.add_page()
    pdf.section_title("7", "STEP 4: ZOOM PUNCHES & SPEED RAMPING")

    pdf.sub_title("Zoom Punches (Crop + Scale)")
    pdf.body(
        "A 'zoom punch' simulates a camera cut to a tighter shot. In FFmpeg, we crop a portion "
        "of the frame and scale it back to full resolution. This creates the illusion of multiple "
        "camera angles from a single wide shot."
    )

    pdf.code_block(
        "# Crop 1067x600 pixels starting at position (46, 80)\n"
        "# Then scale back up to 1920x1080\n"
        "crop=1067:600:46:80,scale=1920:1080:flags=lanczos"
    )

    pdf.body("The crop parameters are: crop=WIDTH:HEIGHT:X_POSITION:Y_POSITION")
    pdf.bullet("WIDTH:HEIGHT - Size of the crop area (smaller = more zoomed in)")
    pdf.bullet("X:Y - Top-left corner of the crop (use this to target a specific person)")
    pdf.bullet("lanczos - High-quality scaling algorithm for sharp upscaling")
    pdf.ln(2)

    pdf.body_bold("Zoom levels we used:")
    pdf.bullet("No zoom: Full 1920x1080 frame (wide establishing shots)")
    pdf.bullet("1.3x zoom: crop=1477:831 (medium shot, both people visible)")
    pdf.bullet("1.5x zoom: crop=1280:720 (medium-tight, one person focused)")
    pdf.bullet("1.8x zoom: crop=1067:600 (tight close-up on one person)")

    pdf.sub_title("Speed Ramping")
    pdf.body(
        "Speed ramping means different clips play at different speeds. "
        "This creates rhythm - fast for energy, slow for dramatic moments."
    )

    pdf.code_block(
        "# Slow motion (0.5x = half speed, twice as long)\n"
        "setpts=PTS/0.5\n\n"
        "# Fast motion (1.5x = 50% faster)\n"
        "setpts=PTS/1.5\n\n"
        "# Normal speed\n"
        "setpts=PTS/1.0"
    )

    pdf.body_bold("Speed choices by style:")
    pdf.bullet("Energy: 0.50x - 0.65x for dramatic moments, 1.2x - 1.5x for fast energy")
    pdf.bullet("Cinematic: 0.50x - 0.85x throughout (everything feels grand and slow)")
    pdf.bullet("Clean: 0.70x - 1.0x (subtle slow-motion, mostly natural speed)")

    pdf.tip_box("The magic is in the CONTRAST between speeds. A fast clip followed immediately by a slow-mo clip creates a powerful visual rhythm. This is what professional editors call 'speed ramping'.")

    # ============================================================
    # SECTION 8: TRANSITIONS
    # ============================================================
    pdf.add_page()
    pdf.section_title("8", "STEP 5: TRANSITIONS")

    pdf.sub_title("White Flash Cuts")
    pdf.body(
        "A white flash between clips creates a high-energy 'punch' feel. We generate a "
        "tiny white frame (2 frames / 0.083 seconds) and insert it between every clip."
    )

    pdf.code_block(
        "# Generate a white flash frame\n"
        'ffmpeg -y -f lavfi -i \\\n'
        '  "color=white:s=1920x1080:d=0.083:r=24000/1001" \\\n'
        '  -c:v libx264 flash.mp4\n\n'
        "# Concatenate: clip1 + flash + clip2 + flash + clip3...\n"
        "# Using FFmpeg concat demuxer with a text file:\n"
        "file 'clip_00.mp4'\n"
        "file 'flash.mp4'\n"
        "file 'clip_01.mp4'\n"
        "file 'flash.mp4'\n"
        "file 'clip_02.mp4'"
    )

    pdf.sub_title("Crossfade Transitions")
    pdf.body(
        "For smoother, more cinematic transitions, FFmpeg's xfade filter blends "
        "two clips together over a specified duration."
    )

    pdf.code_block(
        "# Crossfade between clips (0.4 second overlap)\n"
        "[0:v][1:v]xfade=transition=fade:duration=0.4:offset=3.5[x1];\n"
        "[x1][2:v]xfade=transition=smoothleft:duration=0.4:offset=6.8[x2];\n"
        "[x2][3:v]xfade=transition=dissolve:duration=0.4:offset=10.1[vout]"
    )

    pdf.body_bold("Available transition types:")
    pdf.bullet("fade - Simple opacity crossfade (safest, always looks good)")
    pdf.bullet("fadeblack - Fade through black (dramatic)")
    pdf.bullet("fadewhite - Fade through white (bright, energetic)")
    pdf.bullet("smoothleft/smoothright - Directional slide blend")
    pdf.bullet("dissolve - Gradual pixel dissolve")
    pdf.bullet("wiperight/wipeleft - Hard wipe (retro, bold)")

    pdf.sub_title("When to Use Which")
    pdf.bullet("Flash cuts: High-energy edits, music videos, motivational content")
    pdf.bullet("Crossfades: Cinematic edits, brand films, storytelling")
    pdf.bullet("Mix of both: Use flash for beat-synced moments, crossfade for everything else")

    # ============================================================
    # SECTION 9: MUSIC
    # ============================================================
    pdf.add_page()
    pdf.section_title("9", "STEP 6: ROYALTY-FREE MUSIC")

    pdf.body(
        "Music is 50% of the emotional impact. Choose the wrong track and your edit falls flat. "
        "Here's where to find royalty-free music and how to mix it properly."
    )

    pdf.sub_title("Where to Find Royalty-Free Music")
    pdf.bullet("Mixkit.co - Completely free, no attribution required, high quality")
    pdf.bullet("Pixabay Music - Free, large library, various genres")
    pdf.bullet("YouTube Audio Library - Free for YouTube content")
    pdf.bullet("Epidemic Sound - Paid but premium quality (used by top creators)")
    pdf.bullet("Artlist - Paid, unlimited downloads with one license")

    pdf.sub_title("Tracks We Used")
    pdf.bullet("Breakbeat: 'No Warning' (Mixkit) - High-energy breakbeat, perfect for fast edits")
    pdf.bullet("Epic: 'Life's a Movie' (Mixkit) - Orchestral film score, dramatic and sweeping")
    pdf.bullet("Soul: 'Feel Alive' (Mixkit) - Smooth soul track, warm and authentic")
    pdf.bullet("Hip-Hop: 'Daylight Robbery' (Mixkit) - Hard-hitting hip-hop beat")

    pdf.sub_title("Audio Mixing with FFmpeg")
    pdf.code_block(
        "# Trim music to video duration, add fades, set volume\n"
        "[1:a]atrim=0:25.5,        # Trim to 25.5 seconds\n"
        "asetpts=PTS-STARTPTS,      # Reset timestamps\n"
        "afade=t=in:d=0.8,          # Fade in over 0.8s\n"
        "afade=t=out:st=24.5:d=1.0, # Fade out last 1.0s\n"
        "volume=0.40[aout]          # 40% volume (background level)"
    )

    pdf.body_bold("Volume guidelines:")
    pdf.bullet("0.30 - 0.35: Subtle background (if you have voiceover/dialogue)")
    pdf.bullet("0.38 - 0.45: Medium presence (our sweet spot for no-dialogue edits)")
    pdf.bullet("0.50+: Dominant (music video feel)")

    pdf.tip_box("Always remove the original audio first (-an flag when processing clips) and add music separately. This gives you clean control over the audio mix. The original audio from raw footage is almost never usable.")

    # ============================================================
    # SECTION 10: CAPTIONS
    # ============================================================
    pdf.add_page()
    pdf.section_title("10", "STEP 7: ANIMATED CAPTIONS WITH PYCAPS")

    pdf.body(
        "pycaps is an open-source Python tool that adds TikTok/Reels-style animated "
        "word-by-word captions to your video. Each word pops in with animation, making "
        "your captions feel dynamic and engaging."
    )

    pdf.sub_title("Install pycaps")
    pdf.code_block("pip install pycaps")

    pdf.sub_title("Create Your SRT File")
    pdf.body("SRT (SubRip) is the standard caption format. Each entry has an index, timestamp, and text:")

    pdf.code_block(
        "1\n"
        "00:00:02,150 --> 00:00:05,000\n"
        "every empire starts here\n"
        "\n"
        "2\n"
        "00:00:06,200 --> 00:00:09,000\n"
        "deep in the zone\n"
        "\n"
        "3\n"
        "00:00:11,000 --> 00:00:14,500\n"
        "while they sleep we grind"
    )

    pdf.sub_title("Render Captions")
    pdf.code_block(
        'pycaps render \\\n'
        '  --input "base_video.mp4" \\\n'
        '  --output "final_with_captions.mp4" \\\n'
        '  --template hype \\\n'
        '  --transcript "captions.srt" \\\n'
        '  --transcript-format srt \\\n'
        '  --lang en \\\n'
        '  --video-quality high'
    )

    pdf.body_bold("Available pycaps templates:")
    pdf.bullet("hype - Bold, animated pop-in (best for energy/motivational content)")
    pdf.bullet("gentle - Smooth fade-in (good for cinematic)")
    pdf.bullet("default - Clean standard captions")

    pdf.sub_title("Writing Good Captions")
    pdf.bullet("Keep each line to 3-5 words maximum (pycaps animates word by word)")
    pdf.bullet("Use lowercase for a modern, casual feel")
    pdf.bullet("Time captions to match your clip cuts (not random)")
    pdf.bullet("Leave the first clip caption-free (let the visual breathe)")
    pdf.bullet("Use motivational/aspirational language for business content")

    pdf.body_bold("Caption examples we used:")
    captions = [
        '"every empire starts here"',
        '"deep in the zone"',
        '"execute relentlessly"',
        '"while they sleep we grind"',
        '"from vision to reality"',
        '"never stop building"',
    ]
    for c in captions:
        pdf.bullet(c)

    # ============================================================
    # SECTION 11: 4 EDIT STYLES BREAKDOWN
    # ============================================================
    pdf.add_page()
    pdf.section_title("11", "THE 4 EDIT STYLES BREAKDOWN")

    pdf.sub_title("Style 1: Breakbeat Energy (25.5 seconds)")
    pdf.body_bold("Clip Structure (10 clips):")
    v1_clips = [
        "0:00-0:02 | Wide opening | 1.2x speed | No zoom",
        "0:03-0:05 | Writing close-up | 0.65x slow-mo | 1.8x zoom left person",
        "0:07-0:09 | Wide quick | 1.5x fast | No zoom",
        "0:10-0:12 | Right person | 1.0x normal | 1.6x zoom right",
        "0:14-0:16 | Medium pointing | 1.5x fast | 1.3x zoom",
        "0:18-0:20 | Wide discussion | 1.3x fast | No zoom",
        "0:22-0:24 | Dramatic pointing | 0.50x slow-mo | 1.8x zoom",
        "0:28-0:30 | Right typing | 1.4x fast | 1.6x zoom",
        "0:32-0:34 | Wide pitch | 1.3x fast | No zoom",
        "0:36-0:39 | Slow finale | 0.55x slow-mo | 1.3x zoom",
    ]
    for c in v1_clips:
        pdf.bullet(c)

    pdf.body("Music: Breakbeat | Transitions: White flash cuts | Volume: 45%")

    pdf.divider()

    pdf.sub_title("Style 2: Cinematic Epic (37.9 seconds)")
    pdf.body_bold("Clip Structure (7 clips):")
    v2_clips = [
        "0:00-0:03 | Wide opening | 0.85x slow | No zoom",
        "0:04-0:07 | Extreme slow-mo writing | 0.55x | 1.8x zoom",
        "0:10-0:14 | Wide both working | 1.0x normal | No zoom",
        "0:16-0:19 | Slow zoom right | 0.60x | 1.6x zoom",
        "0:22-0:26 | Dramatic slow-mo | 0.50x | 1.8x zoom",
        "0:30-0:34 | Wide pitch | 0.80x slow | No zoom",
        "0:36-0:40 | Epic slow finale | 0.50x | 1.3x zoom",
    ]
    for c in v2_clips:
        pdf.bullet(c)
    pdf.body("Music: Epic orchestral | Transitions: Smooth crossfades | Volume: 35%")

    pdf.divider()

    pdf.sub_title("Style 3: Clean Soul (27.9 seconds)")
    pdf.body_bold("Clip Structure (7 clips):")
    v3_clips = [
        "0:00-0:04 | Wide natural opening | 1.0x | No zoom",
        "0:05-0:08 | Gentle zoom left | 0.80x | 1.5x zoom",
        "0:10-0:14 | Wide laptops | 1.0x | No zoom",
        "0:15-0:18 | Gentle zoom right | 0.85x | 1.5x zoom",
        "0:22-0:26 | Medium both | 0.75x | 1.3x zoom",
        "0:30-0:34 | Wide discussion | 1.0x | No zoom",
        "0:36-0:40 | Smooth finale | 0.70x | 1.5x zoom",
    ]
    for c in v3_clips:
        pdf.bullet(c)
    pdf.body("Music: Soul | Transitions: Smooth crossfades | Volume: 38%")

    # ============================================================
    # SECTION 12: ALL PROMPTS
    # ============================================================
    pdf.add_page()
    pdf.section_title("12", "ALL PROMPTS USED (COPY & PASTE READY)")

    pdf.body(
        "Here are the exact prompts I gave Claude Code, in order. You can copy and paste "
        "these into your own Claude Code session. Just replace the file paths with your own."
    )

    prompts = [
        ("Prompt 1: Initial Analysis",
         "Here's my video file: [PATH] - Let me know how you can improve this video. "
         "Add some amazing transitions. Add some music that is royalty-free so I don't get any copyright. "
         "Remove the audio, just the music, slight music, and add some captions with amazing design, "
         "like we are having a business meeting or working on something cool."),

        ("Prompt 2: Style Change",
         "I don't like the music. Can you do something more, like motivational-type music? "
         "Royalty-free. Increase the speed and try to cover the video under 30 seconds."),

        ("Prompt 3: Energy Feedback",
         "I don't like these - NO PASSION or ENERGY in your EDITING. "
         "Make it hit harder with zoom punches, speed ramping, flash cuts."),

        ("Prompt 4: Multiple Versions + Brightness",
         "Give me 3 more versions but don't dark the video, it's already too much darker. "
         "I want one with breakbeat energy and fast cuts, one cinematic with dramatic slow-mo "
         "and epic music, and one clean/smooth with soul music."),

        ("Prompt 5: Lead Magnet PDF",
         "Give me a PDF that will include all the prompts, all the procedure summary "
         "for any beginner. I want to pitch that PDF as a lead magnet."),
    ]

    for title, prompt in prompts:
        pdf.sub_title(title)
        pdf.prompt_box(prompt)

    pdf.tip_box(
        "Notice how the prompts got more specific over iterations. The first prompt was broad - "
        "'add amazing transitions and music.' The later prompts were precise - "
        "'zoom punches, speed ramping, flash cuts, don't darken.' "
        "Being specific gets better results from AI. Iterate and give honest feedback."
    )

    # ============================================================
    # SECTION 13: COMPLETE SCRIPTS
    # ============================================================
    pdf.add_page()
    pdf.section_title("13", "THE COMPLETE PYTHON SCRIPTS")

    pdf.body(
        "Below is the core architecture of the editing pipeline. Claude Code generated "
        "these scripts automatically from the prompts above. The full scripts are included "
        "alongside this PDF."
    )

    pdf.sub_title("Script Architecture")

    pdf.code_block(
        "three_versions.py (Main orchestrator)\n"
        "|\n"
        "|-- process_clips()     # Extract clips with zoom + speed + color grade\n"
        "|   |-- FFmpeg: trim, setpts, crop, scale, eq, colorbalance, unsharp\n"
        "|\n"
        "|-- create_flash()      # Generate white flash frame\n"
        "|   |-- FFmpeg: lavfi color source\n"
        "|\n"
        "|-- assemble_with_flash()      # Join clips with flash cuts\n"
        "|   |-- FFmpeg: concat demuxer\n"
        "|\n"
        "|-- assemble_with_crossfade()  # Join clips with xfade transitions\n"
        "|   |-- FFmpeg: xfade filter chain\n"
        "|\n"
        "|-- add_music_and_finish()     # Mix music, add letterbox, fades\n"
        "|   |-- FFmpeg: filter_complex_script\n"
        "|\n"
        "|-- add_pycaps()        # Animated captions\n"
        "    |-- Generate SRT from clip timing\n"
        "    |-- pycaps render with hype template"
    )

    pdf.sub_title("Key FFmpeg Command Pattern")
    pdf.code_block(
        "# Single clip processing command:\n"
        "ffmpeg -y -i input.mp4 \\\n"
        "  -vf \"trim=start=3:end=5.5,  \\\n"
        "       setpts=PTS-STARTPTS,     \\\n"
        "       setpts=PTS/0.65,         \\\n"
        "       crop=1067:600:46:80,     \\\n"
        "       scale=1920:1080:flags=lanczos, \\\n"
        "       eq=brightness=0.06:contrast=1.15:saturation=0.90, \\\n"
        "       colorbalance=rs=0.06:gs=0.02:bs=-0.04, \\\n"
        "       unsharp=5:5:0.5\"         \\\n"
        "  -an -c:v libx264 -preset fast -crf 16 \\\n"
        "  -pix_fmt yuv420p -r 24000/1001 \\\n"
        "  clip_output.mp4"
    )

    pdf.body(
        "Each clip goes through this pipeline: trim the segment from the source, reset timestamps, "
        "apply speed change, crop for zoom, scale back to 1080p, color grade, and encode as H.264."
    )

    pdf.sub_title("Final Assembly + Music Command")
    pdf.code_block(
        "# Combine assembled video with music:\n"
        "ffmpeg -y \\\n"
        "  -i assembled.mp4 -i music.mp3 \\\n"
        "  -filter_complex_script final_fg.txt \\\n"
        "  -map [vout] -map [aout] \\\n"
        "  -c:v libx264 -preset medium -crf 17 \\\n"
        "  -c:a aac -b:a 192k \\\n"
        "  -pix_fmt yuv420p -movflags +faststart \\\n"
        "  output.mp4"
    )

    pdf.tip_box("On Windows, always use -filter_complex_script (write filtergraph to a text file) instead of -filter_complex (inline). Windows command line has escaping issues with FFmpeg's complex filter syntax.")

    # ============================================================
    # SECTION 14: PRO TIPS
    # ============================================================
    pdf.add_page()
    pdf.section_title("14", "PRO TIPS & COMMON MISTAKES")

    tips = [
        ("Don't over-darken your footage",
         "It's tempting to crush the blacks for a 'cinematic' look, but it often just makes "
         "the video look muddy. Keep brightness above 0.0 and contrast below 1.2 unless you "
         "have a specific reason to go darker."),

        ("Speed contrast is everything",
         "A fast clip (1.5x) immediately followed by a slow-mo clip (0.5x) creates a powerful "
         "visual punch. This is what separates amateur edits from professional ones. "
         "Uniform speed throughout = boring."),

        ("Don't zoom everything",
         "Alternate between wide shots and zoomed shots. If every clip is zoomed in, "
         "the viewer loses spatial context. Wide shots establish the scene, zooms create intimacy."),

        ("Music sets the ceiling",
         "Your edit can only be as good as your music choice. Spend time finding the right track. "
         "The tempo of the music should match your cut rhythm. Cuts on the beat feel intentional."),

        ("Less is more with captions",
         "3-5 words per caption line. No full sentences. Let the visuals do the talking. "
         "Captions should enhance, not distract."),

        ("Iterate with honest feedback",
         "Don't settle for the first version. Tell Claude Code exactly what you don't like. "
         "'I don't like it' is less useful than 'the color is too dark and the pacing is too slow.' "
         "Specific feedback = specific improvements."),

        ("Always preview individual clips first",
         "Before assembling the full video, render and check individual clips. "
         "It's much easier to fix one clip than re-render the entire project."),

        ("Use CRF 16-18 for quality",
         "CRF (Constant Rate Factor) controls quality. 0 = lossless, 51 = worst. "
         "16-18 is the sweet spot for social media - visually lossless but reasonable file size."),

        ("Letterbox bars add production value",
         "Even thin 50-60px black bars at top and bottom instantly make your video look more "
         "cinematic. It's a small trick with big impact."),

        ("Test on mobile first",
         "Most viewers will watch on their phone. Always preview your edit on a phone screen "
         "before finalizing. Text that looks fine on a laptop can be unreadable on mobile."),
    ]

    for title, body in tips:
        pdf.body_bold(title)
        pdf.body(body)
        pdf.ln(1)

    # ============================================================
    # SECTION 15: NEXT STEPS
    # ============================================================
    pdf.add_page()
    pdf.section_title("15", "NEXT STEPS & RESOURCES")

    pdf.body("You now have the complete workflow for AI-powered video editing. Here's how to go further:")

    pdf.sub_title("Level Up Your Edits")
    pdf.numbered(1, "Try different pycaps templates (gentle, hype) and see what fits your brand")
    pdf.numbered(2, "Experiment with more aggressive zoom levels (2.0x+) for extreme close-ups")
    pdf.numbered(3, "Add camera shake effects (animated crop offsets) for more energy")
    pdf.numbered(4, "Use beat detection to auto-sync your cuts to the music tempo")
    pdf.numbered(5, "Try vertical (9:16) output for Instagram Reels and TikTok")

    pdf.sub_title("Useful GitHub Repositories")
    pdf.bullet("pycaps - Animated word-by-word captions (github.com/pycaps)")
    pdf.bullet("Video2X - AI video upscaling (increase resolution with AI)")
    pdf.bullet("Practical-RIFE - AI frame interpolation (smooth slow-motion)")
    pdf.bullet("AudioCraft by Meta - AI music generation (make your own tracks)")
    pdf.bullet("whisper / faster-whisper - AI speech-to-text (auto-generate captions)")

    pdf.sub_title("FFmpeg Resources")
    pdf.bullet("FFmpeg Wiki: trac.ffmpeg.org (official documentation)")
    pdf.bullet("FFmpeg Filters: ffmpeg.org/ffmpeg-filters.html (complete filter reference)")
    pdf.bullet("r/ffmpeg on Reddit (community help)")

    pdf.ln(8)
    pdf.divider()
    pdf.ln(4)

    # Closing
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(18, 18, 24)
    pdf.cell(0, 10, "Ready to Build?", align="C")
    pdf.ln(12)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 7,
        "The best way to learn is to do it. Take any video on your phone, "
        "open Claude Code, and start with the first prompt from Section 12. "
        "You'll have a professional edit in under 5 minutes.",
        align="C"
    )

    pdf.ln(12)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 120, 200)
    pdf.cell(0, 8, "Built by Waseem Nasir", align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 7, "skynetjoe.com  |  waseemnasir.com", align="C")
    pdf.ln(7)
    pdf.cell(0, 7, "Powered by Claude Code + FFmpeg + Python", align="C")

    # Save
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdf.output(OUTPUT_PDF)
    size_mb = os.path.getsize(OUTPUT_PDF) / 1048576
    pages = pdf.page_no()
    print(f"PDF created: {OUTPUT_PDF}")
    print(f"Pages: {pages} | Size: {size_mb:.2f} MB")


if __name__ == "__main__":
    build_pdf()
