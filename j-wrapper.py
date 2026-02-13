#!/usr/bin/env python3
"""
J EASY SCRIPT RUNNER
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
        self.root.title("J Project Platform - Script Runner")
        self.root.geometry("850x750")
        self.root.configure(bg=COLORS["bg"])

        # --- SCROLLABLE AREA SETUP ---
        # 1. Canvas
        self.canvas = tk.Canvas(root, bg=COLORS["bg"], highlightthickness=0)
        
        # 2. Scrollbar
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        
        # 3. Frame inside Canvas (The Scrollable Frame)
        self.scroll_frame = tk.Frame(self.canvas, bg=COLORS["bg"])

        # 4. Link Canvas Window
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        # 5. Configure Scrolling
        self.scroll_frame.bind(
            "<Configure>",
            self.on_frame_configure
        )
        self.canvas.bind(
            "<Configure>",
            self.on_canvas_configure
        )
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 6. Pack (Layout)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add mousewheel scrolling support
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel) # Windows
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)   # Linux Scroll Up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)   # Linux Scroll Down

        self.create_content()

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        """When canvas resizes, resize the inner frame to match width"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def _on_mousewheel(self, event):
        """Enable mouse scrolling"""
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")

    def create_content(self):
        # Add padding inside the scroll frame
        main_pad = tk.Frame(self.scroll_frame, bg=COLORS["bg"], padx=20, pady=20)
        main_pad.pack(fill="both", expand=True)

        # --- HEADER (CENTERED) ---
        header_frame = tk.Frame(main_pad, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(header_frame, text="==============================", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        tk.Label(header_frame, text="J WRAPPER", font=FONTS["title"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        tk.Label(header_frame, text="==============================", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="center")
        
        tk.Label(header_frame, text="Created by jh4ck3r", font=FONTS["subtitle"], bg=COLORS["bg"], fg=COLORS["green"]).pack(anchor="center", pady=(5,0))
        tk.Label(header_frame, text="J Project Platform Meet: https://jprojectplatform.com", font=FONTS["subtitle"], bg=COLORS["bg"], fg="white").pack(anchor="center")
        tk.Label(header_frame, text="Enjoy With J Project Platform", font=FONTS["subtitle"], bg=COLORS["bg"], fg="white").pack(anchor="center")

        # --- INTRO ---
        intro_card = tk.Frame(main_pad, bg=COLORS["card"], padx=15, pady=15)
        intro_card.pack(fill="x", pady=10)
        
        tk.Label(intro_card, text="Welcome! This tool will help you create a wrapper for your Python scripts.", 
                 font=("Segoe UI", 11, "bold"), bg=COLORS["card"], fg=COLORS["magenta"]).pack(anchor="w")
        tk.Label(intro_card, text="A wrapper lets you run your script from anywhere in the terminal using a short command.", 
                 font=FONTS["info"], bg=COLORS["card"], fg=COLORS["cyan"]).pack(anchor="w")
        tk.Label(intro_card, text="You do NOT need to manually activate virtualenv (venv) if your script has one.", 
                 font=FONTS["info"], bg=COLORS["card"], fg=COLORS["cyan"]).pack(anchor="w")

        # --- STEP 1 ---
        step1_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step1_frame.pack(fill="x")
        
        tk.Label(step1_frame, text="Step 1: Enter the full path to your Python script", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step1_frame, text="Example: /home/jproject/me.py", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        tk.Label(step1_frame, text="This should be the full absolute path to your script, not relative path.", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        
        input1_frame = tk.Frame(step1_frame, bg=COLORS["bg"], pady=5)
        input1_frame.pack(fill="x")
        
        self.entry_path = tk.Entry(input1_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_path.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 10))
        
        tk.Button(input1_frame, text="BROWSE", command=self.browse_file, bg="#444", fg="white", bd=0, padx=15, pady=5).pack(side="right")

        # --- STEP 2 ---
        step2_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step2_frame.pack(fill="x")

        tk.Label(step2_frame, text="Step 2: Enter the virtualenv folder name (if your script has one)", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step2_frame, text="Example: j-env", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        tk.Label(step2_frame, text="If your script does NOT have a venv, just press Enter (leave blank).", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")

        self.entry_venv = tk.Entry(step2_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_venv.pack(fill="x", ipady=5, pady=5)

        # --- STEP 3 ---
        step3_frame = tk.Frame(main_pad, bg=COLORS["bg"], pady=10)
        step3_frame.pack(fill="x")

        tk.Label(step3_frame, text="Step 3: Enter the wrapper name (short command to run your script)", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["yellow"]).pack(anchor="w")
        tk.Label(step3_frame, text="Example: me", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        tk.Label(step3_frame, text="This will be the command you type in terminal to run your script from anywhere.", font=FONTS["info"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")

        self.entry_name = tk.Entry(step3_frame, font=FONTS["input"], bg=COLORS["input_bg"], fg="white", insertbackground="white", bd=0)
        self.entry_name.pack(fill="x", ipady=5, pady=5)

        # --- BUTTON ---
        tk.Button(main_pad, text="CREATE WRAPPER", command=self.process, 
                  bg=COLORS["magenta"], fg="black", font=("Segoe UI", 12, "bold"), 
                  bd=0, padx=20, pady=10, cursor="hand2").pack(fill="x", pady=20)

        # --- OUTPUT LOG ---
        tk.Label(main_pad, text="System Output:", font=FONTS["step"], bg=COLORS["bg"], fg=COLORS["cyan"]).pack(anchor="w")
        self.console = scrolledtext.ScrolledText(main_pad, height=10, bg="black", fg=COLORS["green"], 
                                                 font=FONTS["log"], bd=0)
        self.console.pack(fill="both", expand=True, pady=(5, 0))

    # --- LOGIC ---
    def browse_file(self):
        filename = filedialog.askopenfilename(title="Select Python Script")
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
            messagebox.showerror("Error", f"Script not found at {script_path}")
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

        self.log(f"Creating wrapper...", COLORS["magenta"])

        # Content
        wrapper_content = f"""#!/usr/bin/env bash
# ======================================================
# Wrapper for {script_path}
# Created using J Easy Script Runner
# ======================================================
SCRIPT="{script_path}"
SCRIPT_DIR="$(dirname "$SCRIPT")"
cd "$SCRIPT_DIR" || exit 1
"""
        if venv_name:
            wrapper_content += f"""
if [ -x "$SCRIPT_DIR/{venv_name}/bin/python3" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python3" "$SCRIPT" "$@"
elif [ -x "$SCRIPT_DIR/{venv_name}/bin/python" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python" "$SCRIPT" "$@"
else
  exec python3 "$SCRIPT" "$@"
fi"""
        else:
            wrapper_content += 'exec python3 "$SCRIPT" "$@"\n'

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
        success, msg = self.run_sudo_command(f"mv {temp_file} {target_file}", sudo_pass)
        if not success:
            self.log(f"Failed to move file: {msg}", COLORS["red"])
            return

        success, msg = self.run_sudo_command(f"chmod +x {target_file}", sudo_pass)
        if not success:
            self.log(f"Failed to chmod: {msg}", COLORS["red"])
            return

        # Final Success Message (Original Text)
        self.log(f"\n✅ Wrapper created successfully at: {target_file}", COLORS["green"])
        self.log(f"\nHow to use:", COLORS["blue"])
        self.log(f"1. Open any terminal.", COLORS["cyan"])
        self.log(f"2. Type the wrapper command: {wrapper_name}", COLORS["cyan"])
        self.log(f"   Example: {wrapper_name}", COLORS["cyan"])
        self.log(f"3. If your script takes arguments, you can pass them after the command:", COLORS["cyan"])
        self.log(f"   Example: {wrapper_name} arg1 arg2 arg3", COLORS["cyan"])
        
        if venv_name:
            self.log(f"\nNote: The wrapper automatically uses your virtualenv '{venv_name}' if it exists.", COLORS["yellow"])
        else:
            self.log(f"\nNote: The wrapper uses system python3 since no venv was specified.", COLORS["yellow"])

        self.log(f"\nTip: Keep your script and venv folder in one place for easy management.", COLORS["green"])
        self.log(f"Enjoy with J Project Platform!", COLORS["magenta"])
        
        messagebox.showinfo("Success", f"Wrapper '{wrapper_name}' created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JWrapperApp(root)
    root.mainloop()
