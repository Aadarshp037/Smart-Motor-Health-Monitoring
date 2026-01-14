import random
import time
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "motor_data.csv")

def generate_motor_data():
    return {
        "voltage": round(random.uniform(210, 240), 2),
        "current": round(random.uniform(2.0, 6.0), 2),
        "rpm": random.randint(1200, 3000),
        "temperature": round(random.uniform(40, 95), 2)
    }

# Create file with header if it doesn't exist
if not os.path.exists(DATA_PATH):
    with open(DATA_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["voltage", "current", "rpm", "temperature"])

while True:
    data = generate_motor_data()
    print(data)

    with open(DATA_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data.values())

    time.sleep(1)
