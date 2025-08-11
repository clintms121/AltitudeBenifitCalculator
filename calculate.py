from contextlib import nullcontext


def round_to_nearest_1000(x):
    return round(x/1000) * 1000

# Pace calculator logic as function
def pace_calculator(distance, time=None, pace=None, unit='mile'):

    def time_to_minutes(hours, minutes, seconds):
        return hours * 60 + minutes + seconds / 60

    def pace_to_minutes(pace_str):
        mins, secs = map(int, pace_str.strip().split(':'))
        return mins + secs / 60

    def minutes_to_pace_str(minutes_val):
        mins = int(minutes_val)
        secs = round((minutes_val - mins) * 60)
        return f"{mins}:{secs:02d}"

    def minutes_to_time_str(total_minutes):
        hours = int(total_minutes // 60)
        mins = int(total_minutes % 60)
        secs = round((total_minutes * 60) % 60)
        return f"{hours}h {mins}m {secs}s"

    # Compute total minutes
    if time:
        total_minutes = time_to_minutes(*time)
        pace_minutes = total_minutes / distance
    elif pace:
        pace_minutes = pace_to_minutes(pace)
        total_minutes = distance * pace_minutes
    else:
        raise ValueError("You must provide either time or pace.")

    # Calculate speed
    hours = total_minutes / 60
    speed = distance / hours
    unit_label = "mph" if unit == "mile" else "kph"

    return {
        "pace": f"{minutes_to_pace_str(pace_minutes)} per {unit}",
        "time": minutes_to_time_str(total_minutes),
        "speed": f"{speed:.2f} {unit_label}"
    }

# Altitude benefit calculation logic as a function
def altitude_calculator(altitude, duration):
    altitude_base = {
        4000: 0.3,
        5000: 0.5,
        6000: 0.7,
        7000: 0.9,
        8000: 1.2,
        9000: 1.4,
    }
    try:
        altitude = int(float(altitude))
        duration = int(float(duration))
        altitude = round_to_nearest_1000(altitude)
        if altitude < 4000 or altitude > 9000:
            return None, "Altitude must be between 4000 and 9000 feet."
        if duration < 1 or duration > 4:
            return None, "Duration must be between 1 and 4 weeks."
        if altitude in altitude_base:
            base_percent = altitude_base[altitude]
            total_increase = base_percent * duration
            return round(total_increase, 2), "increase in RBC!"
        else:
            return None, "Invalid altitude entered."
    except ValueError:
        return None, "Please enter valid numeric values."
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

