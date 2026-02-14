#!/usr/bin/env python3
"""
J EASY SCRIPT RUNNER (UNIVERSAL)
GUI Professional Edition
Created by jh4ck3r
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess

# ======================== UI Configuration ========================
# Dark Theme Colors
COLORS = {
    "bg": "#121212",           # Main Background
    "card": "#1E1E1E",         # Card Background
    "input_bg": "#2D2D2D",     # Input Fields
    "text": "#E0E0E0",         # Standard Text
    
    # Your Branding Colors
    "cyan": "#00FFFF",         # Instructions/Examples
    "magenta": "#FF00FF",      # Headers/Welcome
    "yellow": "#FFFF00",       # Steps
    "green": "#00FF00",        # Success/Credits
    "red": "#FF4500",          # Errors
    "blue": "#00BFFF"          # Info
}

FONTS = {
    "title": ("Segoe UI", 18, "bold"),
    "subtitle": ("Segoe UI", 10),
    "step": ("Segoe UI", 11, "bold"),
    "info": ("Segoe UI", 9),
    "input": ("Consolas", 11),
    "log": ("Consolas", 9)
}

class CustomPasswordDialog(tk.Toplevel):
    """Secure Password Dialog"""
    def __init__(self, parent):
        super().__init__(parent)
        self.password = None
        self.title("Authentication Required")
        self.geometry("400x180")
        self.configure(bg=COLORS["card"])
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        # Center in screen
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        tk.Label(self, text="System Password Required", font=("Segoe UI", 12, "bold"), 
                 bg=COLORS["card"], fg=COLORS["cyan"]).pack(pady=(20, 5))
        
        tk.Label(self, text="sudo permission needed to write to /usr/local/bin", 
                 font=("Segoe UI", 9), bg=COLORS["card"], fg=COLORS["text"]).pack(pady=(0, 15))

        self.entry = tk.Entry(self, show="•", font=FONTS["input"], 
                              bg=COLORS["input_bg"], fg="white", 
                              insertbackground="white", bd=0, relief="flat")
        self.entry.pack(ipady=5, ipadx=5, fill="x", padx=40)
        self.entry.focus_set()
        self.entry.bind("<Return>", self.on_confirm)

        btn_frame = tk.Frame(self, bg=COLORS["card"])
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Cancel", command=self.on_cancel, 
                  bg="#333", fg="white", bd=0, padx=15, pady=5).pack(side="left", padx=10)
        
        tk.Button(btn_frame, text="Authenticate", command=self.on_confirm, 
                  bg=COLORS["magenta"], fg="black", font=("Segoe UI", 9, "bold"), 
                  bd=0, padx=15, pady=5).pack(side="left", padx=10)

        self.wait_window()

    def on_confirm(self, event=None):
        self.password = self.entry.get()
        self.destroy()

    def on_cancel(self):
        self.destroy()

class JWrapperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("J Project Platform - Universal Script Runner")
        self.root.geometry("850x750")
        self.root.configure(bg=COLORS["bg"])

        # --- SCROLLABLE AREA SETUP ---
        self.canvas = tk.Canvas(root, bg=COLORS["bg"], highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = tk.Frame(self.canvas, bg=COLORS["bg"])
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        
        self.scroll_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

        self.create_content()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")

    def create_content(self):
        main_pad = tk.Frame(self.scroll_frame, bg=COLORS["bg"], padx=20, pady=20)
        main_pad.pack(fill="both", expand=True)

        # --- HEADER ---
        header_frame = tk.Frame(main_pad, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(header_frame, text="==============================", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        tk.Label(header_frame, text="J WRAPPER", font=FONTS["title"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        tk.Label(header_frame, text="==============================", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        
        tk.Label(header_frame, text="Created by jh4ck3r", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["green"]).pack(anchor="center", pady=(5,0))
        tk.Label(header_frame, text="J Project Platform.com", font=FONTS["subtitle"], bg=COLORS["bg"], fg="white").pack(anchor="center")

        # --- INTRO ---
        intro_card = tk.Frame(main_pad, bg=COLORS["card"], padx=15, pady=15)
        intro_card.pack(fill="x", pady=10)
        
        tk.Label(intro_card, text="Run ANY script/file from anywhere in the terminal.", 
                 font=("Segoe UI", 11, "bold"), bg=COLORS["card"], fg=COLORS["magenta"]).pack(anchor="w")
        tk.Label(intro_card, text="Supports: Python (.py), Bash (.sh), Perl, Ruby, NodeJS, and Executables.", 
                 font=FONTS["info"], bg=COLORS["card"], fg=COLORS["cyan"]).pack(anchor="w")

        # --- STEP 1 ---
        step1_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step1_frame.pack(fill="x")
        
        tk.Label(step1_frame, text="Step 1: Select your File (Script or Binary)", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step1_frame, text="Example: /home/jproject/tool.py OR /home/user/myscript.sh", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        
        input1_frame = tk.Frame(step1_frame, bg=COLORS["bg"], pady=5)
        input1_frame.pack(fill="x")
        
        self.entry_path = tk.Entry(input1_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_path.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 10))
        
        tk.Button(input1_frame, text="BROWSE", command=self.browse_file, bg="#444", fg="white", bd=0, padx=15, pady=5).pack(side="right")

        # --- STEP 2 ---
        step2_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step2_frame.pack(fill="x")

        tk.Label(step2_frame, text="Step 2: Python Virtualenv Name (Optional)", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step2_frame, text="Only use this if it is a Python script with a specific environment.", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        tk.Label(step2_frame, text="Leave blank for Bash, other languages, or standard Python.", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["text"]).pack(anchor="w")

        self.entry_venv = tk.Entry(step2_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_venv.pack(fill="x", ipady=5, pady=5)

        # --- STEP 3 ---
        step3_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step3_frame.pack(fill="x")

        tk.Label(step3_frame, text="Step 3: Wrapper Name (Short Command)", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step3_frame, text="This is the command you will type in the terminal.", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")

        self.entry_name = tk.Entry(step3_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_name.pack(fill="x", ipady=5, pady=5)

        # --- BUTTON ---
        tk.Button(main_pad, text="CREATE UNIVERSAL WRAPPER", command=self.process, 
                  bg=COLORS["magenta"], fg="black", font=("Segoe UI", 12, "bold"), 
                  bd=0, padx=20, pady=10, cursor="hand2").pack(fill="x", pady=20)

        # --- OUTPUT LOG ---
        tk.Label(main_pad, text="System Output:", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        self.console = scrolledtext.ScrolledText(main_pad, height=10, bg="black", fg=COLORS["green"], 
                                                 font=FONTS["log"], bd=0)
        self.console.pack(fill="both", expand=True, pady=(5, 0))

    # --- LOGIC ---
    def browse_file(self):
        # Updated to accept ALL files
        filename = filedialog.askopenfilename(title="Select Any Script/File", 
                                              filetypes=[("All Files", "*.*")])
        if filename:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, filename)

    def log(self, msg, color=COLORS["green"]):
        self.console.tag_config(color, foreground=color)
        self.console.insert(tk.END, f"{msg}\n", color)
        self.console.see(tk.END)

    def run_sudo_command(self, cmd, password):
        full_cmd = f"echo '{password}' | sudo -S -p '' {cmd}"
        try:
            process = subprocess.Popen(full_cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                err_msg = stderr.decode().strip()
                if "incorrect password" in err_msg.lower():
                    return False, "Incorrect Password"
                return False, f"Error: {err_msg}"
            return True, "Success"
        except Exception as e:
            return False, str(e)

    def process(self):
        script_path = self.entry_path.get().strip()
        venv_name = self.entry_venv.get().strip()
        wrapper_name = self.entry_name.get().strip()

        # Validation
        if not script_path or not os.path.isfile(script_path):
            messagebox.showerror("Error", f"File not found at {script_path}")
            return
        if not wrapper_name:
            messagebox.showerror("Error", "Wrapper name cannot be empty.")
            return

        # Password
        dialog = CustomPasswordDialog(self.root)
        sudo_pass = dialog.password
        if not sudo_pass:
            self.log("Operation cancelled.", COLORS["red"])
            return

        self.log(f"Analyzing file...", COLORS["magenta"])

        # ==========================================
        #  UNIVERSAL WRAPPER GENERATION LOGIC
        # ==========================================
        
        wrapper_content = f"""#!/usr/bin/env bash
