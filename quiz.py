import csv
import google.generativeai as genai

genai.configure(api_key="api-key")
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 500,
}

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config)
convo = model.start_chat(history=[])

def get_response(user_input):
    convo.send_message(user_input)
    gemini_reply = convo.last.text
    return gemini_reply

def ask_and_evaluate(question, filename="progress.csv"):
    print(question)
    user_answer = input("Your answer: ")

    # Ask the AI to evaluate the answer
    evaluation_prompt = f"Evaluate the following answer to the question: {question}\n\nAnswer: {user_answer}\n\nRate the answer on a scale of 1-10."
    evaluation = get_response(evaluation_prompt)

    # Extract the score from the evaluation
    try:
        score = int(evaluation.split()[0])
    except ValueError:
        score = 0  # Handle cases where the score cannot be extracted

    print(evaluation)

    # Write the question and score to the CSV file
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Question', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, write the header if needed
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Question': question, 'Score': score})

while True:
    topic = input("What topic are you learning? ")
    prompt = f"Generate 10 questions to test knowledge on {topic}"
    questions = get_response(prompt).split('\n')

    for question in questions:
        ask_and_evaluate(question)

    if not input("Do you want to continue? (yes/no): ").lower() == "yes":
        break
