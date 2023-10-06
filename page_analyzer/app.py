from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['DEBUG'] = os.getenv('DEBUG')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run
