# 📂 Project: The Cleanup Crew - Automated File Organizer

A real-time, event-driven Python automation script designed to monitor a target directory (such as a chaotic `Downloads` folder) and automatically categorize incoming files into structured subdirectories based on their file extensions.

---

## 🛠️ System Architecture & Workflow

The script leverages an asynchronous, event-driven approach rather than resource-heavy polling loops:

1. **Active Monitoring (`watchdog`):** 
    The script initializes an `Observer` thread that interfaces directly with the Operating System's file system API to listen for `on_created` events within the source directory.

2. **Extension Parsing (`os.path`):** 
    Upon file detection, the script isolates the file extension using path-splitting utilities and evaluates it against a predefined structural map (`dir_tree`).

3. **File I/O Guardrails & Relocation (`shutil`):** 
    * A 3-second delay (`time.sleep(3)`) is introduced to ensure the file has completed downloading and is no longer locked by the browser or system.
    * The script checks for the existence of the destination category folder, creates it dynamically if missing (`os.makedirs`), and safely transfers the file (`shutil.move`).

---

## 🌲 Directory Mapping Strategy

Files are automatically routed into the following subfolders based on their extensions:

* 🖼️ **Image_Files:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.jfif`
* 🎬 **Video_Files:** `.mpg`, `.mp2`, `.mpeg`, `.mpe`, `.mpv`, `.mp4`, `.m4p`, `.m4v`, `.avi`, `.mov`
* 📄 **Document_Files:** `.ppt`, `.xls`, `.csv`, `.pdf`, `.txt`
* ⚙️ **Setup_Files:** `.exe`, `.bin`, `.cmd`, `.msi`, `.dmg`

---

## 🚀 Setup & Execution

### Prerequisites
The script relies on the third-party `watchdog` library for file system monitoring. Install it via:

```bash
   pip install watchdog
*Run it through command prompt.


---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE). Feel free to fork, modify, and use it for your own directory cleanup needs!

---

<p align="center">
  🚀 <b>Built by a junior polyglot</b><br>
  <sub>Learning & Embarking on new Endeavours</sub>
</p>
