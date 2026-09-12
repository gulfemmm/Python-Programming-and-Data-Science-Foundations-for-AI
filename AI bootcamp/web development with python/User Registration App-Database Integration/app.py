
from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


# Create Database Tables
with app.app_context():
    db.create_all()


# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        # Hash password
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful!', 'success')

            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()

            print("DATABASE ERROR:", e)

            flash('Username or Email already exists!', 'error')

            return redirect(url_for('register'))

    return render_template('register.html')


# Login Route
@app.route('/login')
def login():

    messages = get_flashed_messages(with_categories=True)

    message_text = ""

    for category, message in messages:
        message_text += message + "<br>"

    return message_text + "Login Page (To be implemented)"


if __name__ == '__main__':
    app.run(debug=True)

