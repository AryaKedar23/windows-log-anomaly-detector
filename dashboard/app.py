from collections import deque
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    last_lines = deque(maxlen=100)  # store only last 100 lines
    
    with open("../samples/synthetic_attack.log", "r") as f:
        for line in f:
            last_lines.append(line.strip())
            
    log_entries = []
    for line in last_lines:
        parts = line.split()
        if len(parts) < 5:
            continue
        timestamp = " ".join(parts[:3])
        host = parts[3]
        process = parts[4]
        message = " ".join(parts[5:])
        log_entries.append([timestamp, host, process, message])

    data = pd.DataFrame(log_entries, columns=["timestamp", "host", "process", "message"])
    logs_html = data.to_html(classes="table table-striped")
    return render_template("dashboard.html", logs=logs_html)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

