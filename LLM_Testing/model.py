from transformers import pipeline
generator = pipeline('text-generation', model='mistralai/Mistral-7B-v0.1')
prompt = input("Enter Query : ") 
result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])