from flask import Flask
app = Flask(__name__)

VERSION = "v3"
COLOR = "#25fffb"

@app.route("/")
def home():
    return f"""<body style="font-family:sans-serif;text-align:center;margin-top:20vh;background:{COLOR};color:white">
    <h1>Hello from ECS Fargate RVCE 🚀</h1><h2>Version: {VERSION}</h2></body>"""

@app.route("/health")
def health():
    return "ok"
