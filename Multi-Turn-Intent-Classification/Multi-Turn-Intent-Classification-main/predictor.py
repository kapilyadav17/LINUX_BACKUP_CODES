import json
import csv
from preprocess import create_conversation
from model import IntentDetector  # Updated to match your new class name

# Initialize the intent detector
intent_model = IntentDetector()

def predict_intents(input_file: str, json_output: str, csv_output: str):
    """
    Executes the prediction workflow:
    - Reads conversations from a JSON file
    - Predicts intent for each conversation
    - Saves results to both JSON and CSV formats
    """
    # Load conversation data
    with open(input_file, 'r') as infile:
        conversations = json.load(infile)

    output_data = []

    # Iterate through each conversation entry
    for entry in conversations:
        conv_id = entry.get('conversation_id')
        formatted_text = create_conversation(entry.get('messages', []))
        intent_result = intent_model.classify_intent(formatted_text)

        output_record = {
            "conversation_id": conv_id,
            "predicted_intent": intent_result["predicted_intent"],
            "rationale": intent_result["rationale"]
        }
        output_data.append(output_record)

    # Write results to a JSON file
    with open(json_output, 'w') as json_file:
        json.dump(output_data, json_file, indent=2)

    # Write results to a CSV file
    with open(csv_output, 'w', newline='') as csv_file:
        fieldnames = ["conversation_id", "predicted_intent", "rationale"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)
