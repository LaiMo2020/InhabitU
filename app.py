# Inspired some code were copied/edited the mini project task manager
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# sugesstion habits for user
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# suggestion for users
heart = {
        "category_name": "Heart",
        "habit_name": "Date your wife ",
        "habit_description": " invite your wife for dinner.",
        "frequenc": "Monthly "
    }
brain = {
        "category_name": "Brain",
        "habit_name": "meditate ",
        "habit_description": "Stay relax and meiditate daily",
        "frequenc": "Daily "
    }
body = {
        "category_name": "Body",
        "habit_name": "meditate ",
        "habit_description": "Stay relax and meiditate daily",
        "frequenc": "Daily "
    }
mongo.db.categories.update_one(
        {"_id": "5063114bd386d8fadbd6b004"},
        {"$set": heart},
        upsert=True
    )
mongo.db.categories.update_one(
        {"_id": "5063114bd386d8fadbd6b005"},
        {"$set": brain},
        upsert=True
    )
mongo.db.categories.update_one(
        {"_id": "5063114bd386d8fadbd6b006"},
        {"$set": body},
        upsert=True
    )

# Route to habits page


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Route to home page

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
            {"email": request.form.get("email")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirmpassword = request.form.get("confirmpassword")

        if password == confirmpassword:
            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email"),
                "password": generate_password_hash(password)
                }
            mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_email = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_email:
            # ensure hashed password matches user input
            if check_password_hash(existing_email["password"], request.form.get("password")):
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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, categories=categories)

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
        prioritize = "on" if request.form.get("prioritize") else "off"
        habits = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "prioritize": True,
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
        prioritize = "True" if request.form.get("prioritize") else "False"
        submit = {
            "category_name": request.form.get("category_name"),
            "habit_name": request.form.get("habit_name"),
            "habit_description": request.form.get("habit_description"),
            "prioritize": True,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }

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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
