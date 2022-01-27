from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello World!"

    @app.route('/welcome')
    @app.route('/welcome/<name>')
    def welcome(name = None):
        return render_template('welcome.html', name = name)
    
    return app