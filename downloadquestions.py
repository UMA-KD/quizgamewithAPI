import requests
import json
url="https://opentdb.com/api.php?amount=50"
response=requests.get(url)
if response.status_code:
    data=response.json()
    question=[]
    for quest in data["results"]:
        quest_data={"q":quest["question"],
                    "options":[quest["correct_answer"]]+quest["incorrect_answers"],
                    "ans":quest["correct_answer"],
                    "category":quest["type"],
                    "difficulty":quest["difficulty"]}
        question.append(quest_data)
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(question,file, indent=4)
else:
    print("Error: ", response.stauts_code)
    print("Failed to download questions")
