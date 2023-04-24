from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def index():
    return "<p>トップページ</p>"

@app.route("/login")
def login():
    return "<p>ログイン</p>"

@app.route("/user/<username>")
def profile(username):
    return f"<p>{escape(username)}のプロファイル</p>"

with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="foobar"))
    print(url_for("profile", username="Hoge"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)