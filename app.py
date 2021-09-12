
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
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
def home():
    """
    Home page view
    """
    return render_template("home.html")


# Route to habits page

@app.route("/get_habits/<username>", methods=["GET"])
def get_habits(username):
    """
    habit page view, diplaying only the habits created
    by the user that logged in.
    """
    # *** Check if user is logged in. If not, redirect them to the login page.
    if "user" in session:
        habits = list(mongo.db.habits.find({"created_by": session["user"]}))
        return render_template("habit.html", habits=habits)
    else:
        return redirect('login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    register page view, with four fileds, username, email,
    password, and confirm password
    """
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")
        email = request.form.get("email")

        # *** check if username already exists in db
        existing_user = mongo.db.users.find_one({"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if password == confirm_password:
            register = {
                "username": password,
                "password": generate_password_hash(password),
                "email": email
            }
            mongo.db.users.insert_one(register)

            # *** put the new user into 'session' cookie
            session["user"] = username
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))

        else:
            flash("Passwords do not match.")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    login page view, with two fileds, username, email,
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], password):
                session["user"] = username
                flash("Welcome, {}".format(
                    username))
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


@app.route("/home/<username>", methods=["GET"])
def profile(username):
    # *** grab the session user's username from db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    username = mongo.db.users.find_one(
        {"username": session["user"]})

    if session["user"]:
        return render_template(
            "home.html", username=username, categories=categories)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    remove user from session cookie, tell them they are looged out
    """
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("login"))


@app.route("/create_habit", methods=["GET", "POST"])
def create_habit():
    """
    create page view, here user can create a new habit
    """
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
    return render_template("create_habit.html")


@app.route("/add_journals/<habit_id>", methods=["GET", "POST"])
def add_journals(habit_id):
    """
    journal entry page view, user can add daily notes to his journal
    eg: follow up his performance in each habit.
    the jouranl id is connecting with the habit id
    """
    habit = mongo.db.habits.find_one({"_id": ObjectId(habit_id)})
    if request.method == "POST":
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        journal = {
            "habit_id": habit_id,
            "journal_entry_text": request.form.get("journal_entry_text"),
            "date": date_time
        }
        mongo.db.journal_entries.insert_one(journal)

        flash("Journal Entry Successfully Created")
        return redirect(url_for("add_journals", habit_id=habit_id))
    journals = list(mongo.db.journal_entries.find({"habit_id": (habit_id)}))
    return render_template("add_journal.html", habit=habit, journals=journals)


@app.route("/delete_journal<journal_id>")
def delete_journal(journal_id):
    """
    delete one journal entry
    """
    mongo.db.journal_entries.remove({"_id": ObjectId(journal_id)})
    flash("Journal Successfully Deleted")
    # *** return to habit pages after deleting
    return redirect(url_for("get_habits", username=session["user"]))


@app.route("/edit_habit/<habit_id>", methods=["GET", "POST"])
def edit_habit(habit_id):
    """
    editing habit so it match user new availability
    """
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


@app.route("/delete_habit/<habit_id>")
def delete_habit(habit_id):
    """
    delete one habit
    """
    mongo.db.habits.remove({"_id": ObjectId(habit_id)})
    flash("Habit Successfully Deleted")
    # *** return user to habit page
    return redirect(url_for("get_habits", username=session["user"]))


@app.errorhandler(404)
def page_not_found(e):
    """
    give 404 error id the page do not exisit
    """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
