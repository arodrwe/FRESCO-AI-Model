# main.py
import pandas as pd
import numpy as np
import config

def generate_mock_data():
    all_recorded_rows = []
    meat_options = ["Pork", "Chicken", "Beef"]

    for sample_number in range(1, config.TOTAL_SAMPLES + 1):
        meat_type = np.random.choice(meat_options)
        
        # Simulate how long the meat was sitting at the market before purchase
        market_exposure_hours = round(np.random.uniform(config.MIN_MARKET_HOURS, config.MAX_MARKET_HOURS), 1)
        
        chamber_hour = 0.0

        while chamber_hour <= config.MAX_CHAMBER_HOURS:
            # The real age of the meat is the market time plus the time inside the device
            total_spoilage_time = market_exposure_hours + chamber_hour
            
            temp_reading = config.BASE_TEMP + np.random.uniform(-1.0, 1.0)
            humidity_reading = config.BASE_HUMIDITY + np.random.uniform(-2.0, 2.0)
            
            tvc_reading = config.BASE_TVC + (total_spoilage_time * 0.2) + np.random.uniform(0.0, 0.5)
            ph_reading = config.BASE_PH + (total_spoilage_time * 0.05)
            tvbn_reading = config.BASE_TVBN + (total_spoilage_time * 1.5)

            # Check freshness based on the total age, not just the time in the chamber
            if total_spoilage_time <= config.FRESH_LIMIT_HOURS:
                status_label = "Fresh"
                shelf_life_left = config.SEMI_FRESH_LIMIT_HOURS - total_spoilage_time
            elif total_spoilage_time <= config.SEMI_FRESH_LIMIT_HOURS:
                status_label = "Semi-Fresh"
                shelf_life_left = config.SEMI_FRESH_LIMIT_HOURS - total_spoilage_time
            else:
                status_label = "Spoiled"
                shelf_life_left = 0.0

            spot1_r = int(250 - (total_spoilage_time * 5))
            spot1_g = int(100 + (total_spoilage_time * 3))
            spot1_b = int(50 + (total_spoilage_time * 2))

            spot1_r = max(0, min(255, spot1_r))
            spot1_g = max(0, min(255, spot1_g))
            spot1_b = max(0, min(255, spot1_b))

            single_record = {
                "Sample_ID": sample_number,
                "Meat_Type": meat_type,
                "Market_Hours": market_exposure_hours,
                "Chamber_Hours": chamber_hour,
                "Total_Age_Hours": round(total_spoilage_time, 1),
                "Spot1_R": spot1_r,
                "Spot1_G": spot1_g,
                "Spot1_B": spot1_b,
                "Temperature": round(temp_reading, 2),
                "Humidity": round(humidity_reading, 2),
                "TVC_Ref": round(tvc_reading, 2),
                "pH_Ref": round(ph_reading, 2),
                "TVB_N_Ref": round(tvbn_reading, 2),
                "Freshness_Label": status_label,
                "Remaining_Shelf_Life_Hours": round(shelf_life_left, 1)
            }
            
            all_recorded_rows.append(single_record)
            chamber_hour += config.TIME_INTERVAL

    dataset_table = pd.DataFrame(all_recorded_rows)
    dataset_table.to_csv("updated_mock_fresco_dataset.csv", index=False)

if __name__ == "__main__":
    generate_mock_data()