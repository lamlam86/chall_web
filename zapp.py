import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    cmd = ""
    if request.method == "POST":
        cmd = request.form.get("cmd", "")
        if len(cmd) > 4:
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
