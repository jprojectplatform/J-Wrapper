# 🚀 **J-Wrapper: Universal Script Execution Engine**

<div align="center">
  
  ![J-Wrapper Banner](https://i.imgur.com/WxSdDFJ.png)
  
  [![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/jprojectplatform/J-Wrapper)
  [![Python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)](https://python.org)
  [![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Kali%20%7C%20Ubuntu-brightgreen.svg)](https://www.kali.org/)
  [![License](https://img.shields.io/badge/license-JPL-red.svg)](LICENSE)
  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/jprojectplatform)
  [![Made by](https://img.shields.io/badge/made%20by-jh4ck3r-ff69b4.svg)](https://portfolio.jprojectplatform.com/)
  
  **Run ANY script from ANYWHERE in your terminal - One Command to Rule Them All!**
  
  [Installation](#-quick-installation) • [Features](#-features) • [Usage](#-how-to-use) • [Demo](#-video-demo) • [Documentation](#-documentation)
  
</div>

---

## 💫 **What is J-Wrapper?**

**J-Wrapper** is a revolutionary **Universal Script Execution Engine** that liberates you from the constraints of directory navigation. With its sleek professional GUI, you can transform any script into a global terminal command in seconds!

### 🎯 **The Problem We Solve**

```bash
# Without J-Wrapper - The Nightmare 😱
cd /home/user/Downloads/tools/hacking/scripts/python/venv/bin
source activate
python3 my_tool.py --complex --arguments here
cd ../../../../..

# With J-Wrapper - The Dream ✨
my-tool --complex --arguments here
```

---

## ✨ **Features**

### 🎨 **Professional GUI Interface**
- **Sleek Dark Theme** - Easy on the eyes during late-night sessions
- **Real-time Console Output** - Watch every step of the process
- **Smart Scrolling** - Smooth navigation through logs
- **Password Dialog** - Secure sudo authentication

### 🔧 **Universal Language Support**

| Language | Extension | Auto-Detection | VirtualEnv Support |
|----------|-----------|----------------|-------------------|
| **Python** | `.py` | ✅ | ✅ |
| **Bash** | `.sh`, `.bash` | ✅ | ❌ |
| **Node.js** | `.js` | ✅ | ❌ |
| **Ruby** | `.rb` | ✅ | ❌ |
| **Perl** | `.pl` | ✅ | ❌ |
| **PHP** | `.php` | ✅ | ❌ |
| **Binary** | Any executable | ✅ | ❌ |

### 🚀 **Smart Auto-Detection**
- **Intelligent file type recognition** based on extension
- **Automatic shebang detection** for extensionless scripts
- **Fallback execution** strategies for unknown types
- **Virtual environment activation** for Python projects

---

## 📦 **Quick Installation**

### **Method 1: One-Line Install (Recommended)**
```bash
git clone https://github.com/jprojectplatform/J-Wrapper.git
cd J-Wrapper
python3 j-wrapper.py
```

### **Method 2: Manual Setup**
```bash
# Clone the repository
git clone https://github.com/jprojectplatform/J-Wrapper.git
cd J-Wrapper

# No dependencies needed! Just Python 3.8+
python3 j-wrapper.py
```



## 🎮 **How To Use**

### **Step-by-Step Guide**

#### **1️⃣ Launch J-Wrapper**
```bash
python3 j-wrapper.py
```
*The professional GUI will appear with your branding colors.*

#### **2️⃣ Select Your Script**
- Click **BROWSE** to navigate to any script
- Supports all file types: `.py`, `.sh`, `.js`, `.rb`, `.pl`, `.php`, binaries
- Example: `/home/user/tools/my-hacking-tool.py`

#### **3️⃣ Configure (Optional)**
- **Python Virtualenv Name**: If using Python with venv, specify the environment name
- **Wrapper Name**: The global command you want (e.g., `my-tool`, `scan`, `hack`)

#### **4️⃣ Create & Enjoy!**
- Click **CREATE UNIVERSAL WRAPPER**
- Enter sudo password when prompted
- Done! Now use your tool from anywhere!

---

## 🌟 **Real-World Examples**

### **Example 1: Python Hacking Tool with VirtualEnv**
```bash
# Before J-Wrapper
cd /opt/tools/recon-tool
source venv/bin/activate
python3 recon.py --target example.com --ports 1-1000
deactivate

# After J-Wrapper
recon --target example.com --ports 1-1000
```

### **Example 2: Bash Automation Script**
```bash
# Before J-Wrapper
cd ~/scripts/backup
./backup-system.sh --full --destination /mnt/backup

# After J-Wrapper
backup-system --full --destination /mnt/backup
```

### **Example 3: Node.js Tool**
```bash
# Before J-Wrapper
cd /home/user/tools/api-tester
node tester.js --url https://api.example.com

# After J-Wrapper
api-tester --url https://api.example.com
```

---

## 🎨 **GUI Showcase**

### **Main Interface**
```
┌─────────────────────────────────────────────┐
│   ==============================             │
│          J WRAPPER                           │
│   ==============================             │
│   Created by jh4ck3r                         │
│   J Project Platform.com                     │
│                                              │
│   Run ANY script/file from anywhere...       │
│                                              │
│   Step 1: Select your File                   │
│   ┌──────────────────────────────────┐ [BROWSE]
│   │ /home/user/tools/myscript.py    │        │
│                                              │
│   Step 2: Python Virtualenv Name (Optional)  │
│   ┌──────────────────────────────────┐       │
│   │ myenv                            │       │
│                                              │
│   Step 3: Wrapper Name (Short Command)       │
│   ┌──────────────────────────────────┐       │
│   │ myscript                          │       │
│                                              │
│   [CREATE UNIVERSAL WRAPPER]                  │
└─────────────────────────────────────────────┘
```

### **Authentication Dialog**
```
┌─────────────────────────────────────────────┐
│         Authentication Required              │
│                                              │
│   System Password Required                   │
│   sudo permission needed to write...         │
│                                              │
│   ┌──────────────────────────────────┐       │
│   │ •••••••••••                      │       │
│                                              │
│   [Cancel]                    [Authenticate] │
└─────────────────────────────────────────────┘
```

---

## 📁 **Generated Wrapper Structure**

When you create a wrapper, J-Wrapper generates an intelligent script:

```bash
#!/usr/bin/env bash
# ======================================================
# J-Wrapper for /home/user/tools/myscript.py
# ======================================================
SCRIPT="/home/user/tools/myscript.py"
SCRIPT_DIR="$(dirname "$SCRIPT")"
FILENAME="$(basename "$SCRIPT")"
EXTENSION="${FILENAME##*.}"

# 1. Navigate to directory (Crucial for relative imports)
cd "$SCRIPT_DIR" || exit 1

# --- Universal Auto-Detect Mode ---
case "$EXTENSION" in
    py)
        # Python with optional venv
        if [ -n "$VENV_NAME" ] && [ -d "$VENV_NAME" ]; then
            source "$VENV_NAME/bin/activate"
            python3 "$SCRIPT" "$@"
            deactivate
        else
            python3 "$SCRIPT" "$@"
        fi
        ;;
    sh|bash)
        exec bash "$SCRIPT" "$@"
        ;;
    js)
        exec node "$SCRIPT" "$@"
        ;;
    *)
        exec "$SCRIPT" "$@"
        ;;
esac
```

---

## 🛠️ **Advanced Features**

### **Wrapper Management**
```bash
# List all J-Wrappers
ls -la /usr/local/bin/ | grep -v "^total"

# Remove a wrapper
sudo rm /usr/local/bin/wrapper-name

# Update a wrapper
# Simply run j-wrapper.py again with same name
```

### **Debug Mode**
```bash
# Run wrapper with debug output
DEBUG=1 your-wrapper --args

# View wrapper content
cat /usr/local/bin/your-wrapper
```

### **Custom VirtualEnv Paths**
```bash
# Specify full venv path
# In Step 2, enter: /full/path/to/venv
```

---

## 📺 **Video Demo**

[![J-Wrapper Demo](https://i.imgur.com/AlnOojr.jpeg)](https://youtu.be/@jprojectplatform)

*Click the image above to watch the complete tutorial*

---

## 🔧 **Troubleshooting**

### **Common Issues & Solutions**

| Issue | Solution |
|-------|----------|
| **"Permission denied"** | Ensure sudo password is correct |
| **"Command not found"** | Check if `/usr/local/bin` is in your PATH |
| **Python venv not found** | Verify venv name and path |
| **Script won't execute** | Check file permissions: `chmod +x script` |
| **GUI won't open** | Install tkinter: `sudo apt install python3-tk` |

### **PATH Configuration**
```bash
# Add to ~/.bashrc if /usr/local/bin not in PATH
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc
```

---

## 🎯 **Use Cases**

### **For Penetration Testers**
- Create global commands for your custom tools
- Quickly access scripts from any directory
- Maintain tool organization without path headaches

### **For Developers**
- Run project-specific tools globally
- Share scripts with team members easily
- Standardize command names across projects

### **For System Administrators**
- Create admin utility shortcuts
- Manage backup scripts from anywhere
- Automate maintenance tasks

---

## 📊 **Performance Metrics**

| Feature | Performance |
|---------|------------|
| **Wrapper Creation** | < 2 seconds |
| **Command Execution** | Instant (no delay) |
| **Memory Footprint** | < 50MB |
| **Supported Languages** | 7+ |
| **Max Script Size** | Unlimited |

---

## 🤝 **Integration Ecosystem**

J-Wrapper seamlessly integrates with all **J Project Platform** tools:

- 🔍 [J-Proxies-Scanner](https://github.com/jprojectplatform/J-Proxies-Scanner) - Proxy validation tool
- 🛡️ [J-Anonymous](https://github.com/jprojectplatform/J-Anonymous) - Network privacy toolkit
- 🔧 And More tools

---


### **Quick Reference**
- **Create wrapper:** `python3 j-wrapper.py`
- **Use wrapper:** `your-command [args]`
- **List wrappers:** `ls /usr/local/bin/`
- **Remove wrapper:** `sudo rm /usr/local/bin/name`


## 🔒 **Security Features**

- **Secure Password Handling** - Custom password dialog with masking
- **Sudo Authentication** - Proper privilege escalation
- **File Integrity** - Maintains original script permissions
- **No Data Leakage** - All processing done locally
- **Clean Installation** - Only writes to `/usr/local/bin/`

---

## 🌟 **Why Choose J-Wrapper?**

| Feature | J-Wrapper | Manual Aliases | Other Tools |
|---------|-----------|----------------|--------------|
| **GUI Interface** | ✅ Professional | ❌ | ⚠️ Limited |
| **VirtualEnv Support** | ✅ Built-in | ❌ | ❌ |
| **Auto-Detection** | ✅ Smart | ❌ | ⚠️ Basic |
| **Multi-Language** | ✅ 7+ | ⚠️ Manual | ✅ 3-4 |
| **Password Security** | ✅ Custom Dialog | ❌ | ❌ |
| **Directory Handling** | ✅ Automatic | ⚠️ Manual | ⚠️ Partial |
| **J-Project Integration** | ✅ Native | ❌ | ❌ |

---

## 💖 **Support & Community**

### **Join Our Community**
- **Telegram:** [@JProjectPlatform](https://t.me/jprojectplatform)
- **Email:** info@jprojectplatform.com

### **Contribute**
- ⭐ Star this repository
- 🐛 Report bugs via Issues
- 🔧 Submit Pull Requests
- 📝 Improve documentation
- 💡 Suggest new features

---


## 📜 **License**

This project is licensed under the **J Project License (JPL)**.

**Terms of Use:**
- ✅ Free for personal and educational use
- ✅ Modify and adapt for your needs
- ✅ Share with attribution
- ❌ Commercial use without permission
- ❌ Redistribution without license
- ❌ Claim as your own work

---

## 👨‍💻 **About The Creator**

**jh4ck3r** - Security Researcher & Developer
- 🔭 Creator of **J Project Platform**
- 🌐 [Portfolio](https://portfolio.jprojectplatform.com)
---

## 🙏 **Acknowledgments**

- **J Project Platform Community** - For continuous support
- **Open Source Contributors** - For making this possible
- **Security Researchers** - For inspiration and feedback

---

<div align="center">
  
### **Built with 💙 by [J Project Platform](https://jprojectplatform.com)**

**"Hands With Universal Technology"**

[Website](https://jprojectplatform.com) 

---

**© J Project Platform. All rights reserved.**


---

⭐ **If you find J-Wrapper useful, please consider giving it a star!** ⭐

</div>
