from flask import Flask, render_template, request
import calculate_benifit
from calculate_benifit import AltitudeCalculator

app = Flask(__name__)
Calculator = AltitudeCalculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        altitude = request.form.get('altitude', '')
        duration = request.form.get('duration', '')

        if altitude and duration:
            result, error = calculate_benifit.calculate_benefit(altitude, duration)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
