import loginpage

name=loginpage.username()

skill=loginpage.skill()

print(f"hello {name}, welcome to prep buddy, your personal assistant to help you prepare for {skill} interviews and questions")

import course, assistant
course.recommend_resources(skill)

print("now you can ask me any question related to your skill, and i will help you out, but remember, i will not give you direct answers, just guide you how to get the answer")

doubt = input("do you have any doubt? (yes/no)\n")

while doubt.lower() == "yes":
    user_input = input("what question doubts you\n")
    assistant.ai_reply(user_input)