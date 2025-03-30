from flask import Flask , request , jsonify , render_template
from dotenv import load_dotenv
import os
from src.data_ingestion import ingestdata
from src.retrieval_generation import generation

app = Flask(__name__)

load_dotenv()

data_file_path = os.path.join(os.getcwd(),"data/finance_data.pdf")
vstore,inserted_ids=ingestdata("Done",data_file_path)
chain=generation(vstore)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)


if __name__ == '__main__':
    app.run(debug= True)