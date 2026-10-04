#!/bin/bash
# 부팅 시 launcher.py 자동 실행 등록

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AUTOSTART_DIR="$HOME/.config/autostart"
DESKTOP_FILE="$AUTOSTART_DIR/boot-launcher.desktop"

mkdir -p "$AUTOSTART_DIR"

cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=Boot Launcher
Exec=python3 $SCRIPT_DIR/launcher.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
EOF

echo "자동 실행 등록 완료: $DESKTOP_FILE"
echo "다음 부팅부터 launcher.py 가 자동으로 실행됩니다."
