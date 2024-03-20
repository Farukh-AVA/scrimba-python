import random 
#ask user for num of questios
def math_tutor():
    num_ques = input("How many mult tables questions do you want? ")
    i = 0
    correct_ans = 0
    
    while i < int(num_ques):
        mult_1 = random.randint(1,9)
        mult_2 = random.randint(1,9)
        ans = mult_1 * mult_2
        #prompt the user with question and let user input ans
        user_ans = input(f"What is {mult_1} X {mult_2}: ") 
        if ans == int(user_ans):
            correct_ans+=1
        i+=1
    persentage = (correct_ans/int(num_ques)) * 100    
    print("Thanks for playing math tutor!")
    print(f"You got {correct_ans} correct answers")
    print(f"Your percentage score is: {persentage}%")     
math_tutor()   
    

#output greetings, num of correct ans, %correct 

 