import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["PLAYER_ID", "AGE", "GOALS", "TEAM"]

def generate_row():

    return {
        "PLAYER_ID": random.randint(1000, 9999),
        "AGE": random.randint(16, 45),
        "GOALS": random.randint(0, 60),
        "TEAM": random.choice(["Lokomotiv", "Spartak", "Dynamo Minsk", "Avangard", "Ak Bars"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