# ======================================================
# J-Wrapper for {script_path}
# ======================================================
SCRIPT="{script_path}"
SCRIPT_DIR="$(dirname "$SCRIPT")"
FILENAME="$(basename "$SCRIPT")"
EXTENSION="${{FILENAME##*.}}"

# 1. Navigate to directory (Crucial for relative imports)
cd "$SCRIPT_DIR" || exit 1
"""

        # Logic: If VENV is provided, force Python logic
        if venv_name:
            wrapper_content += f"""
# --- Python Virtualenv Mode ---
if [ -x "$SCRIPT_DIR/{venv_name}/bin/python3" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python3" "$SCRIPT" "$@"
elif [ -x "$SCRIPT_DIR/{venv_name}/bin/python" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python" "$SCRIPT" "$@"
else
  echo "[!] Venv specified but not found. Fallback to system python."
  exec python3 "$SCRIPT" "$@"
fi
"""
        else:
            # Logic: Universal Detection Mode
            wrapper_content += f"""
# --- Universal Auto-Detect Mode ---

case "$EXTENSION" in
    py)
        # Python
        exec python3 "$SCRIPT" "$@"
        ;;
    sh|bash)
        # Bash Script
        exec bash "$SCRIPT" "$@"
        ;;
    js)
        # Node JS
        exec node "$SCRIPT" "$@"
        ;;
    rb)
        # Ruby
        exec ruby "$SCRIPT" "$@"
        ;;
    pl)
        # Perl
        exec perl "$SCRIPT" "$@"
        ;;
    php)
        # PHP
        exec php "$SCRIPT" "$@"
        ;;
    *)
        # Fallback: Executable Binary or Unknown
        # Try to execute directly
        if [ -x "$SCRIPT" ]; then
             exec "$SCRIPT" "$@"
        else
             # Attempt to make executable and run
             # If it fails, fallback to bash if it looks like text
             chmod +x "$SCRIPT" 2>/dev/null
             exec "$SCRIPT" "$@"
        fi
        ;;
