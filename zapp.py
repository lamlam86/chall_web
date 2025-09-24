import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

BLACKLIST = ["sh", "rm", "echo", "flag", "d_flag_o_day_ne.txt", "d_flag_o_day_ne", "tac", "more", "less", "head", "tail","ln","nl","pr"]
import os, threading, time, shutil
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

ALLOWED = {
    "zapp.py",
    "templates",
    "static",
    "d_flag_o_day_ne.txt",
    "zDockerfile",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".git",
    "README.md",

}

def cleaner():
    """Xóa file/folder lạ mỗi 20 giây"""
    while True:
        for f in os.listdir("."):
            if f not in ALLOWED:
                try:
                    if os.path.isfile(f):
                        os.remove(f)
                        print(f"[Cleaner] Deleted file: {f}")
                    elif os.path.isdir(f):
                        shutil.rmtree(f)
                        print(f"[Cleaner] Deleted folder: {f}")
                except Exception as e:
                    print(f"[Cleaner] Không xóa được {f}: {e}")
        time.sleep(20)
threading.Thread(target=cleaner, daemon=True).start()
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    cmd = ""
    if request.method == "POST":
        cmd = request.form.get("cmd", "")
        if len(cmd) > 4:
            output = "bạn muốn làm hacker ???"
        elif any(bad in cmd for bad in BLACKLIST):
            output = "bạn muốn làm hacker ???"
        else:
            try:
                result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output = result.stdout.decode("utf-8", errors="ignore")
                if not output.strip():
                    output = "(không có output)"
            except Exception as e:
                output = f"Lỗi: {e}"

    return render_template("index.html", output=output, cmd=cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=False)
