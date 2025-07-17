#function to round altitude to nearest whole 1000
def round_to_nearest_1000(x):
    return round(x/1000) * 1000

#create altitude calculator class
class AltitudeCalculator:
    #dictionary storing altitude as keys and percent base as values
    altitude_base = {
        4000: 0.3,
        5000: 0.5,
        6000: 0.7,
        7000: 0.9,
        8000: 1.2,
        9000: 1.4,
    }

    try:
        #get altitude
        print("Please ensure that the altitude entered is 4000 feet and above and 9000 feet and below")
        altitude = int(input("Please enter your altitude: "))

        #round altitude to nearest whole number and assign it back
        roundedAlt = round_to_nearest_1000(altitude)
        altitude = roundedAlt

        #check if altitude is out of range and raise error if so
        if altitude < 3999 or altitude > 9000:
            raise ValueError("Altitude must be between 4000 and 9000 feet")

        #get duration
        print("Please ensure that the duration entered is greater than 1")
        duration = int(input("Please enter the amount of weeks you are staying at altitude: "))

        #check if duration is out of range and raise error if so
        if duration < 1 or duration > 4:
            raise ValueError("Duration must be between 1 and 4 weeks.")

        #get Vo2
        #VO2 = int(input("Please enter your Vo2 Max: "))

        #calculate altitude benefit, pull values from dictionary
        if altitude in altitude_base and 1 <= duration <=4:
            base_percent = altitude_base[altitude]
            total_increase = base_percent * duration
            print(f"You will see a {total_increase}% increase in RBC!")
        else:
            print("Invalid altitude or duration entered.")

    #this exception catches any string that starts with altitude or duration and returns the error
    except ValueError as e:
        if str(e).startswith("Altitude") or str(e).startswith("Duration"):
            print(f"ERROR: {e}")
        else:
            print("ERROR: Please enter valid numeric values")
    except Exception as e:
        print(f"An unexpected error occured")
