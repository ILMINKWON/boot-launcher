import json
import tkinter as tk
from tkinter import simpledialog, messagebox
import webbrowser
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"youtube_urls": []}
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("부팅 런처")
        self.root.geometry("480x380")
        self.root.resizable(False, False)
        self.config = load_config()
        self.vars = []
        self.build_ui()

    def build_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.vars = []

        tk.Label(self.root, text="YouTube 자동 실행", font=("Arial", 14, "bold")).pack(pady=12)

        list_frame = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        if not self.config["youtube_urls"]:
            tk.Label(list_frame, text="등록된 URL이 없습니다.", fg="gray").pack(pady=20)
        else:
            for item in self.config["youtube_urls"]:
                var = tk.BooleanVar(value=True)
                row = tk.Frame(list_frame)
                row.pack(fill=tk.X, padx=8, pady=3)
                tk.Checkbutton(row, text=item["name"], variable=var, anchor="w", width=30).pack(side=tk.LEFT)
                tk.Label(row, text=item["url"][:40] + "..." if len(item["url"]) > 40 else item["url"],
                         fg="gray", font=("Arial", 8)).pack(side=tk.LEFT)
                self.vars.append((var, item))

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=14)

        tk.Button(btn_frame, text="선택 열기", command=self.open_selected,
                  bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="URL 추가", command=self.add_url,
                  width=10).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="선택 삭제", command=self.remove_selected,
                  width=10).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="닫기", command=self.root.destroy,
                  width=10).grid(row=0, column=3, padx=5)

    def open_selected(self):
        selected = [item for var, item in self.vars if var.get()]
        if not selected:
            messagebox.showwarning("알림", "선택된 URL이 없습니다.")
            return
        for item in selected:
            webbrowser.open(item["url"])
        self.root.destroy()

    def add_url(self):
        name = simpledialog.askstring("URL 추가", "이름을 입력하세요:\n(예: 로파이 음악)")
        if not name:
            return
        url = simpledialog.askstring("URL 추가", "YouTube URL을 입력하세요:")
        if not url:
            return
        self.config["youtube_urls"].append({"name": name, "url": url})
        save_config(self.config)
        self.build_ui()

    def remove_selected(self):
        self.config["youtube_urls"] = [item for var, item in self.vars if not var.get()]
        save_config(self.config)
        self.build_ui()


if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()
