from flask import Flask , request , jsonify , render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('chat.html')




if __name__ == '__main__':
    app.run(debug= True)