from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random
from face_auth import register_face, verify_face

app = Flask(__name__)

def init_db():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    """)
    con.commit()
    con.close()

init_db()
OTP_STORE = {}

@app.route("/")
def home():
    return """
    <h2>Secure MFA Login</h2>
    <a href='/register'>Register</a><br>
    <a href='/login'>Login</a>
    """

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pwd = generate_password_hash(request.form["password"])

        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (?,?)", (user, pwd))
        con.commit()
        con.close()

        register_face()
        return "User & Face Registered Successfully ✔"

    return """
    <form method="post">
    Username:<input name="username"><br>
    Password:<input type="password" name="password"><br>
    <button>Register</button>
    </form>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("SELECT password FROM users WHERE username=?", (user,))
        row = cur.fetchone()
        con.close()

        if row and check_password_hash(row[0], pwd):
            otp = str(random.randint(100000, 999999))
            OTP_STORE[user] = otp
            print("OTP (Demo):", otp)
            return f"""
            OTP sent (check terminal)<br>
            <form action="/otp" method="post">
            <input name="username" value="{user}" hidden>
            OTP:<input name="otp"><br>
            <button>Verify OTP</button>
            </form>
            """
        return "Invalid Credentials ❌"

    return """
    <form method="post">
    Username:<input name="username"><br>
    Password:<input type="password" name="password"><br>
    <button>Login</button>
    </form>
    """

@app.route("/otp", methods=["POST"])
def otp():
    user = request.form["username"]
    otp = request.form["otp"]

    if OTP_STORE.get(user) == otp:
        if verify_face():
            return "LOGIN SUCCESS 🎉 (MFA Verified)"
        else:
            return "Face Verification Failed ❌"

    return "Invalid OTP ❌"

if __name__ == "__main__":
    app.run(debug=True)
