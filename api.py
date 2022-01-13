from flask import Flask ,request, jsonify
app=Flask(__name__)
from classifier import get_prediction
@app.route("/predict-digit",methods=['POST'])
def predict_digit():
    image=request.files.get('digit')
    prediction=get_prediction(image)
    return jsonify({'prediction':prediction})
if __name__=='__main__':
    app.run(debug=True)
