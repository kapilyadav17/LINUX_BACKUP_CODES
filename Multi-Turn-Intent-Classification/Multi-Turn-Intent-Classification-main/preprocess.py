import re 
import emoji
from typing import List
def clean_and_lowercase(text: str) -> str:
     # Remove emojis
    text = emoji.replace_emoji(text, replace='')
    cleaned = text.lower()  # make all characters lowercase
    cleaned = re.sub(r"[^\w\s]", "", cleaned)  # eliminate punctuation
    cleaned = re.sub(r"\s+", " ", cleaned)  # condense multiple spaces
    return cleaned.strip()  
# Formats a list of chat messages into a single conversation string
def create_conversation(messages: List[dict], max_messages: int = None) -> str:
    if max_messages is not None:
        messages = messages[-max_messages:]
    formatted_lines = [
        f"{m.get('sender', '').capitalize()}: {m.get('text', '')}" for m in messages
    ]
    return "\n".join(formatted_lines)
