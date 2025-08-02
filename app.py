import os
import csv
from datetime import datetime

from flask import Flask, request, render_template

from DiamondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)
LOG_FILE = 'prediction_logs.csv'

# Utility to log predictions
def log_prediction(timestamp, result):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, result])

# Utility to read latest logs
def read_prediction_logs(limit=5):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='r') as file:
            reader = csv.reader(file)
            logs = list(reader)[-limit:]
    return logs

@app.route('/')
def home_page():
    logs = read_prediction_logs()
    return render_template('index.html', logs=logs)

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        try:
            data = CustomData(
                carat=float(request.form.get('carat')),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity')
            )

            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)

            # Save prediction log
            log_prediction(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), result)

            return render_template('result.html', final_result=result)

        except Exception as e:
            return f"Error during prediction: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
