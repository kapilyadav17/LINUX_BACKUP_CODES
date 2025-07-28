from transformers import pipeline

class IntentDetector:

    #A class to determine customer intent from conversation text using zero-shot classification.
    def __init__(self):
        # Define possible customer intents
        self.intent_options = [
            "Book Appointment",
            "Product Inquiry",
            "Pricing Negotiation",
            "Support Request",
            "Follow-Up"
        ]
        # Initialize the zero-shot classification pipeline with a pre-trained model
        self.intent_pipeline = pipeline(
            task="zero-shot-classification",
            model="cross-encoder/nli-distilroberta-base",
            
            
        )

    def classify_intent(self, dialogue: str) -> dict:
        #Predicts the most likely intent from a given conversation.
        # Args: dialogue (str): The input conversation or message.
        # Returns: dict: Contains the predicted intent and a brief explanation.
       
        classification = self.intent_pipeline(dialogue, self.intent_options)
        top_intent = classification["labels"][0]
        explanation = (
            f"Based on the conversation, the customer is likely interested in '{top_intent.lower()}'."
        )
        return {
            "predicted_intent": top_intent,
            "rationale": explanation
        }
