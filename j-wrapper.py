#!/usr/bin/env python3
"""
J Easy Script Runner
Created by jh4ck3r
J Project Platform Meet: https://jprojectplatform.com
Enjoy With J Project Platform
"""

import os

# ======================== Terminal Colors ========================
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

def print_banner():
    print(f"\n{BOLD}{CYAN}==============================")
    print(f"{BOLD}{CYAN}       J EASY SCRIPT RUNNER")
    print(f"{BOLD}{CYAN}=============================={RESET}\n")
    print(f"{GREEN}Created by jh4ck3r")
    print("J Project Platform Meet: https://jprojectplatform.com")
    print("Enjoy With J Project Platform\n" + RESET)

def main():
    print_banner()
    
    print(f"{BOLD}{MAGENTA}Welcome! This tool will help you create a wrapper for your Python scripts.{RESET}")
    print(f"{CYAN}A wrapper lets you run your script from anywhere in the terminal using a short command.")
    print(f"{CYAN}You do NOT need to manually activate virtualenv (venv) if your script has one.\n")
    
    print(f"{YELLOW}Step 1: Enter the full path to your Python script{RESET}")
    print(f"{CYAN}Example: /home/jproject/me.py")
    print(f"{CYAN}This should be the full absolute path to your script, not relative path.\n")
    
    script_path = input(f"{YELLOW}Enter full path to your Python script: {RESET}").strip()
    while not os.path.isfile(script_path):
        print(f"{RED}Error: Script not found at {script_path}{RESET}")
        script_path = input(f"{YELLOW}Please enter a valid path (example: /home/jproject/me.py): {RESET}").strip()
    
    print(f"\n{YELLOW}Step 2: Enter the virtualenv folder name (if your script has one){RESET}")
    print(f"{CYAN}Example: j-env")
    print(f"{CYAN}If your script does NOT have a venv, just press Enter.\n")
    
    venv_name = input(f"{YELLOW}Enter virtualenv folder name (or leave blank if none): {RESET}").strip()
    
    print(f"\n{YELLOW}Step 3: Enter the wrapper name (short command to run your script){RESET}")
    print(f"{CYAN}Example: me")
    print(f"{CYAN}This will be the command you type in terminal to run your script from anywhere.\n")
    
    wrapper_name = input(f"{YELLOW}Enter the wrapper name (command to run script): {RESET}").strip()
    while not wrapper_name:
        print(f"{RED}Wrapper name cannot be empty.{RESET}")
        wrapper_name = input(f"{YELLOW}Enter wrapper name (example: me): {RESET}").strip()
    
    wrapper_path = f"/usr/local/bin/{wrapper_name}"
    
    print(f"\n{BOLD}{MAGENTA}Creating wrapper...{RESET}")
    
    # Step 4: Prepare wrapper content
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
        wrapper_content += f"""# Try python3 in virtualenv {venv_name}
if [ -x "$SCRIPT_DIR/{venv_name}/bin/python3" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python3" "$SCRIPT" "$@"
elif [ -x "$SCRIPT_DIR/{venv_name}/bin/python" ]; then
  exec "$SCRIPT_DIR/{venv_name}/bin/python" "$SCRIPT" "$@"
else
  exec python3 "$SCRIPT" "$@"
fi
"""
    else:
        wrapper_content += 'exec python3 "$SCRIPT" "$@"\n'

    # Step 5: Write wrapper
    temp_file = "/tmp/wrapper_temp.sh"
    with open(temp_file, "w") as f:
        f.write(wrapper_content)

    os.system(f"sudo mv {temp_file} {wrapper_path}")
    os.system(f"sudo chmod +x {wrapper_path}")
    
    # Step 6: Instructions & Examples
    print(f"\n{GREEN}✅ Wrapper created successfully at: {wrapper_path}{RESET}")
    print(f"\n{BOLD}{BLUE}How to use:{RESET}")
    print(f"{CYAN}1. Open any terminal.")
    print(f"{CYAN}2. Type the wrapper command: {wrapper_name}")
    print(f"{CYAN}   Example: {wrapper_name}")
    print(f"{CYAN}3. If your script takes arguments, you can pass them after the command:")
    print(f"{CYAN}   Example: {wrapper_name} arg1 arg2 arg3")
    
    if venv_name:
        print(f"\n{YELLOW}Note:{RESET} The wrapper automatically uses your virtualenv '{venv_name}' if it exists.")
    else:
        print(f"\n{YELLOW}Note:{RESET} The wrapper uses system python3 since no venv was specified.")
    
    print(f"\n{GREEN}Tip: Keep your script and venv folder in one place for easy management.{RESET}")
    print(f"{BOLD}{MAGENTA}Enjoy with J Project Platform!\n{RESET}")

if __name__ == "__main__":
    main()
