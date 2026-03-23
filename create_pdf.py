#!/usr/bin/env python3
"""
AI Video Editing Guide - Premium Lead Magnet PDF V2
Full beginner guide with installation, workflow, prompts, and GitHub reference.
Uses TTF fonts for Unicode support and better typography.
"""
from fpdf import FPDF
import os

OUTPUT_DIR = "C:/Users/info/OneDrive/Desktop/business meeting"
OUTPUT_PDF = f"{OUTPUT_DIR}/AI_Video_Editing_Guide.pdf"

# Colors
BLACK = (18, 18, 24)
WHITE = (255, 255, 255)
BLUE = (0, 122, 255)
DARK_BLUE = (0, 60, 120)
LIGHT_BLUE = (230, 242, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (245, 245, 248)
DARK_GRAY = (50, 50, 55)
ACCENT = (255, 107, 53)       # Orange accent
ACCENT_BG = (255, 245, 238)   # Light orange bg
GREEN = (34, 170, 85)
GREEN_BG = (235, 250, 240)
YELLOW_BG = (255, 252, 235)
YELLOW_BORDER = (220, 190, 60)

GITHUB_URL = "https://github.com/waseemnasir2k26/ai-video-editor"


class GuidePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=28)

        # Register TTF fonts for Unicode support
        self.add_font("Segoe", "", "C:/Windows/Fonts/segoeui.ttf", uni=True)
        self.add_font("Segoe", "B", "C:/Windows/Fonts/segoeuib.ttf", uni=True)
        self.add_font("Segoe", "I", "C:/Windows/Fonts/segoeuil.ttf", uni=True)
        self.add_font("SegoeSB", "", "C:/Windows/Fonts/seguisb.ttf", uni=True)
        self.add_font("Consolas", "", "C:/Windows/Fonts/consola.ttf", uni=True)

    def header(self):
        if self.page_no() > 2:
            self.set_font("Segoe", "I", 7.5)
            self.set_text_color(*GRAY)
            self.cell(85, 8, "AI Video Editing with Claude Code", 0, 0, "L")
            self.cell(85, 8, "The Complete Beginner's Guide", 0, 0, "R")
            self.ln(5)
            self.set_draw_color(220, 220, 225)
            self.set_line_width(0.3)
            self.line(15, self.get_y(), 195, self.get_y())
            self.ln(6)

    def footer(self):
        self.set_y(-18)
        if self.page_no() > 1:
            self.set_draw_color(220, 220, 225)
            self.set_line_width(0.3)
            self.line(15, self.get_y(), 195, self.get_y())
            self.ln(3)
            self.set_font("Segoe", "", 7.5)
            self.set_text_color(*GRAY)
            self.cell(85, 6, "skynetjoe.com  |  Waseem Nasir", 0, 0, "L")
            self.cell(85, 6, f"Page {self.page_no()}", 0, 0, "R")

    # ---- Design Components ----

    def _safe_page_check(self, needed_height=20):
        """Check if we need a page break before writing content."""
        if self.get_y() + needed_height > 270:
            self.add_page()

    def section_header(self, num, title):
        """Big section header with colored background bar."""
        self._safe_page_check(22)
        self.ln(6)
        y = self.get_y()
        # Full-width dark bar
        self.set_fill_color(*BLACK)
        self.rect(15, y, 180, 13, "F")
        # Blue accent strip on left
        self.set_fill_color(*BLUE)
        self.rect(15, y, 4, 13, "F")
        # Text
        self.set_xy(22, y + 1.5)
        self.set_font("SegoeSB", "", 13)
        self.set_text_color(*WHITE)
        self.cell(0, 10, f"{num}   {title.upper()}")
        self.set_y(y + 17)
        self.set_text_color(*DARK_GRAY)

    def sub_header(self, title):
        """Subsection header with blue left border."""
        self._safe_page_check(14)
        self.ln(4)
        y = self.get_y()
        self.set_fill_color(*BLUE)
        self.rect(15, y, 2.5, 9, "F")
        self.set_xy(20, y)
        self.set_font("SegoeSB", "", 11.5)
        self.set_text_color(*DARK_BLUE)
        self.cell(0, 9, title)
        self.set_y(y + 12)
        self.set_text_color(*DARK_GRAY)

    def para(self, text, size=10):
        """Standard paragraph text with proper wrapping."""
        self.set_font("Segoe", "", size)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(170, 5.8, text, 0, "L")
        self.ln(2.5)

    def para_bold(self, text, size=10):
        """Bold paragraph."""
        self._safe_page_check(10)
        self.set_font("SegoeSB", "", size)
        self.set_text_color(*BLACK)
        self.multi_cell(170, 5.8, text, 0, "L")
        self.ln(2)

    def bullet(self, text, indent=8):
        """Bullet point with proper wrapping."""
        self._safe_page_check(10)
        self.set_font("Segoe", "", 10)
        self.set_text_color(*DARK_GRAY)
        x = self.get_x()
        self.set_x(x + indent)
        self.set_font("SegoeSB", "", 10)
        self.cell(5, 5.8, "\u2022")
        self.set_font("Segoe", "", 10)
        self.multi_cell(170 - indent - 5, 5.8, f" {text}", 0, "L")
        self.ln(1.5)

    def numbered_item(self, num, text):
        """Numbered item with blue number."""
        self._safe_page_check(12)
        x = self.get_x()
        self.set_x(x + 6)
        self.set_font("SegoeSB", "", 11)
        self.set_text_color(*BLUE)
        self.cell(9, 6, f"{num}.")
        self.set_font("Segoe", "", 10)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(155, 5.8, text, 0, "L")
        self.ln(2)

    def code_block(self, code):
        """Code block with gray background and monospace font."""
        self._safe_page_check(15)
        lines = code.strip().split("\n")
        block_height = len(lines) * 5.5 + 8
        y_start = self.get_y()

        # Background
        self.set_fill_color(*LIGHT_GRAY)
        self.set_draw_color(210, 210, 215)

        # Check if block fits on page
        if y_start + block_height > 268:
            self.add_page()
            y_start = self.get_y()

        self.rect(18, y_start, 174, block_height, "DF")

        self.set_font("Consolas", "", 8.2)
        self.set_text_color(40, 40, 50)
        self.set_y(y_start + 4)
        for line in lines:
            self.set_x(22)
            self.cell(166, 5.5, line, 0, 1)
        self.set_y(y_start + block_height + 4)

    def prompt_box(self, prompt_text):
        """Styled prompt box with blue header and light background."""
        self._safe_page_check(25)
        y_start = self.get_y()

        # Header bar
        self.set_fill_color(*DARK_BLUE)
        self.rect(18, y_start, 174, 8, "F")
        self.set_xy(20, y_start + 0.5)
        self.set_font("SegoeSB", "", 8.5)
        self.set_text_color(*WHITE)
        self.cell(170, 7, "\u00BB  PROMPT TO CLAUDE CODE")

        # Content area
        y_content = y_start + 8
        self.set_xy(18, y_content)
        self.set_fill_color(*LIGHT_BLUE)
        self.set_font("Segoe", "I", 9.5)
        self.set_text_color(*DARK_BLUE)

        # Calculate height needed
        self.set_xy(22, y_content + 3)
        y_before = self.get_y()
        self.multi_cell(166, 5.8, f'"{prompt_text}"', 0, "L")
        y_after = self.get_y()
        content_h = y_after - y_content + 3

        # Draw background behind text
        self.set_fill_color(*LIGHT_BLUE)
        self.rect(18, y_content, 174, content_h, "F")

        # Rewrite text on top of background
        self.set_xy(22, y_content + 3)
        self.set_font("Segoe", "I", 9.5)
        self.set_text_color(*DARK_BLUE)
        self.multi_cell(166, 5.8, f'"{prompt_text}"', 0, "L")
        self.ln(4)
        self.set_text_color(*DARK_GRAY)

    def tip_box(self, title, text, color_bg=YELLOW_BG, color_icon=YELLOW_BORDER, icon="!"):
        """Colored tip/warning box."""
        self._safe_page_check(22)
        y_start = self.get_y()

        # Calculate text height
        self.set_font("Segoe", "", 9)
        # Rough estimate: ~40 chars per line, 5.5 height per line
        est_lines = max(1, len(text) / 55)
        box_h = max(16, est_lines * 5.5 + 14)

        if y_start + box_h > 268:
            self.add_page()
            y_start = self.get_y()

        # Background
        self.set_fill_color(*color_bg)
        self.set_draw_color(*color_icon)
        self.set_line_width(0.5)

        self.rect(18, y_start, 174, box_h, "DF")

        # Icon circle
        self.set_fill_color(*color_icon)
        self.set_xy(22, y_start + 3)
        self.set_font("SegoeSB", "", 9)
        self.set_text_color(*WHITE)

        # Title
        self.set_xy(24, y_start + 3)
        r, g, b = color_icon
        self.set_text_color(r, g, b)
        self.set_font("SegoeSB", "", 9)
        self.cell(0, 5.5, title)

        # Text
        self.set_xy(24, y_start + 10)
        self.set_font("Segoe", "", 9)
        self.set_text_color(60, 55, 40)
        self.multi_cell(162, 5.2, text, 0, "L")

        self.set_y(y_start + box_h + 4)
        self.set_text_color(*DARK_GRAY)
        self.set_line_width(0.2)

    def pro_tip(self, text):
        self.tip_box("PRO TIP", text, YELLOW_BG, YELLOW_BORDER)

    def important_box(self, text):
        self.tip_box("IMPORTANT", text, ACCENT_BG, ACCENT)

    def success_box(self, text):
        self.tip_box("QUICK WIN", text, GREEN_BG, GREEN)

    def divider(self):
        self.ln(2)
        self.set_draw_color(230, 230, 235)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)

    def table_row(self, col1, col2, header=False):
        """Simple two-column table row."""
        self._safe_page_check(10)
        if header:
            self.set_fill_color(*BLACK)
            self.set_text_color(*WHITE)
            self.set_font("SegoeSB", "", 9)
        else:
            self.set_fill_color(*LIGHT_GRAY)
            self.set_text_color(*DARK_GRAY)
            self.set_font("Segoe", "", 9)

        self.set_x(18)
        self.cell(55, 8, f"  {col1}", 1, 0, "L", True)
        self.cell(119, 8, f"  {col2}", 1, 1, "L", True)

    # ---- Cover Page ----

    def cover_page(self):
        self.add_page()
        # Top accent bar
        self.set_fill_color(*BLUE)
        self.rect(0, 0, 210, 5, "F")

        # Main dark block
        self.set_fill_color(*BLACK)
        self.rect(0, 30, 210, 110, "F")

        # Blue accent line inside dark block
        self.set_fill_color(*BLUE)
        self.rect(20, 50, 50, 3, "F")

        # Title
        self.set_y(60)
        self.set_font("SegoeSB", "", 36)
        self.set_text_color(*WHITE)
        self.set_x(20)
        self.cell(0, 16, "AI VIDEO")
        self.ln(16)
        self.set_x(20)
        self.cell(0, 16, "EDITING")
        self.ln(20)

        self.set_font("Segoe", "", 16)
        self.set_text_color(*BLUE)
        self.set_x(20)
        self.cell(0, 10, "with Claude Code")
        self.ln(14)

        self.set_font("Segoe", "", 11)
        self.set_text_color(180, 180, 185)
        self.set_x(20)
        self.cell(0, 7, "The Complete Beginner's Guide to Professional")
        self.ln(7)
        self.set_x(20)
        self.cell(0, 7, "Video Editing Using AI + FFmpeg + Python")

        # What's inside box
        self.set_y(155)
        self.set_font("SegoeSB", "", 12)
        self.set_text_color(*BLACK)
        self.set_x(20)
        self.cell(0, 8, "WHAT'S INSIDE")

        self.ln(10)
        items = [
            "Step-by-step setup guide (Claude Code, FFmpeg, Python, pycaps)",
            "Exact prompts used to create 4 professional video edits",
            "Color grading, zoom punches, and speed ramping explained",
            "Royalty-free music sourcing and audio mixing",
            "Animated TikTok/Reels-style captions",
            "Complete Python scripts + GitHub repository link",
            "Pro tips and common mistakes to avoid",
        ]
        for item in items:
            self.set_font("Segoe", "", 9.5)
            self.set_text_color(*DARK_GRAY)
            self.set_x(22)
            self.set_text_color(*BLUE)
            self.set_font("SegoeSB", "", 9.5)
            self.cell(5, 6.5, "\u2713")
            self.set_font("Segoe", "", 9.5)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 6.5, f"  {item}")
            self.ln(6.5)

        # Bottom section
        self.set_y(235)
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(20, 233, 170, 22, "F")
        self.set_xy(25, 236)
        self.set_font("SegoeSB", "", 9)
        self.set_text_color(*BLUE)
        self.cell(0, 6, "GITHUB REPOSITORY")
        self.ln(7)
        self.set_x(25)
        self.set_font("Segoe", "", 9)
        self.set_text_color(*DARK_GRAY)
        self.cell(0, 6, f"Clone the scripts:  {GITHUB_URL}")

        # Author
        self.set_y(265)
        self.set_font("Segoe", "", 9)
        self.set_text_color(*GRAY)
        self.cell(0, 6, "by Waseem Nasir  |  skynetjoe.com  |  waseemnasir.com", 0, 0, "C")

        # Bottom accent bar
        self.set_fill_color(*BLUE)
        self.rect(0, 292, 210, 5, "F")