esac
"""

        # Write Temp
        temp_file = "/tmp/j_wrapper_temp.sh"
        target_file = f"/usr/local/bin/{wrapper_name}"
        
        try:
            with open(temp_file, "w") as f:
                f.write(wrapper_content)
        except Exception as e:
            self.log(f"File write failed: {e}", COLORS["red"])
            return

        # Move with Sudo
        self.log(f"Installing wrapper to /usr/local/bin/...", COLORS["yellow"])
        success, msg = self.run_sudo_command(f"mv {temp_file} {target_file}", sudo_pass)
        if not success:
            self.log(f"Failed to move file: {msg}", COLORS["red"])
            return

        success, msg = self.run_sudo_command(f"chmod +x {target_file}", sudo_pass)
        if not success:
            self.log(f"Failed to chmod: {msg}", COLORS["red"])
            return

        # Final Success Message
        self.log(f"\n✅ Wrapper '{wrapper_name}' created successfully!", COLORS["green"])
        self.log(f"File Type Handled: Universal", COLORS["blue"])
        self.log(f"\nHow to use:", COLORS["cyan"])
        self.log(f"   Command: {wrapper_name} [args]", COLORS["cyan"])
        
        self.log(f"\nEnjoy with J Project Platform!", COLORS["magenta"])
        
        messagebox.showinfo("Success", f"Wrapper '{wrapper_name}' created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JWrapperApp(root)
    root.mainloop()
