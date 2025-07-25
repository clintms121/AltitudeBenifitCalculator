import os
from flask import Flask, render_template, request
from calculate_benifit import AltitudeCalculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        altitude = request.form.get('altitude', '')
        duration = request.form.get('duration', '')
        if altitude and duration:
            result, error = AltitudeCalculator(altitude, duration)
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#http://127.0.0.1:5000
#http://localhost:5000

