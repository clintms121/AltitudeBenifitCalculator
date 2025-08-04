import os
from flask import Flask, render_template, request
from calculate import altitude_calculator
from calculate import pace_calculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    altitude_result = None
    pace_result = None
    error = None

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'altitude':
            altitude = request.form.get('altitude', '')
            duration = request.form.get('duration', '')
            if altitude and duration:
                altitude_result, error = altitude_calculator(altitude, duration)
            else:
                error = "Please enter both altitude and duration."

        elif form_type == 'pace':
            distance = request.form.get('distance', '')
            time_h = request.form.get('hours', '')
            time_m = request.form.get('minutes', '')
            time_s = request.form.get('seconds', '')
            pace_str = request.form.get('pace', '')
            unit = request.form.get('unit', 'mile')

            try:
                distance = float(distance)
                time = (int(time_h), int(time_m), int(time_s)) if time_h and time_m and time_s else None
                pace_result = pace_calculator(distance, time=time, pace=pace_str, unit=unit)
            except Exception as e:
                error = f"Invalid input: {e}"


    return render_template("index.html", altitude_result=altitude_result, pace_result=pace_result, error=error)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#http://127.0.0.1:5000
#http://localhost:5000

