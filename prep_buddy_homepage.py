import importlib
x=int(input("enter choice"))
user_input=input()

if (x==1):
    buddy = importlib.import_module("buddy_ai_text_ui")
    print(buddy.get_response(user_input))  

elif (x==2):
    course = importlib.import_module("course_search")
    print(course.recommend_resources())  
elif (x==3):
    test = importlib.import_module("quiz")
    question=test.question
    print(test.get_response(user_input))  
    print(test.ask_and_evaluate(question, filename="progress.csv"))  
