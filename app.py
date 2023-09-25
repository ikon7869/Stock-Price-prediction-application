from flask import Flask, request, jsonify, render_template, Response
import joblib
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        Open = float(request.form['Open'])
        High = float(request.form['High'])
        Low = float(request.form['Low'])
        Volume = float(request.form['Volume'])


        features = [[Open,High,Low,Volume]]
        predicted_price = model.predict(features)
        predicted_price = str(predicted_price[0])

        print(predicted_price)

        return predicted_price      
    except Exception as e:
        print(str(e))  # Print the error message
        return "Error occurred during prediction", 500  # Return a 500 error response


if __name__ == '__main__':
    app.run(debug=True)