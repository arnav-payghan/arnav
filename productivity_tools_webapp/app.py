from flask import Flask as fk, render_template, request


app = fk(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/wordcount", methods=["POST"])
def wordcount():
    text = request.form["text"]
    word_count = len(text.split())
    return f"<h2>Word Count: {word_count}</h2><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)