# config.py

TOTAL_SAMPLES = 10
MAX_CHAMBER_HOURS = 24.0
TIME_INTERVAL = 0.5

FRESH_LIMIT_HOURS = 10.0
SEMI_FRESH_LIMIT_HOURS = 20.0

BASE_TEMP = 25.0
BASE_HUMIDITY = 60.0

BASE_TVC = 3.0
BASE_PH = 5.5
BASE_TVBN = 10.0

MIN_MARKET_HOURS = 2.0
MAX_MARKET_HOURS = 6.0

# config.py (add these lines to your existing file)

# The size of the circle we want to measure
SPOT_RADIUS = 20

# The exact locations of the four spots on your picture (X and Y coordinates)
SPOT_1_X = 100
SPOT_1_Y = 150

SPOT_2_X = 200
SPOT_2_Y = 150

SPOT_3_X = 300
SPOT_3_Y = 150

SPOT_4_X = 400
SPOT_4_Y = 150

# config.py (add these lines to your existing file)

# The name of the spreadsheet file to read
DATASET_FILENAME = "updated_mock_fresco_dataset.csv"

# The percentage of data to hide from the AI for testing (0.2 means 20 percent)
TEST_SPLIT_RATIO = 0.2

# A fixed number to make sure the data mixes the same way every time you run it
RANDOM_SEED = 42

# config.py (add these to the bottom)

# File names for saving the trained AI brains
SCALER_FILENAME = "saved_scaler.pkl"
CLASSIFIER_FILENAME = "saved_classifier.pkl"
REGRESSOR_FILENAME = "saved_regressor.pkl"