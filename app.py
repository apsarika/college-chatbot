from flask import Flask, render_template, request
from semantic_search import get_best_match

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chatbot():
    answer = ""
    if request.method == "POST":
        query = request.form.get("query")
        answer = get_best_match(query)
    return render_template("index.html", response=answer)

if __name__ == "__main__":
    app.run(debug=True)
