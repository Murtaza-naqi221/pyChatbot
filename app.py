from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from chat import get_response

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.get("/")
def index_get():

    return render_template("base.html")

@app.post("/predict")
@cross_origin()
def predict():
    text = request.get_json().get("message")
    #TODO check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
    

