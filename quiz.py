import json
score=0
print("-"*30)
print("Quiz Game")
print("-"*30)
with open("questions.json", "r") as file:
    questions=json.load(file)
diff=int(input("Select difficulty level\n1. easy\n2. medium\n3. hard\n"))
while True:
    idx=1
    if diff==1:
        for quests in questions:
       
            if quests['difficulty']=="easy":
                print(f"{idx}. {quests['q']}")
                for i,j in enumerate(quests['options']):
                    print(f"{chr(64+i+1)}. {j}")
            idx+=1
            answer=input("Enter the correct option: ").strip().upper()
            
            sel_idx=ord(answer)-65
            
            while answer:
                if sel_idx<=len(quests['options']):
                    sel_ans=quests['options'][sel_idx]
                    print(sel_ans)
                    if sel_ans==quests['ans']:
                        print("Correct answer")
                        score+=1
                        print(f"Score: {score}/{len(questions)}")
                        break
                    else:
                        print("Wrong answer! Better luck next time.")
                        print(f"Score: {score}/{len(questions)}")
                        break
                else:
                    print("Enter number from given options")
                    answer=input("Select answer from options: ")
        cont=input("Press any character to continue or 'q' to exit quiz: ")
        if cont.lower()=="q":
            break
    print(f"Your score is {score}/{len(questions)}")
    break