from flask import Flask, render_template, request
from cli_logic import wordcount

app = Flask(__name__)
history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cli_input = request.form["cli_input"]
        command, *args = cli_input.strip().split(" ", 1)
        result = ""

        if command == "wordcount":
            if args:
                result = wordcount.count_words(args[0])
            else:
                result = "Usage: wordcount \"your text here\""
        else:
            result = f"Unknown command: {command}"

        history.append({"command": cli_input, "result": result})

    return render_template("index.html", history=history)
