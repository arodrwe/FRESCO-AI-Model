# process_image.py
import cv2
import numpy as np
import config

def get_average_color(image, center_x, center_y, radius):
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, (center_x, center_y), radius, 255, -1)
    
    average_color = cv2.mean(image, mask=mask)
    
    # OpenCV loads images backwards in Blue, Green, Red format
    blue_val = int(average_color[0])
    green_val = int(average_color[1])
    red_val = int(average_color[2])
    
    return blue_val, green_val, red_val

def process_sensor_image(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Could not find the picture. Please check the file name.")
        return

    blue1, green1, red1 = get_average_color(image, config.SPOT_1_X, config.SPOT_1_Y, config.SPOT_RADIUS)
    blue2, green2, red2 = get_average_color(image, config.SPOT_2_X, config.SPOT_2_Y, config.SPOT_RADIUS)
    blue3, green3, red3 = get_average_color(image, config.SPOT_3_X, config.SPOT_3_Y, config.SPOT_RADIUS)
    blue4, green4, red4 = get_average_color(image, config.SPOT_4_X, config.SPOT_4_Y, config.SPOT_RADIUS)
    
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    l_val1, a_val1, b_lab_val1 = get_average_color(lab_image, config.SPOT_1_X, config.SPOT_1_Y, config.SPOT_RADIUS)

    color_data = {
        "Spot1_Red": red1,
        "Spot1_Green": green1,
        "Spot1_Blue": blue1,
        "Spot1_L_value": l_val1,
        "Spot1_A_value": a_val1,
        "Spot1_B_value": b_lab_val1
    }
    
    print("Successfully extracted color data:")
    print(color_data)
    return color_data

if __name__ == "__main__":
    process_sensor_image("sample_test_image.jpg")