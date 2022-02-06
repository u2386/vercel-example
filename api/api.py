from flask import Flask, request


app = Flask("vercel-example")


@app.route("/")
def index():
    return "hello"


@app.route("/echo", methods=["POST"])
def echo():
    command = request.values.get("command")
    return command
