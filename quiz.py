import json
score=0
print("-"*30)
print("Quiz Game")
print("-"*30)
with open("questions.json", "r") as file:
    questions=json.load(file)
while True:
    diff=int(input("Select difficulty level\n1. easy\n2. medium\n3. hard\n"))
    if diff==1:
        selected_difficulty="easy"
        
    elif diff==2:
        selected_difficulty="medium"
        
    elif diff==3:
        selected_difficulty="hard"
        
    else:
        print("Select correct number")
        continue

    idx=1
    
    for quests in questions:
        print(quests['difficulty'])
        if quests['difficulty']==selected_difficulty:
            print(f"{idx}. {quests['q']}")
            for i,j in enumerate(quests['options']):
                print(f"{chr(64+i+1)}. {j}")
            idx+=1
            try:
                answer=input("Enter the correct option: ").strip().upper()
                while True:
                    sel_idx=ord(answer)-65
                    print(sel_idx)
                
                    if 0<=sel_idx<len(quests['options']):
                        sel_ans=quests['options'][sel_idx]
                        print(sel_ans)
                        if sel_ans==quests['ans']:
                            print("Correct answer")
                            score+=1
                            print(f"Score: {score}/{idx-1}")
                            break
                        else:
                            print("Wrong answer! Better luck next time.")
                            print(f"Score: {score}/{idx-1}")
                            break
                    else:
                        print("Enter number from given options")
                        # break
                        answer=input("Select answer from options: ").strip().upper()
            except ValueError:
                print("Enter correct input")
    print(f"Your score is {score}/{idx-1}")
    cont=input("Press any character to continue or 'q' to exit quiz: ")
    if cont.lower()=="q":
        break
    
    # break