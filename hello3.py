from flask import Flask

app = Flask(__name__)

@app.route("/projects/")
def projects():
    return "<p>プロジェクトページ</p>"
@app.route("/about")
def about():
    return "<p>サイトについて</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)