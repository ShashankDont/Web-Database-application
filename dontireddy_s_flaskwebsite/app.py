from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/enternew')
def new_user():
    return render_template('add_user.html')

# Add a New Baking Contest User
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"].strip()
        age = request.form["age"].strip()
        phone_number = request.form["phone_number"].strip()
        security_level = request.form["security_level"].strip()
        password = request.form["password"].strip()

        # Validate inputs
        errors = []
        if not name or name.isspace():
            errors.append("Name cannot be empty.")
        if not age.isdigit() or not (0 < int(age) < 121):
            errors.append("Age must be a number between 1 and 120.")
        if not phone_number or phone_number.isspace():
            errors.append("Phone number cannot be empty.")
        if not security_level.isdigit() or not (1 <= int(security_level) <= 3):
            errors.append("Security Level must be between 1 and 3.")
        if not password or password.isspace():
            errors.append("Password cannot be empty.")
        
        # If errors print them
        msg = "; ".join(errors)
        if errors:
            return render_template("results.html", msg=msg)

        # Add new user to the databse 
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO BakingContestPeople (name, age, phone_number, security_level, password) VALUES (?, ?, ?, ?, ?)",
                    (name, int(age), phone_number, int(security_level), password),
                )
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            msg = f"Error adding record: {e}"
        finally:
            return render_template("results.html", msg=msg)
            con.close()

# List Baking Users
@app.route("/list_users")
def list_users():
    con = sql.connect("database.db")
    con.row_factory = sql.Row 
    cur = con.cursor()
    cur.execute("SELECT name, age, phone_number, security_level,password FROM BakingContestPeople")
    rows = cur.fetchall()
    return render_template("list_users.html", rows=rows)

# List Baking Results
@app.route("/list_results")
def list_results():
    con = sql.connect("database.db")
    con.row_factory = sql.Row  
    cur = con.cursor()
    cur.execute("""
        SELECT entry_id, user_id, baking_item, num_excellent_votes, num_ok_votes, num_bad_votes 
        FROM BakingContestEntry
    """)
    rows = cur.fetchall()
    return render_template("list_results.html", rows=rows)

# Results page
@app.route("/results")
def results():
    msg = request.args.get("msg", "No message.")
    return render_template("results.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True, port=52525, host ="0.0.0.0")