def build_pdf():
    pdf = GuidePDF()

    # ============================================================
    # COVER
    # ============================================================
    pdf.cover_page()

    # ============================================================
    # TABLE OF CONTENTS
    # ============================================================
    pdf.add_page()
    pdf.ln(5)
    pdf.set_fill_color(*BLUE)
    pdf.rect(15, pdf.get_y(), 3, 10, "F")
    pdf.set_x(22)
    pdf.set_font("SegoeSB", "", 22)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 10, "Table of Contents")
    pdf.ln(18)

    toc = [
        ("01", "Prerequisites & Requirements"),
        ("02", "Installing Claude Code"),
        ("03", "Installing FFmpeg"),
        ("04", "Installing Python & pycaps"),
        ("05", "The Quick Start (Use Our GitHub Repo)"),
        ("06", "The Workflow Overview"),
        ("07", "Step-by-Step: Analyze Your Footage"),
        ("08", "Step-by-Step: Define Your Edit Style"),
        ("09", "Step-by-Step: Color Grading"),
        ("10", "Step-by-Step: Zoom Punches & Speed Ramping"),
        ("11", "Step-by-Step: Transitions"),
        ("12", "Step-by-Step: Royalty-Free Music"),
        ("13", "Step-by-Step: Animated Captions"),
        ("14", "The 4 Edit Styles Explained"),
        ("15", "All Prompts Used (Copy & Paste Ready)"),
        ("16", "The Python Scripts Architecture"),
        ("17", "Pro Tips & Common Mistakes"),
        ("18", "Next Steps & Resources"),
    ]
    for num, title in toc:
        pdf.set_x(20)
        pdf.set_font("SegoeSB", "", 10.5)
        pdf.set_text_color(*BLUE)
        pdf.cell(12, 9, num)
        pdf.set_font("Segoe", "", 10.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.cell(130, 9, title)
        pdf.ln(9)
        # subtle line
        pdf.set_draw_color(240, 240, 242)
        pdf.line(20, pdf.get_y(), 185, pdf.get_y())

    # ============================================================
    # SECTION 1: PREREQUISITES
    # ============================================================
    pdf.add_page()
    pdf.section_header("01", "Prerequisites & Requirements")

    pdf.para(
        "Before we start, let's be clear about what you need. This workflow uses "
        "Claude Code, which is Anthropic's AI-powered coding assistant that runs in your terminal. "
        "It writes the video editing scripts for you - you just describe what you want."
    )

    pdf.important_box(
        "Claude Code requires a PAID Anthropic plan. The free tier will NOT work for this workflow "
        "because video editing scripts need extended conversations and multiple tool calls. "
        "You need either the Pro plan ($20/month) or the Max plan ($100/month) at minimum."
    )

    pdf.sub_header("What You Need")

    pdf.table_row("Tool", "Purpose", header=True)
    pdf.table_row("Claude Code", "AI writes all your editing scripts (requires paid plan)")
    pdf.table_row("FFmpeg", "Open-source video processor (free)")
    pdf.table_row("Python 3.8+", "Runs the scripts Claude writes (free)")
    pdf.table_row("pycaps", "Animated word-by-word captions (free, pip install)")
    pdf.table_row("Node.js 18+", "Required to install Claude Code (free)")
    pdf.table_row("Git (optional)", "Clone the GitHub repo with ready scripts")

    pdf.ln(4)

    pdf.sub_header("System Requirements")
    pdf.bullet("Windows 10/11, macOS, or Linux")
    pdf.bullet("At least 8GB RAM (video processing is memory-intensive)")
    pdf.bullet("2GB+ free disk space for temporary files during rendering")
    pdf.bullet("Internet connection (Claude Code connects to Anthropic's servers)")

    pdf.sub_header("Estimated Cost")
    pdf.table_row("Item", "Cost", header=True)
    pdf.table_row("Claude Code (Pro plan)", "$20/month - REQUIRED minimum")
    pdf.table_row("Claude Code (Max plan)", "$100/month - recommended for heavy use")
    pdf.table_row("FFmpeg", "Free and open-source")
    pdf.table_row("Python", "Free and open-source")
    pdf.table_row("pycaps", "Free and open-source")
    pdf.table_row("Royalty-free music", "Free (Mixkit.co)")

    pdf.ln(3)
    pdf.pro_tip(
        "The Pro plan ($20/month) is enough for most users. If you're editing videos daily or "
        "running long sessions, the Max plan gives you more usage. Both work for this workflow."
    )

    # ============================================================
    # SECTION 2: INSTALLING CLAUDE CODE
    # ============================================================
    pdf.add_page()
    pdf.section_header("02", "Installing Claude Code")

    pdf.para(
        "Claude Code is Anthropic's command-line AI assistant. It runs in your terminal "
        "and can read files, write code, run commands, and build entire projects from natural "
        "language prompts. Here's how to install it from scratch."
    )

    pdf.sub_header("Step 1: Install Node.js")
    pdf.para("Claude Code requires Node.js 18 or newer. If you don't have it:")

    pdf.para_bold("Windows:")
    pdf.numbered_item(1, "Go to nodejs.org and download the LTS version (the big green button)")
    pdf.numbered_item(2, "Run the installer, click Next through everything (defaults are fine)")
    pdf.numbered_item(3, 'Open a new terminal (search "cmd" or "PowerShell" in Start menu)')
    pdf.numbered_item(4, "Verify: type  node --version  and you should see v18 or higher")

    pdf.para_bold("macOS:")
    pdf.code_block("brew install node")

    pdf.para_bold("Linux (Ubuntu/Debian):")
    pdf.code_block(
        "curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -\n"
        "sudo apt-get install -y nodejs"
    )

    pdf.sub_header("Step 2: Install Claude Code")
    pdf.para("Once Node.js is installed, run this single command in your terminal:")
    pdf.code_block("npm install -g @anthropic-ai/claude-code")

    pdf.para("That's it. Claude Code is now installed globally on your system.")

    pdf.sub_header("Step 3: Log In")
    pdf.numbered_item(1, "Open your terminal and type:  claude")
    pdf.numbered_item(2, "It will open a browser window to log in to your Anthropic account")
    pdf.numbered_item(3, "Log in with your account (the one with Pro or Max subscription)")
    pdf.numbered_item(4, "Once authenticated, you're back in the terminal ready to go")

    pdf.sub_header("Step 4: Verify It Works")
    pdf.code_block(
        '# Open a terminal and type:\n'
        'claude\n\n'
        '# You should see the Claude Code prompt.\n'
        '# Try typing: "What version of Claude are you?"\n'
        '# It should respond - you\'re ready!'
    )

    pdf.important_box(
        "If you see an error about authentication or billing, make sure your Anthropic account "
        "has an active Pro ($20/mo) or Max ($100/mo) subscription at console.anthropic.com/settings/billing"
    )

    # ============================================================
    # SECTION 3: INSTALLING FFMPEG
    # ============================================================
    pdf.add_page()
    pdf.section_header("03", "Installing FFmpeg")

    pdf.para(
        "FFmpeg is the engine that does all the actual video processing - cutting, color grading, "
        "transitions, zoom, speed changes, audio mixing. It's free, open-source, and used by "
        "every major tech company (YouTube, Netflix, etc). Claude Code writes FFmpeg commands "
        "for you, but FFmpeg needs to be installed on your system."
    )

    pdf.sub_header("Windows Installation")
    pdf.numbered_item(1, "Go to gyan.dev/ffmpeg/builds/ (official Windows builds)")
    pdf.numbered_item(2, 'Download "ffmpeg-release-essentials.zip" (the smaller one is fine)')
    pdf.numbered_item(3, "Extract the ZIP file to a permanent location, for example C:\\ffmpeg")
    pdf.numbered_item(4, 'Inside the extracted folder, find the "bin" subfolder. It contains ffmpeg.exe and ffprobe.exe')
    pdf.numbered_item(5, 'Add the bin folder to your system PATH:')

    pdf.code_block(
        "How to add to PATH on Windows:\n"
        "1. Press Win + S, search 'Environment Variables'\n"
        "2. Click 'Edit the system environment variables'\n"
        "3. Click 'Environment Variables' button\n"
        "4. Under 'System variables', find 'Path', click Edit\n"
        "5. Click 'New' and add: C:\\ffmpeg\\bin\n"
        "6. Click OK on everything\n"
        "7. CLOSE and REOPEN your terminal"
    )

    pdf.numbered_item(6, "Verify installation - open a NEW terminal and type:")
    pdf.code_block("ffmpeg -version")
    pdf.para("You should see version info. If you see 'not recognized', restart your terminal or PC.")

    pdf.sub_header("macOS Installation")
    pdf.code_block(
        "# Using Homebrew (install Homebrew first from brew.sh if needed):\n"
        "brew install ffmpeg"
    )

    pdf.sub_header("Linux (Ubuntu/Debian)")
    pdf.code_block("sudo apt update && sudo apt install ffmpeg -y")

    pdf.pro_tip(
        "The most common issue on Windows is FFmpeg not being in PATH. If Claude Code says "
        "'ffmpeg not found', it means the PATH wasn't set correctly. Close ALL terminal windows "
        "and open a fresh one after adding to PATH."
    )

    # ============================================================
    # SECTION 4: PYTHON & PYCAPS
    # ============================================================
    pdf.add_page()
    pdf.section_header("04", "Installing Python & pycaps")

    pdf.sub_header("Install Python")

    pdf.para_bold("Windows:")
    pdf.numbered_item(1, "Go to python.org/downloads and download the latest Python 3.x")
    pdf.numbered_item(2, 'IMPORTANT: Check the box that says "Add Python to PATH" during installation')
    pdf.numbered_item(3, "Click Install Now and let it complete")
    pdf.numbered_item(4, "Verify in a new terminal:")
    pdf.code_block("python --version\npip --version")

    pdf.para_bold("macOS:")
    pdf.code_block("brew install python")

    pdf.para_bold("Linux:")
    pdf.code_block("sudo apt install python3 python3-pip -y")

    pdf.sub_header("Install pycaps (Animated Captions)")
    pdf.para(
        "pycaps adds animated word-by-word captions to your videos, like the text effects "
        "you see on TikTok and Instagram Reels. Install it with pip:"
    )
    pdf.code_block("pip install pycaps")

    pdf.sub_header("Install fpdf2 (PDF Generation - Optional)")
    pdf.para("Only needed if you want to generate lead magnet PDFs like this one:")
    pdf.code_block("pip install fpdf2")

    pdf.sub_header("Verify Everything Works")
    pdf.para("Open a terminal and run these commands to confirm all tools are installed:")
    pdf.code_block(
        "node --version       # Should show v18+\n"
        "claude --version     # Should show Claude Code version\n"
        "ffmpeg -version      # Should show FFmpeg version\n"
        "python --version     # Should show Python 3.8+\n"
        "pip show pycaps      # Should show pycaps package info"
    )

    pdf.success_box(
        "If all 5 commands work, you're fully set up! You can skip straight to Section 05 "
        "for the fastest way to start editing videos."
    )

    # ============================================================
    # SECTION 5: QUICK START (GITHUB REPO)
    # ============================================================
    pdf.add_page()
    pdf.section_header("05", "The Quick Start (Use Our GitHub Repo)")

    pdf.para(
        "Instead of building everything from scratch, you can clone our GitHub repository "
        "which has all the scripts ready to go. Just point them at your video and run."
    )

    pdf.sub_header("Option A: Clone with Git (Recommended)")
    pdf.code_block(
        f"git clone {GITHUB_URL}.git\n"
        "cd ai-video-editor\n"
        "pip install -r requirements.txt"
    )

    pdf.sub_header("Option B: Download ZIP (No Git Required)")
    pdf.numbered_item(1, f"Go to: {GITHUB_URL}")
    pdf.numbered_item(2, 'Click the green "Code" button, then "Download ZIP"')
    pdf.numbered_item(3, "Extract the ZIP anywhere on your computer")
    pdf.numbered_item(4, "Open terminal in that folder and run:  pip install -r requirements.txt")

    pdf.sub_header("What's In The Repo")
    pdf.table_row("File", "What It Does", header=True)
    pdf.table_row("config.py", "All presets: color grades, zoom levels, speed ramps")
    pdf.table_row("energy_edit.py", "Single high-energy edit with zoom punches + flash cuts")
    pdf.table_row("three_versions.py", "Renders 3 different styled versions at once")
    pdf.table_row("create_pdf.py", "Generates this PDF guide")
    pdf.table_row("requirements.txt", "Python dependencies (pycaps, fpdf2)")

    pdf.sub_header("Option C: Let Claude Code Do Everything")
    pdf.para(
        "The fastest approach - just open Claude Code in your terminal and describe "
        "what you want. Claude will write custom scripts for YOUR specific video:"
    )
    pdf.code_block(
        "# Open terminal, navigate to a working folder, then:\n"
        "claude\n\n"
        "# Then type this prompt:\n"
        '"I have a video at [YOUR PATH]. Edit it into a short-form\n'
        ' social media video with zoom punches, speed ramping, flash\n'
        ' cuts, royalty-free music, and animated captions. Give me 3\n'
        ' versions: one energy/hype, one cinematic, one clean/smooth."'
    )

    pdf.pro_tip(
        "Option C is the most flexible because Claude Code adapts to YOUR specific video "
        "content, duration, and resolution. The GitHub scripts are great starting templates, "
        "but Claude can customize everything on the fly."
    )

    # ============================================================
    # SECTION 6: WORKFLOW OVERVIEW
    # ============================================================
    pdf.add_page()
    pdf.section_header("06", "The Workflow Overview")

    pdf.para(
        "Here's the complete pipeline from raw footage to finished edit. "
        "Each step is handled by Claude Code writing FFmpeg commands."
    )
    pdf.ln(2)

    steps = [
        ("ANALYZE", "Give Claude Code your video file. It runs ffprobe to check resolution, duration, framerate, and codec."),
        ("DEFINE STYLE", "Tell Claude what vibe you want: energetic, cinematic, clean, dark, etc. Be specific about mood and pacing."),
        ("CLIP SELECTION", "Claude picks the best moments and defines start/end timestamps for each clip."),
        ("COLOR GRADE", "FFmpeg adjusts brightness, contrast, saturation, color balance, and sharpness."),
        ("ZOOM + SPEED", "Each clip gets its own zoom level (crop + upscale) and speed (slow-mo or fast-forward)."),
        ("TRANSITIONS", "Clips are joined with flash cuts, crossfades, or other transitions."),
        ("MUSIC", "Royalty-free music is mixed in with fade-in/out and volume control."),
        ("CAPTIONS", "Animated word-by-word captions are rendered using pycaps."),
        ("OUTPUT", "Final MP4 with H.264, AAC audio, optimized for social media upload."),
    ]

    for i, (name, desc) in enumerate(steps, 1):
        pdf._safe_page_check(16)
        y = pdf.get_y()
        # Number circle
        pdf.set_fill_color(*BLUE)
        pdf.set_xy(20, y)
        pdf.set_font("SegoeSB", "", 10)
        pdf.set_text_color(*WHITE)
        pdf.cell(8, 8, str(i), 0, 0, "C", True)
        # Name
        pdf.set_xy(31, y)
        pdf.set_font("SegoeSB", "", 10)
        pdf.set_text_color(*BLACK)
        pdf.cell(30, 8, name)
        # Description
        pdf.set_xy(31, y + 8)
        pdf.set_font("Segoe", "", 9.5)
        pdf.set_text_color(*DARK_GRAY)
        pdf.multi_cell(155, 5.5, desc, 0, "L")
        pdf.ln(3)

    pdf.success_box(
        "The entire pipeline runs in 2-4 minutes on a modern laptop. "
        "You describe what you want in plain English, Claude writes the code, and FFmpeg renders it."
    )

    # ============================================================
    # SECTION 7: ANALYZE FOOTAGE
    # ============================================================
    pdf.add_page()
    pdf.section_header("07", "Step-by-Step: Analyze Your Footage")

    pdf.para(
        "Before any editing, Claude Code needs to understand your source material. "
        "Give it your video file path and ask for analysis."
    )

    pdf.prompt_box(
        "Here's my video file: C:/path/to/your/video.mp4 - Analyze it and tell me "
        "the resolution, duration, framerate, and codec. I want to turn this into "
        "a professional short-form social media edit."
    )

    pdf.para("Claude Code runs this FFprobe command behind the scenes:")
    pdf.code_block(
        'ffprobe -v quiet -show_entries format=duration,size \\\n'
        '  -show_entries stream=width,height,r_frame_rate,codec_name \\\n'
        '  -of json "your_video.mp4"'
    )

    pdf.sub_header("What The Analysis Tells You")
    pdf.bullet("Resolution: How much you can zoom before losing quality (1080p = up to 1.8x zoom)")
    pdf.bullet("Duration: Total length to plan your clip selections")
    pdf.bullet("Framerate: Determines flash cut duration and slow-mo limits")
    pdf.bullet("Codec: Usually H.264 - confirms compatibility")

    pdf.sub_header("Our Example Video")
    pdf.table_row("Property", "Value", header=True)
    pdf.table_row("Resolution", "1920x1080 (Full HD)")
    pdf.table_row("Duration", "49 seconds")
    pdf.table_row("Framerate", "23.976 fps (24fps film standard)")
    pdf.table_row("Codec", "H.264 (universal compatibility)")
    pdf.table_row("Content", "Two people discussing business over laptops in a cafe")

    # ============================================================
    # SECTION 8: EDIT STYLE
    # ============================================================
    pdf.add_page()
    pdf.section_header("08", "Step-by-Step: Define Your Edit Style")

    pdf.para(
        "This is the most important decision. Your style choice determines clip selection, "
        "speed, color grade, music, and transitions. Here are the 4 styles we created:"
    )

    styles = [
        ("BREAKBEAT ENERGY", "25 seconds",
         "Fast cuts (1-2s each), aggressive zoom punches, white flash transitions, breakbeat music. "
         "Speed varies between 0.5x slow-mo and 1.5x fast. 10+ clips. "
         "Best for: motivational content, hustle culture, TikTok, Reels."),
        ("CINEMATIC EPIC", "38 seconds",
         "Longer clips (4-8s), heavy slow-motion (0.5x-0.85x), smooth crossfade transitions, "
         "orchestral/epic music. Fewer cuts, more dramatic. 7 clips. "
         "Best for: brand films, YouTube intros, dramatic storytelling."),
        ("CLEAN SOUL", "28 seconds",
         "Medium clips (3-5s), gentle zooms (1.0x-1.3x), smooth crossfades, soul/lo-fi music. "
         "Natural feel, not over-edited. 7 clips. "
         "Best for: lifestyle content, behind-the-scenes, authentic branding."),
        ("HIP-HOP ENERGY", "25 seconds",
         "Mixed speed ramping, tight crop zooms, white flash cuts, hip-hop beat. "
         "Aggressive color grade. 8 clips. "
         "Best for: high-energy social content, promo videos, attention-grabbing ads."),
    ]

    for name, dur, desc in styles:
        pdf._safe_page_check(28)
        pdf.sub_header(f"{name}  ({dur})")
        pdf.para(desc)

    pdf.prompt_box(
        "Give me 3 versions of this video: one with breakbeat energy and fast cuts, "
        "one cinematic with dramatic slow-mo and epic music, and one clean and smooth "
        "with soul music. Keep the color bright and natural - don't darken it."
    )

    pdf.pro_tip(
        "Be specific about what you DON'T want. Saying 'don't darken the video' saved us "
        "from over-processing. AI tends to go heavy on effects - set clear boundaries."
    )

    # ============================================================
    # SECTION 9: COLOR GRADING
    # ============================================================
    pdf.add_page()
    pdf.section_header("09", "Step-by-Step: Color Grading")

    pdf.para(
        "Color grading transforms the look and feel of your video. FFmpeg's eq, "
        "colorbalance, and unsharp filters give you full control."
    )

    pdf.sub_header("Bright Energy Grade")
    pdf.code_block(
        "eq=brightness=0.06:contrast=1.15:saturation=0.90,\n"
        "colorbalance=rs=0.06:gs=0.02:bs=-0.04,\n"
        "unsharp=5:5:0.5"
    )
    pdf.para(
        "Boosted brightness, punchy contrast, slightly desaturated for that film look. "
        "Warm tones pushed via red highlights. Strong sharpening for crisp detail."
    )

    pdf.sub_header("Cinematic Warm Grade")
    pdf.code_block(
        "eq=brightness=0.04:contrast=1.10:saturation=0.82,\n"
        "colorbalance=rs=0.08:gs=0.03:bs=-0.03,\n"
        "unsharp=3:3:0.4"
    )
    pdf.para(
        "More desaturated for a filmic look. Warmer color balance. This gives that "
        "Hollywood orange-and-teal vibe without being too heavy."
    )

    pdf.sub_header("Clean Natural Grade")
    pdf.code_block(
        "eq=brightness=0.05:contrast=1.08:saturation=0.95,\n"
        "colorbalance=rs=0.04:gs=0.02:bs=-0.02,\n"
        "unsharp=3:3:0.3"
    )
    pdf.para(
        "Minimal processing. Near-original saturation with a subtle warmth. "
        "Enhanced but still looks natural and authentic."
    )

    pdf.sub_header("What Each Parameter Does")
    pdf.table_row("Parameter", "What It Controls", header=True)
    pdf.table_row("brightness", "-1.0 to 1.0 (0 = no change, 0.05 = slightly brighter)")
    pdf.table_row("contrast", "0.0 to 2.0 (1.0 = no change, 1.15 = punchy)")
    pdf.table_row("saturation", "0.0 to 2.0 (1.0 = normal, 0.8 = desaturated/filmic)")
    pdf.table_row("colorbalance rs/gs/bs", "Shadow color shift (+red = warm shadows)")
    pdf.table_row("colorbalance rm/gm/bm", "Midtone shift (where skin tones live)")
    pdf.table_row("unsharp W:H:S", "Sharpening (5:5:0.5 = strong, 3:3:0.3 = subtle)")

    pdf.ln(3)
    pdf.important_box(
        "AVOID going below brightness=0.0 or above contrast=1.25 unless you specifically "
        "want a dark/moody look. Keeping it bright and natural is almost always better, "
        "especially for social media where people scroll fast on bright phone screens."
    )

    # ============================================================
    # SECTION 10: ZOOM & SPEED
    # ============================================================
    pdf.add_page()
    pdf.section_header("10", "Step-by-Step: Zoom Punches & Speed Ramping")

    pdf.sub_header("Zoom Punches (Crop + Scale)")
    pdf.para(
        "A 'zoom punch' simulates a camera cut to a tighter shot. FFmpeg crops a region "
        "of the frame and scales it back to full resolution, creating the illusion of "
        "multiple camera angles from a single wide shot."
    )
    pdf.code_block(
        "# Crop 1067x600 at position (46, 80), then upscale\n"
        "crop=1067:600:46:80,scale=1920:1080:flags=lanczos"
    )
    pdf.para("Parameters: crop=WIDTH:HEIGHT:X_POSITION:Y_POSITION")

    pdf.sub_header("Zoom Level Reference")
    pdf.table_row("Zoom Level", "Crop Size (for 1080p source)", header=True)
    pdf.table_row("1.0x (no zoom)", "Full 1920x1080 frame - wide establishing shots")
    pdf.table_row("1.3x zoom", "crop=1477:831 - medium shot, both people visible")
    pdf.table_row("1.5x zoom", "crop=1280:720 - medium-tight, focus on one person")
    pdf.table_row("1.8x zoom", "crop=1067:600 - tight close-up")
    pdf.table_row("2.0x zoom", "crop=960:540 - extreme close-up")

    pdf.sub_header("Speed Ramping")
    pdf.para(
        "Speed ramping means different clips play at different speeds. "
        "This creates rhythm - fast sections build energy, slow sections add drama."
    )
    pdf.code_block(
        "# Slow motion (0.5x = half speed, twice as long)\n"
        "setpts=PTS/0.5\n\n"
        "# Fast motion (1.5x = 50% faster)\n"
        "setpts=PTS/1.5"
    )

    pdf.sub_header("Speed Reference")
    pdf.table_row("Speed", "Feel & When To Use", header=True)
    pdf.table_row("0.50x", "Dramatic slow-mo - key moments, reactions, pointing")
    pdf.table_row("0.65x", "Smooth slow-mo - writing, typing, detail shots")
    pdf.table_row("0.80x", "Subtle slow - cinematic feel, still natural")
    pdf.table_row("1.00x", "Normal speed - standard clips")
    pdf.table_row("1.20x", "Slightly fast - energy boost")
    pdf.table_row("1.35x", "Fast - quick establishing shots")
    pdf.table_row("1.50x", "Very fast - rapid cuts, high energy")

    pdf.ln(3)
    pdf.pro_tip(
        "The magic is in CONTRAST. A fast clip (1.5x) followed immediately by a slow-mo "
        "clip (0.5x) creates a powerful visual punch. This is what separates amateur "
        "edits from professional ones. Uniform speed throughout = boring."
    )

    # ============================================================
    # SECTION 11: TRANSITIONS
    # ============================================================
    pdf.add_page()
    pdf.section_header("11", "Step-by-Step: Transitions")

    pdf.sub_header("White Flash Cuts")
    pdf.para(
        "A white flash between clips creates a high-energy punch feel. We generate a "
        "tiny white frame (2 frames at 24fps = 0.083 seconds) and insert it between clips."
    )
    pdf.code_block(
        "# Generate a white flash frame:\n"
        'ffmpeg -y -f lavfi -i \\\n'
        '  "color=white:s=1920x1080:d=0.083:r=24000/1001" \\\n'
        '  -c:v libx264 flash.mp4\n\n'
        "# Concat file (clips with flash between each):\n"
        "file 'clip_00.mp4'\n"
        "file 'flash.mp4'\n"
        "file 'clip_01.mp4'\n"
        "file 'flash.mp4'\n"
        "file 'clip_02.mp4'"
    )

    pdf.sub_header("Crossfade Transitions")
    pdf.para("For smoother transitions, FFmpeg's xfade filter blends clips together:")
    pdf.code_block(
        "[0:v][1:v]xfade=transition=fade:duration=0.4:offset=3.5[x1];\n"
        "[x1][2:v]xfade=transition=smoothleft:duration=0.4:offset=6.8[vout]"
    )

    pdf.sub_header("Available Transition Types")
    pdf.table_row("Type", "Description & Best Use", header=True)
    pdf.table_row("fade", "Simple opacity crossfade - always looks good, safest choice")
    pdf.table_row("fadeblack", "Fade through black - dramatic, cinematic")
    pdf.table_row("fadewhite", "Fade through white - bright, energetic")
    pdf.table_row("smoothleft", "Directional slide blend - modern, dynamic")
    pdf.table_row("dissolve", "Gradual pixel dissolve - subtle, artistic")
    pdf.table_row("wiperight", "Hard wipe - retro, bold, attention-grabbing")

    pdf.sub_header("When To Use Which")
    pdf.bullet("Flash cuts: High-energy edits, music videos, motivational content")
    pdf.bullet("Crossfades: Cinematic edits, brand films, smooth storytelling")
    pdf.bullet("Mix of both: Flash for beat-synced moments, crossfade for everything else")

    # ============================================================
    # SECTION 12: MUSIC
    # ============================================================
    pdf.add_page()
    pdf.section_header("12", "Step-by-Step: Royalty-Free Music")

    pdf.para(
        "Music is 50% of the emotional impact. Choose the wrong track and your edit "
        "falls flat, no matter how good the visuals are."
    )

    pdf.sub_header("Where To Find Royalty-Free Music")
    pdf.table_row("Source", "Details", header=True)
    pdf.table_row("Mixkit.co", "Completely free, no attribution needed, high quality")
    pdf.table_row("Pixabay Music", "Free, large library, various genres")
    pdf.table_row("YouTube Audio Library", "Free for YouTube content creators")
    pdf.table_row("Epidemic Sound", "Paid ($15/mo) but premium quality")
    pdf.table_row("Artlist", "Paid ($10/mo) unlimited downloads")

    pdf.sub_header("Tracks We Used")
    pdf.bullet("Breakbeat: 'No Warning' from Mixkit - high-energy, perfect for fast edits")
    pdf.bullet("Epic: 'Life's a Movie' from Mixkit - orchestral film score, dramatic")
    pdf.bullet("Soul: 'Feel Alive' from Mixkit - smooth soul, warm and authentic")
    pdf.bullet("Hip-Hop: 'Daylight Robbery' from Mixkit - hard-hitting beat")

    pdf.sub_header("Audio Mixing with FFmpeg")
    pdf.code_block(
        "# Trim music to video length, add fades, set volume:\n"
        "[1:a]atrim=0:25.5,         # Trim to 25.5 seconds\n"
        "asetpts=PTS-STARTPTS,       # Reset timestamps\n"
        "afade=t=in:d=0.8,           # Fade in over 0.8 seconds\n"
        "afade=t=out:st=24.5:d=1.0,  # Fade out last 1.0 second\n"
        "volume=0.40[aout]           # 40% volume"
    )

    pdf.sub_header("Volume Guide")
    pdf.table_row("Volume", "When To Use", header=True)
    pdf.table_row("0.30 - 0.35", "Background level (if you have voiceover/dialogue)")
    pdf.table_row("0.38 - 0.45", "Medium presence (best for no-dialogue edits)")
    pdf.table_row("0.50+", "Dominant (music video feel)")

    pdf.ln(3)
    pdf.pro_tip(
        "Always remove the original audio first (-an flag when processing clips) and "
        "add music separately. The original audio from raw footage is almost never "
        "clean enough to use in a polished edit."
    )

    # ============================================================
    # SECTION 13: CAPTIONS
    # ============================================================
    pdf.add_page()
    pdf.section_header("13", "Step-by-Step: Animated Captions")

    pdf.para(
        "pycaps adds TikTok/Reels-style animated word-by-word captions. Each word "
        "pops in with animation, making your text feel dynamic and engaging."
    )

    pdf.sub_header("Create Your SRT File")
    pdf.para("SRT (SubRip) is the standard caption format. Each entry has an index, time range, and text:")
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

    pdf.sub_header("Render With pycaps")
    pdf.code_block(
        'pycaps render \\\n'
        '  --input "base_video.mp4" \\\n'
        '  --output "final_with_captions.mp4" \\\n'
        '  --template hype \\\n'
        '  --transcript "captions.srt" \\\n'
        '  --transcript-format srt \\\n'
        '  --lang en --video-quality high'
    )

    pdf.sub_header("pycaps Templates")
    pdf.table_row("Template", "Style & Best Use", header=True)
    pdf.table_row("hype", "Bold animated pop-in - energy/motivational content")
    pdf.table_row("gentle", "Smooth fade-in - cinematic, calm content")
    pdf.table_row("default", "Clean standard captions - any content")

    pdf.sub_header("Caption Writing Tips")
    pdf.bullet("Keep each line to 3-5 words max (pycaps animates word by word)")
    pdf.bullet("Use lowercase for a modern, casual aesthetic")
    pdf.bullet("Time captions to match your clip cuts, not random intervals")
    pdf.bullet("Leave the first clip caption-free (let the visual breathe)")
    pdf.bullet("Use motivational or aspirational language for business content")

    pdf.para_bold("Caption examples we used:")
    captions = [
        '"every empire starts here"', '"deep in the zone"',
        '"execute relentlessly"', '"while they sleep we grind"',
        '"from vision to reality"', '"never stop building"',
    ]
    for c in captions:
        pdf.bullet(c, indent=10)

    # ============================================================
    # SECTION 14: 4 EDIT STYLES
    # ============================================================
    pdf.add_page()
    pdf.section_header("14", "The 4 Edit Styles Explained")

    pdf.sub_header("Style 1: Breakbeat Energy  (25.5 seconds)")
    pdf.para_bold("10 clips with flash cut transitions:")
    clips_v1 = [
        ("0:00-0:02", "Wide opening", "1.2x fast", "No zoom"),
        ("0:03-0:05", "Writing close-up", "0.65x slow-mo", "1.8x zoom left"),
        ("0:07-0:09", "Wide quick shot", "1.5x fast", "No zoom"),
        ("0:10-0:12", "Right person typing", "1.0x normal", "1.6x zoom right"),
        ("0:14-0:16", "Medium pointing", "1.5x fast", "1.3x zoom"),
        ("0:18-0:20", "Wide discussion", "1.3x fast", "No zoom"),
        ("0:22-0:24", "Dramatic pointing up", "0.50x slow-mo", "1.8x zoom"),
        ("0:28-0:30", "Right typing detail", "1.4x fast", "1.6x zoom"),
        ("0:32-0:34", "Wide pitch moment", "1.3x fast", "No zoom"),
        ("0:36-0:39", "Slow zoom finale", "0.55x slow-mo", "1.3x zoom"),
    ]
    pdf.table_row("Timestamp", "Speed  |  Zoom  |  Description", header=True)
    for ts, desc, speed, zoom in clips_v1:
        pdf.table_row(ts, f"{speed}  |  {zoom}  |  {desc}")
    pdf.para("Music: Breakbeat  |  Transitions: White flash cuts  |  Volume: 45%")

    pdf.divider()

    pdf.sub_header("Style 2: Cinematic Epic  (37.9 seconds)")
    pdf.para_bold("7 clips with smooth crossfade transitions:")
    clips_v2 = [
        ("0:00-0:03", "Wide opening", "0.85x slow", "No zoom"),
        ("0:04-0:07", "Extreme slow-mo writing", "0.55x", "1.8x zoom"),
        ("0:10-0:14", "Wide both working", "1.0x normal", "No zoom"),
        ("0:16-0:19", "Slow zoom right person", "0.60x", "1.6x zoom"),
        ("0:22-0:26", "Dramatic slow-mo", "0.50x", "1.8x zoom"),
        ("0:30-0:34", "Wide pitch moment", "0.80x slow", "No zoom"),
        ("0:36-0:40", "Epic slow finale", "0.50x", "1.3x zoom"),
    ]
    pdf.table_row("Timestamp", "Speed  |  Zoom  |  Description", header=True)
    for ts, desc, speed, zoom in clips_v2:
        pdf.table_row(ts, f"{speed}  |  {zoom}  |  {desc}")
    pdf.para("Music: Epic orchestral  |  Transitions: Smooth crossfades  |  Volume: 35%")

    pdf.divider()

    pdf.sub_header("Style 3: Clean Soul  (27.9 seconds)")
    pdf.para_bold("7 clips with smooth crossfade transitions:")
    clips_v3 = [
        ("0:00-0:04", "Wide natural opening", "1.0x normal", "No zoom"),
        ("0:05-0:08", "Gentle zoom left", "0.80x", "1.5x zoom"),
        ("0:10-0:14", "Wide both on laptops", "1.0x normal", "No zoom"),
        ("0:15-0:18", "Gentle zoom right", "0.85x", "1.5x zoom"),
        ("0:22-0:26", "Medium both smooth", "0.75x", "1.3x zoom"),
        ("0:30-0:34", "Wide discussion", "1.0x normal", "No zoom"),
        ("0:36-0:40", "Smooth zoom finale", "0.70x", "1.5x zoom"),
    ]
    pdf.table_row("Timestamp", "Speed  |  Zoom  |  Description", header=True)
    for ts, desc, speed, zoom in clips_v3:
        pdf.table_row(ts, f"{speed}  |  {zoom}  |  {desc}")
    pdf.para("Music: Soul  |  Transitions: Smooth crossfades  |  Volume: 38%")

    # ============================================================
    # SECTION 15: ALL PROMPTS
    # ============================================================
    pdf.add_page()
    pdf.section_header("15", "All Prompts Used (Copy & Paste Ready)")

    pdf.para(
        "Here are the exact prompts I gave Claude Code, in the order I used them. "
        "You can copy and paste these into your own session - just replace file paths."
    )

    prompts = [
        ("Prompt 1: Initial Request",
         "Here is my video file: C:/path/to/video.mp4 - Let me know how you can improve "
         "this video. Add some amazing transitions. Add some music that is royalty-free so "
         "I don't get any copyright. Remove the audio, just the music, slight music, and "
         "add some captions with amazing design, like we are having a business meeting or "
         "working on something cool."),

        ("Prompt 2: Style & Speed Change",
         "I don't like the music. Can you do something more motivational-type music? "
         "Royalty-free. Increase the speed and try to cover the video under 30 seconds."),

        ("Prompt 3: Push For Energy",
         "I don't like these - NO PASSION or ENERGY in your editing. Make it hit harder. "
         "I want zoom punches, speed ramping, flash cuts, something that feels dynamic."),

        ("Prompt 4: Multiple Versions + Fix Brightness",
         "Give me 3 more versions but don't darken the video, it's already too much darker. "
         "I want breakbeat energy with fast cuts, cinematic with dramatic slow-mo and epic "
         "music, and one clean smooth version with soul music."),

        ("Prompt 5: Lead Magnet PDF",
         "Give me a PDF that will include all the prompts, all the procedure summary for "
         "any beginner. I want to pitch that PDF as a lead magnet by uploading this video."),

        ("Prompt 6: Social Media Caption",
         "Save me a social media post caption - what we have done, and comment or DM for "
         "full PDF on how you can use AI to edit videos."),
    ]

    for title, prompt in prompts:
        pdf.sub_header(title)
        pdf.prompt_box(prompt)

    pdf.pro_tip(
        "Notice how the prompts got more specific over iterations. The first was broad: "
        "'add amazing transitions.' The later ones were precise: 'zoom punches, speed "
        "ramping, flash cuts, don't darken.' Specific feedback gets better AI results. "
        "Don't be afraid to push back and iterate - that's how you get great output."
    )

    # ============================================================
    # SECTION 16: SCRIPTS ARCHITECTURE
    # ============================================================
    pdf.add_page()
    pdf.section_header("16", "The Python Scripts Architecture")

    pdf.para(
        "Claude Code generated these scripts automatically from the prompts above. "
        "Here's how they work under the hood."
    )

    pdf.sub_header("Pipeline Architecture")
    pdf.code_block(
        "three_versions.py\n"
        "|\n"
        "|-- process_clips()          # For each clip:\n"
        "|   |-- ffmpeg: trim         # Extract time segment\n"
        "|   |-- ffmpeg: setpts       # Apply speed change\n"
        "|   |-- ffmpeg: crop+scale   # Zoom punch\n"
        "|   |-- ffmpeg: eq+color     # Color grade\n"
        "|\n"
        "|-- create_flash()           # White frame (0.083s)\n"
        "|\n"
        "|-- assemble_with_flash()    # Join: clip+flash+clip\n"
        "|   OR                       #   (concat demuxer)\n"
        "|-- assemble_with_crossfade()# Join with xfade blend\n"
        "|\n"
        "|-- add_music_and_finish()   # Music mix + letterbox\n"
        "|   |-- filter_complex_script# Fades, volume, bars\n"
        "|\n"
        "|-- add_pycaps()             # Animated captions\n"
        "    |-- Generate SRT file\n"
        "    |-- pycaps render"
    )

    pdf.sub_header("Single Clip FFmpeg Command")
    pdf.code_block(
        "ffmpeg -y -i input.mp4 \\\n"
        '  -vf "trim=start=3:end=5.5,\n'
        "       setpts=PTS-STARTPTS,\n"
        "       setpts=PTS/0.65,\n"
        "       crop=1067:600:46:80,\n"
        "       scale=1920:1080:flags=lanczos,\n"
        "       eq=brightness=0.06:contrast=1.15:saturation=0.90,\n"
        "       colorbalance=rs=0.06:gs=0.02:bs=-0.04,\n"
        '       unsharp=5:5:0.5" \\\n'
        "  -an -c:v libx264 -preset fast -crf 16 \\\n"
        "  -pix_fmt yuv420p -r 24000/1001 \\\n"
        "  clip_output.mp4"
    )

    pdf.sub_header("Final Assembly Command")
    pdf.code_block(
        "ffmpeg -y \\\n"
        "  -i assembled.mp4 -i music.mp3 \\\n"
        "  -filter_complex_script final_fg.txt \\\n"
        "  -map [vout] -map [aout] \\\n"
        "  -c:v libx264 -preset medium -crf 17 \\\n"
        "  -c:a aac -b:a 192k \\\n"
        "  -pix_fmt yuv420p -movflags +faststart \\\n"
        "  output.mp4"
    )

    pdf.important_box(
        "On Windows, ALWAYS use -filter_complex_script (write the filtergraph to a .txt file) "
        "instead of inline -filter_complex. Windows command line has escaping issues with "
        "FFmpeg's complex filter expressions. This one tip will save you hours of debugging."
    )

    pdf.sub_header("Get The Full Scripts")
    pdf.para(f"All scripts are on GitHub, ready to clone and run:")
    pdf.code_block(
        f"git clone {GITHUB_URL}.git\n"
        "cd ai-video-editor\n"
        "pip install -r requirements.txt\n"
        "# Edit the VIDEO path in the script, then:\n"
        "python three_versions.py"
    )

    # ============================================================
    # SECTION 17: PRO TIPS
    # ============================================================
    pdf.add_page()
    pdf.section_header("17", "Pro Tips & Common Mistakes")

    tips = [
        ("Don't over-darken your footage",
         "Keep brightness above 0.0 and contrast below 1.25 unless you specifically want "
         "a dark mood. Over-processing makes videos look muddy, especially on phone screens."),
        ("Speed contrast is everything",
         "A fast clip (1.5x) followed by slow-mo (0.5x) creates a visual punch. "
         "Uniform speed = boring. Varying speed = professional."),
        ("Alternate wide and zoomed shots",
         "If every clip is zoomed, viewers lose spatial context. Wide shots establish "
         "the scene, zooms create intimacy. The rhythm between them creates flow."),
        ("Music sets the ceiling",
         "Your edit can only be as good as your music choice. The track tempo should "
         "match your cut rhythm. Cuts landing on the beat feel intentional."),
        ("Less is more with captions",
         "3-5 words per line. No full sentences. Let the visuals tell the story. "
         "Captions should enhance, not distract or overwhelm."),
        ("Iterate with honest feedback",
         "Don't settle for version 1. Tell Claude Code exactly what you don't like. "
         "'Too dark and too slow' is more useful than 'I don't like it.'"),
        ("Use CRF 16-18 for quality",
         "CRF controls video quality: 0 = lossless, 51 = worst. "
         "16-18 is the sweet spot - visually lossless but reasonable file size."),
        ("Letterbox bars add instant production value",
         "Even thin 50-60px black bars at top and bottom make your video look cinematic. "
         "Small trick, big visual impact."),
        ("Always use filter_complex_script on Windows",
         "Write your FFmpeg filtergraph to a .txt file and use -filter_complex_script "
         "instead of inline -filter_complex. This avoids all escaping nightmares."),
        ("Preview on mobile before publishing",
         "Most viewers watch on phones. Text that's readable on a laptop may be too "
         "small on mobile. Always check your final edit on a phone screen."),
    ]

    for i, (title, body) in enumerate(tips, 1):
        pdf._safe_page_check(18)
        pdf.set_font("SegoeSB", "", 10)
        pdf.set_text_color(*ACCENT)
        pdf.set_x(18)
        pdf.cell(8, 6, f"{i}.")
        pdf.set_text_color(*BLACK)
        pdf.cell(0, 6, title)
        pdf.ln(7)
        pdf.para(body)

    # ============================================================
    # SECTION 18: NEXT STEPS
    # ============================================================
    pdf.add_page()
    pdf.section_header("18", "Next Steps & Resources")

    pdf.para(
        "You now have the complete workflow. Here's how to level up and where "
        "to find more resources."
    )

    pdf.sub_header("Level Up Your Edits")
    pdf.numbered_item(1, "Try vertical 9:16 output for Instagram Reels and TikTok Shorts")
    pdf.numbered_item(2, "Use beat detection to auto-sync cuts to the music tempo")
    pdf.numbered_item(3, "Experiment with more aggressive zoom (2.0x+) for extreme close-ups")
    pdf.numbered_item(4, "Add subtle camera shake effects using animated crop offsets")
    pdf.numbered_item(5, "Try AI upscaling with Video2X for higher resolution output")

    pdf.sub_header("Useful GitHub Repositories")
    pdf.table_row("Repository", "What It Does", header=True)
    pdf.table_row("pycaps", "Animated word-by-word captions")
    pdf.table_row("Video2X", "AI video upscaling (increase resolution)")
    pdf.table_row("Practical-RIFE", "AI frame interpolation (smoother slow-mo)")
    pdf.table_row("AudioCraft (Meta)", "AI music generation (make custom tracks)")
    pdf.table_row("faster-whisper", "AI speech-to-text (auto-generate captions)")

    pdf.sub_header("Our Repository")
    pdf.code_block(f"git clone {GITHUB_URL}.git")
    pdf.para(
        "Star the repo, fork it, or submit pull requests. All scripts are open source "
        "and free to use for any purpose."
    )

    pdf.sub_header("FFmpeg Resources")
    pdf.bullet("FFmpeg Documentation: ffmpeg.org/documentation.html")
    pdf.bullet("FFmpeg Wiki: trac.ffmpeg.org (community guides and examples)")
    pdf.bullet("FFmpeg Filters: ffmpeg.org/ffmpeg-filters.html (complete filter reference)")
    pdf.bullet("r/ffmpeg on Reddit (community help and discussion)")

    # ---- CLOSING PAGE ----
    pdf.add_page()
    pdf.ln(30)

    # Dark block
    y = pdf.get_y()
    pdf.set_fill_color(*BLACK)
    pdf.rect(0, y, 210, 80, "F")
    pdf.set_fill_color(*BLUE)
    pdf.rect(20, y + 15, 50, 3, "F")

    pdf.set_y(y + 25)
    pdf.set_font("SegoeSB", "", 24)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 12, "  Ready to Build?", 0, 0, "L")
    pdf.ln(16)
    pdf.set_font("Segoe", "", 12)
    pdf.set_text_color(200, 200, 205)
    pdf.set_x(22)
    pdf.multi_cell(166, 7,
        "Take any video on your phone, open Claude Code, and start with "
        "Prompt 1 from Section 15. You'll have a professional edit in "
        "under 5 minutes. No video editing experience required."
    )

    pdf.set_y(y + 95)
    pdf.set_font("Segoe", "", 10)
    pdf.set_text_color(*DARK_GRAY)
    pdf.cell(0, 8, "Get the scripts:", 0, 0, "C")
    pdf.ln(9)
    pdf.set_font("SegoeSB", "", 11)
    pdf.set_text_color(*BLUE)
    pdf.cell(0, 8, GITHUB_URL, 0, 0, "C")

    pdf.ln(25)
    pdf.set_draw_color(230, 230, 235)
    pdf.line(40, pdf.get_y(), 170, pdf.get_y())
    pdf.ln(10)

    pdf.set_font("SegoeSB", "", 14)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 8, "Waseem Nasir", 0, 0, "C")
    pdf.ln(10)
    pdf.set_font("Segoe", "", 10)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 7, "skynetjoe.com  |  waseemnasir.com", 0, 0, "C")
    pdf.ln(9)
    pdf.set_font("Segoe", "", 9)
    pdf.set_text_color(160, 160, 165)
    pdf.cell(0, 7, "Built with Claude Code + FFmpeg + Python", 0, 0, "C")

    # ---- SAVE ----
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdf.output(OUTPUT_PDF)
    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    pages = pdf.page_no()
    print(f"PDF created: {OUTPUT_PDF}")
    print(f"Pages: {pages} | Size: {size_kb:.0f} KB")


if __name__ == "__main__":
    build_pdf()
