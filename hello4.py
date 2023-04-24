from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/user/<username>")
def show_user(username):
    return f"<p>ユーザー名：{escape(username)}</p>"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"<p>投稿番号：{post_id}</p>"

@app.route("/path/<pass:subpath>")
def show_post(subpath):
    return f"<p>サブパス：{escape(subpath)}</p>"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)