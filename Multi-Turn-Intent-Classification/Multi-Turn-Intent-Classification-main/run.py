import os
from predictor import predict_intents

os.makedirs("data/output", exist_ok=True)
if __name__ == "__main__":
       predict_intents(
    input_file="data/input.json",
    json_output="data/output/predictions.json",
    csv_output="data/output/predictions.csv"
)
    
