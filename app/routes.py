from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Evan"}
    posts = [
        {
            "author": {"username": "Melissa"},
            "body": "Beautiful day in Aurora!"
        },
        {
            "author": {"username": "Parker"},
            "body": "I want applesauce and waffles, please. Now!"
        },
        {
            "author": {"username": "Maddie"},
            "body": "Pink Sky socks, please :)"
        },
        {
            "author": {"username": "Jax"},
            "body": "Throw the ball. Throw the ball. Was that the UPS truck?"
        }        
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
