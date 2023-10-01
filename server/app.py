from flask import Flask, request, session, jsonify, redirect, url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import User

@app.route('/')
def home():
    if 'user_id' in session:
        return f'Hello, {session["username"]}! <a href="/logout">Logout</a>'
    return 'Welcome! <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/')
        else:
            return 'Login failed. <a href="/login">Try again</a>'

    return render_template('login.html')  # Create a login form in a template

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/members-only/articles')
def members_only_articles():
    if 'user_id' not in session:
        abort(401)  # Unauthorized

    # Return JSON data for members-only articles
    articles = [
        {'title': 'LIVERPOOL FC', 'content': 'The best premier team in the whole world.'},
        {'title': 'CR7', 'content': 'The G.O.A.T of football.'},
        {'title': 'Roman Reigns', 'content': 'The Ultimate Head of the Table WWE championship G.O.A.T.'},
    ]

    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
