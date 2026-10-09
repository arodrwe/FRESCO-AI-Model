# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, mean_absolute_error
import config
import joblib

def train_ai_models():
    # Load the spreadsheet from the project folder
    dataset = pd.read_csv(config.DATASET_FILENAME)
    
    # Select the columns the AI will use to make its guesses
    input_features = dataset[['Spot1_R', 'Spot1_G', 'Spot1_B', 'Temperature', 'Humidity']]
    
    # Select the correct answers the AI needs to learn
    freshness_target = dataset['Freshness_Label']
    shelf_life_target = dataset['Remaining_Shelf_Life_Hours']
    
    # Mix and split the data into training and testing piles
    X_train, X_test, y_class_train, y_class_test, y_reg_train, y_reg_test = train_test_split(
        input_features, freshness_target, shelf_life_target, 
        test_size=config.TEST_SPLIT_RATIO, random_state=config.RANDOM_SEED
    )
    
    # Level out the numbers so the math does not get confused by large values
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the machine to classify if the meat is fresh or spoiled
    classification_model = SVC()
    classification_model.fit(X_train_scaled, y_class_train)
    class_predictions = classification_model.predict(X_test_scaled)
    class_accuracy = accuracy_score(y_class_test, class_predictions)
    
    # Train the machine to calculate the exact hours left
    regression_model = SVR()
    regression_model.fit(X_train_scaled, y_reg_train)
    reg_predictions = regression_model.predict(X_test_scaled)
    reg_error = mean_absolute_error(y_reg_test, reg_predictions)
    
    print("Model training is complete.")
    print(f"Freshness accuracy score: {class_accuracy * 100}%")
    print(f"Shelf life calculation error: off by about {round(reg_error, 2)} hours")

    joblib.dump(scaler, config.SCALER_FILENAME)
    joblib.dump(classification_model, config.CLASSIFIER_FILENAME)
    joblib.dump(regression_model, config.REGRESSOR_FILENAME)
    print("The AI brains have been successfully saved to your folder.")

if __name__ == "__main__":
    train_ai_models()