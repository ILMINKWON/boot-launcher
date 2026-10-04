# Boot Launcher

A lightweight Python app that automatically launches on boot/reboot and opens your saved YouTube URLs in Chrome with a simple GUI.

---

## Features

- GUI window appears automatically on every boot/reboot
- Select which YouTube URLs to open via checkboxes
- Add or remove URLs directly from the GUI
- Zero external dependencies — built entirely with Python's standard library

---

## File Structure

```
boot-launcher/
├── launcher.py          # Main program
├── config.json          # URL storage
└── setup_autostart.sh   # Autostart registration script
```

### File Roles

**`launcher.py` — Main Program**
The GUI window that launches on boot. Displays your saved YouTube URLs as checkboxes. Check the ones you want → click "Open Selected" and they open in Chrome. You can also add or remove URLs from this window.

**`config.json` — URL Storage**
Acts as a simple database. Stores all your saved YouTube URLs and their display names. You never need to edit this file manually — `launcher.py` reads and writes to it automatically whenever you add or remove a URL.

**`setup_autostart.sh` — Autostart Registration**
Run this script once and it creates a `.desktop` entry in `~/.config/autostart/`. Linux reads this folder on every boot and automatically launches any registered programs — so `launcher.py` starts up without you doing anything.

---

## Setup

**1. Register autostart (run once)**
```bash
bash setup_autostart.sh
```

**2. That's it.** From the next boot/reboot, the launcher opens automatically.

---

## Usage

- **Check** the URLs you want to open
- Click **"Open Selected"** → URLs open in Chrome, window closes
- Click **"Add URL"** → enter a name and URL to save it
- Click **"Delete Selected"** → removes checked items from the list

---

## Why Python?

| Feature | Reason |
|---|---|
| `tkinter` built-in | GUI library included with Python — no install needed |
| `webbrowser` built-in | Opens URLs in the default browser out of the box |
| `json` built-in | Read/write config files with no extra packages |
| Short code | Same functionality in Java or C++ would be 3–4x longer |
| Fully offline | No external libraries required — works without internet |

---

## Requirements

- Python 3.x
- Linux with GNOME (or any desktop environment that supports `~/.config/autostart`)
