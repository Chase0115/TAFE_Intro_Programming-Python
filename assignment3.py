import random

# Make sure both number are odd number
def generate_odd_number():
    odd_number = random.randint(1,1001)
    if odd_number%2 == 0:
        odd_number += 1
    return odd_number

# function display score and calculate the correct percentage
def display_score(scores, questions):
    percentage = scores/questions * 100
    print(f"Your score is {scores} out of {questions} questions. Percentage of correct answer {percentage}%")

score = 0
number_of_question = 0
should_keep_going = True

#loop for more questions
while should_keep_going:
    number_of_question += 1
    first_odd = generate_odd_number()
    second_odd = generate_odd_number()
    answer = abs(first_odd - second_odd)

    # Find the greater number first
    if first_odd > second_odd:
        display = f"  {first_odd}\n -{second_odd}\n ------ \n"
        print(display,end="")
    else:
        display = f"  {second_odd}\n -{first_odd}\n ------ \n"
        print(display,end="")

    # take user answer with using exception
    while True:
        try: 
            user_answer = int(input("  "))
            break
        except ValueError:
            print("Invalid type. Please enter numbers.")
        except Exception as err:
            print(err)

    if user_answer == answer:
        print("congratulations!!")
        score += 1
        display_score(score, number_of_question)
    else:
        print("The correct answer is ")
        print(display,end="")
        print(f"  {answer}")
        display_score(score, number_of_question)

    #loop and ask user whether to continue or not
    should_keep_going = input("Do you want another question? Type 'y' for Yes, 'n' for No:  ").lower()

    if should_keep_going == 'y':
        should_keep_going = True
        
    elif should_keep_going == 'n':
        should_keep_going = False