from flask import Flask
from flask import render_template, request, redirect
from flask import current_app as app
from models import User, Decks
from database import db


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":

        user_name = request.form.get("username")
        password = request.form.get("password")
        user_name_present = User.query.filter_by(user_cred=user_name).first()
        if user_name.isalnum():
            if user_name_present:

                if user_name_present.password == password:  # Go to dashboard

                    return redirect(f"/dashboard/{user_name}")

                else:
                    error = "User name exists/ Password is in correct. Please try again"
                    return render_template("login.html", error=error)
            else:
                cred_entry = User(user_cred=user_name, password=password)
                db.session.add(cred_entry)
                db.session.commit()

        else:
            error = "Only alphabets and numbers are allowed for user name and password"
            return render_template("login.html", error=error)

    return render_template("login.html", error=error)


@app.route("/dashboard/<user_name>", methods=["GET", "POST"])
def dashboard(user_name):
    user_id = User.query.filter_by(user_cred=user_name).first().user_id
    print(user_id)
    decks = Decks.query.filter_by(deck_user_id=user_id).all()
    dl = len(decks)

    return render_template("dashboard.html", decks=decks, ld=dl, user_name=user_name)

    pass


@app.route("/dashboard/<user_name>/adddeck", methods=["GET", "POST"])
def adddeck(user_name):
    user_id = User.query.filter_by(user_cred=user_name).first().user_id

    if request.method == "GET":
        return render_template("adddeck.html",user_name=user_name)

    elif request.method=="POST":

        deck_name=request.form.get("deck_name")
        deck_description=request.form.get("deck_description")

        add_entry=Decks(deck_user_id=user_id,deck_name=deck_name,deck_description=deck_description)
        db.session.add(add_entry)
        db.session.commit()

        return redirect("/dashboard/<user_name>",user_name=user_name)

@app.route("/deck/<user_name>/<deck_id>/update", methods=["GET", "POST"])
def deck_update(user_name,deck_id):

    user_name=user_name

    return render_template("update.html")

@app.route("/deck/<user_name>/<deck_id>/delete", methods=["GET", "POST"])
def deck_delete(user_name, deck_id):
    k = User.query.filter_by(user_cred=user_name).first().user_id


    Decks.query.filter_by(id=deck_id,deck_user_id=k).delete()
    db.session.commit()
    return redirect("/dashboard/<user_name>",user_name=user_name)
