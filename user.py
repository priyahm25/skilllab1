from flask import Flask, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

# -------------------------
# HOME PAGE → index.html
# -------------------------
@app.route("/index")
def index():
    posts = requests.get(f"{BASE_URL}/posts").json()
    return render_template("index.html", posts=posts)


# -------------------------
# POST DETAILS → post.html
# -------------------------
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = requests.get(f"{BASE_URL}/posts/{post_id}").json()

    comments = requests.get(
        f"{BASE_URL}/posts/{post_id}/comments"
    ).json()

    return render_template(
        "post.html",
        post=post,
        comments=comments
    )


if __name__ == "__main__":
    app.run(debug=True)