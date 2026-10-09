# predict_new_meat.py
import joblib
import pandas as pd
import config

def test_new_sample():
    # Load the saved brains from your project folder
    scaler = joblib.load(config.SCALER_FILENAME)
    classifier = joblib.load(config.CLASSIFIER_FILENAME)
    regressor = joblib.load(config.REGRESSOR_FILENAME)
    
    # Enter the numbers for your new piece of meat here
    new_spot_red = 180
    new_spot_green = 140
    new_spot_blue = 80
    new_temperature = 25.5
    new_humidity = 62.0
    
    # Pack the numbers exactly how the AI expects them
    new_data = pd.DataFrame([{
        'Spot1_R': new_spot_red,
        'Spot1_G': new_spot_green,
        'Spot1_B': new_spot_blue,
        'Temperature': new_temperature,
        'Humidity': new_humidity
    }])
    
    # Level out the numbers using the same math from the training phase
    scaled_data = scaler.transform(new_data)
    
    # Ask the brains to make their guesses
    freshness_guess = classifier.predict(scaled_data)[0]
    hours_left_guess = regressor.predict(scaled_data)[0]
    
    print(f"The AI thinks this meat is: {freshness_guess}")
    print(f"Estimated time before spoiling: {round(hours_left_guess, 1)} hours")

if __name__ == "__main__":
    test_new_sample()