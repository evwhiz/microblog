from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
