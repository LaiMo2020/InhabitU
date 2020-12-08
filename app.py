# Inspired some code were copied/edited the mini project task manager
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from json import dumps
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Route to home page


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Route to habits page

@app.route("/get_habits/<username>", methods=["GET"])
def get_habits(username):
    habits = list(mongo.db.habits.find({"created_by": username}))
    return render_template("habit.html", habits=habits)
    habits = {
        "category_name": request.form.get("category_name"),
        "habit_name": request.form.get("habit_name"),
        "habit_description": request.form.get("habit_description"),
        "prioritize": True,
        "due_date": request.form.get("due_date"),
        "created_by": session["user"]
    }


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("password") == request.form.get("confirm-password"):
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "email": request.form.get("email")
            }
            mongo.db.users.insert_one(register)
            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
        flash("Password Dose Not Much")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/home/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "home.html", username=username, categories=categories)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# Create habit


@app.route("/create_habit", methods=["GET", "POST"])
def create_habit():
    if request.method == "POST":
        prioritize = True if request.form.get("prioritize") else False
        habits = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "prioritize": prioritize,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.habits.insert_one(habits)
        flash("Habit Successfully Created")
        return redirect(url_for("get_habits", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_habit.html", categories=categories)

# edit a habit


@app.route("/edit_habit/<habit_id>", methods=["GET", "POST"])
def edit_habit(habit_id):
    if request.method == "POST":
        prioritize = True if request.form.get("prioritize") else False
        submit = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "prioritize": prioritize,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        # edit and send user to habits page
        mongo.db.habits.update({"_id": ObjectId(habit_id)}, submit)
        flash("Habit Successfully Updated")
        return redirect(url_for("get_habits", username=session["user"]))

    habit = mongo.db.habits.find_one({"_id": ObjectId(habit_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_habit.html", habit=habit, categories=categories)

# delete habit


@app.route("/delete_habit/<habit_id>")
def delete_habit(habit_id):
    mongo.db.habits.remove({"_id": ObjectId(habit_id)})
    flash("Habit Successfully Deleted")
    return redirect(url_for("get_habits", username=session["user"]))


@app.errorhandler(404)
def page_not_found(e):
    # Error page
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
