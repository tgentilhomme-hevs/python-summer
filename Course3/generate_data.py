import json
import random
import math
from typing import List, Dict

# Step 1: Generate synthetic bacterial colony data
def generate_colony_data(n=10, times=range(0, 10)):
    colonies = []
    for i in range(n):
        name = f"Colony_{i}"
        temperature = random.choice([30, 37, 42])  # degrees Celsius
        ph = random.choice([6.0, 7.0, 8.0])
        sugar = round(random.uniform(0.5, 2.0), 2)  # glucose concentration (g/L)

        # Use an arbitrary growth formula to generate data
        growth_data = {}
        for t in times:
            base = sugar * math.exp(-((temperature - 37) ** 2) / 20)  # peak at 37°C
            ph_factor = 1 - abs(ph - 7) * 0.3  # best growth at pH 7
            growth = base * ph_factor * math.log(t + 1)  # log growth over time
            growth_data[str(t)] = round(growth, 3)

        colony = {
            "name": name,
            "conditions": {
                "temperature": temperature,
                "ph": ph,
                "sugar": sugar
            },
            "growth": growth_data
        }
        colonies.append(colony)

    return colonies

# Generate and save the dataset
colony_dataset = generate_colony_data(n=10, times=range(0, 10))

with open("colonies.json", "w") as f:
    json.dump(colony_dataset, f, indent=2)
