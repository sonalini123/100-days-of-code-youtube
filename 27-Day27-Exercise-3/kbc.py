score =0
questions=[("what is the capital of Canada?" , "Toronto"),
           ("what is the color of sky?" , "Blue" )]

for question,correct_answer in questions:
    user_answer= input(question + " " )
    if user_answer.lower()==correct_answer.lower():
        score += 100
        print(f"Correct and your reward is {score}")
        
    else:
     print("answer is incorrect")
print(f"your final reward is {score}")