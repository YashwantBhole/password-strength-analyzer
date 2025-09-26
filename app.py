import secrets, string 
from flask import Flask, render_template, request,redirect,url_for,jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."

    return "Strong: Your password is secure!"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

@app.route("/suggest-password", methods=["GET"])
def suggest_password():
    strong_password = generate_password(12)
    return jsonify( {"password" : strong_password})

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    password = ""
    if request.method == "POST":
        password = request.form.get("password")
        result = check_password_strength(password)
        #pass result once via query string, then redirect
        return redirect(url_for("index", result = result ))
    result = request.args.get("result") #show once
    return render_template("index.html", result=result, password=password)

if __name__ == "__main__":
    app.run(debug=True)
