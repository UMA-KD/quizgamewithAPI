import requests, html, random
import json
url="https://opentdb.com/api.php?amount=50"
response=requests.get(url)
if response.status_code:
    data=response.json()
    question=[]
    for quest in data["results"]:
        option=[html.unescape(quest["correct_answer"])]+[html.unescape(ans) for ans in quest["incorrect_answers"]]
        random.shuffle(option)
        quest_data={"q":html.unescape(quest["question"]),
                    "options":option,
                    "ans":html.unescape(quest["correct_answer"]),
                    "category":html.unescape(quest["type"]),
                    "difficulty":html.unescape(quest["difficulty"])}
        question.append(quest_data)
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(question,file, indent=4)
else:
    print("Error: ", response.stauts_code)
    print("Failed to download questions")
