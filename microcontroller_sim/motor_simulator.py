import random
import time
import csv

def generate_motor_data():
    return {
        "voltage": round(random.uniform(210, 240), 2),
        "current": round(random.uniform(2.0, 6.0), 2),
        "rpm": random.randint(1200, 3000),
        "temperature": round(random.uniform(40, 95), 2)
    }

with open("../data/motor_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["voltage", "current", "rpm", "temperature"])

while True:
    data = generate_motor_data()
    print(data)

    with open("../data/motor_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data.values())

    time.sleep(1)
