import google.generativeai as genai

genai.configure(api_key="api-key")
model_name = "gemini-1.5-pro-latest"
generation_config = {"temperature": 0.5, "top_p": 0.95, "top_k": 0, "max_output_tokens": 500}
model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

convo = model.start_chat(history=[])

def get_response(user_input):
    convo.send_message(user_input)
    return convo.last.text

print("Hello! I'm ready to assist you. How can I help today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "stop", "quit", "bye", "goodbye"]:
        print("Goodbye!")
        break

    response = get_response(user_input)
    print(response)
