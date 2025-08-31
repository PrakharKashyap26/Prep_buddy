import pyttsx3
import google.generativeai as genai
import csv
import requests

try:
    x = int(input("Enter choice (1, 2, 3, or 4): "))
    if x not in [1, 2, 3, 4]:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a number (1, 2, 3, or 4).")
    exit(1)

if x == 1:
    try:
        genai.configure(api_key="apikey")
        model_name = "gemini-1.5-pro-latest"
        generation_config = {"temperature": 0.5, "top_p": 0.95, "top_k": 0, "max_output_tokens": 50}
        model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

        convo = model.start_chat(history=[])

        def get_response(user_input):
            convo.send_message(user_input)
            return convo.last.text

        print("Hello! I'm ready to assist you. How can I help today?")
        engine = pyttsx3.init()
        engine.say("Hello! I'm ready to assist you. How can I help today?")
        engine.runAndWait()

        while True:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "stop", "quit", "bye", "goodbye", "thank you"]:
                print("Goodbye!")
                engine = pyttsx3.init()
                engine.say("Goodbye!")
                engine.runAndWait()
                break

            response = get_response(user_input)
            print(response)
    
            engine = pyttsx3.init()
            engine.say(response)
            engine.runAndWait()



    except Exception as e:
        print(f"Error: {e}")

elif x == 2:
    try:
        genai.configure(api_key="apikey")
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
            evaluation_prompt = f"Evaluate the following answer to the question: {question}\n\nAnswer: {user_answer}\n\nRate the answer on a scale of 1-10 and provide feedback for improvement."
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
            prompt = f"Generate 10 multiple choice questions to test knowledge on {topic}"
            questions = get_response(prompt).split('\n')

            for question in questions:
                ask_and_evaluate(question)

            if not input("Do you want to continue? (yes/no): ").lower() == "yes":
                break
    except Exception as e:
        print(f"Error: {e}")

elif x == 3:
    try:
        import requests

        def recommend_resources():
            skill = input("Enter your skill (e.g., python, data science, web development): ").strip().lower()
    
            api_key = 'apikey'  # Replace with your API key
            cx = 'search engine id'  # Replace with your Custom Search Engine ID
            url = 'https://www.googleapis.com/customsearch/v1'
            params = {'key': api_key, 'cx': cx, 'q': f"online courses {skill}"}

            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                results = response.json()

                print("\nRecommended resources:")
                for item in results.get('items', []):
                    print(f"{item['title']} - {item['link']}")
            except (requests.RequestException, ValueError) as e:
                print(f"Error fetching resources: {e}")

# Run the function
        recommend_resources()


    except Exception as e:
        print(f"Error: {e}")

elif x == 4:
    try:
        genai.configure(api_key="apikey")
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
            evaluation_prompt = f"Evaluate the following answer to the question: {question}\n\nAnswer: {user_answer}\n\nRate the answer on a scale of 1-10. Rate 0 for blank or inappropriate answers"
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
            level = input("What is you current skill level?\n")
            topic = input("What topic would you like to learn about?\n")
            prompt = f"Generate 10 multiple-choice questions (MCQs) based on the topic {topic} for a {level} level. Each question should have 4 options (A, B, C, D) and only one correct answer.\n"
            questions = get_response(prompt).split('\n')

            for question in questions:
                ask_and_evaluate(question)

            if not input("Do you want to continue? (yes/no): ").lower() == "yes":
                break
    except Exception as e:
        print(f"Error: {e}")
