"""
Eden Wilson
CIS 113
25 November 2024
Algorithm
Purpose: Create a program that quizzes the user on state capitals
1. import random and initialize the right variable and capitals dictionary
2. Welcome the user
3. while the user's answer is not "quit" make the keys list equal to all the keys in the dictionary and set the
state equal to a state at a random index in that list
4. set the capital to the value at the state key
5. initialize the question variable as an f string with the question and the state
6. take the user's answer as input with the question variable as the prompt
7. If they enter quit, break the loop
8. if the lowercase versions of the answer and the capital match, print that it was right,
add one to the right variable, and delete the state from the dictionary
9. continue until they enter quit
10. once all the questions are answered, calculte the percent right which is (right/10)*100
11. Display the percentage and a message that corresponds with the amount they got right


"""
import random
def main():
    right=0
    capitals = {'Alabama':'Montgomery','Alaska':'Juneau',
    'Arizona':'Phoenix','Arkansas':'Little Rock',
    'California':'Sacramento','Colorado':'Denver',
    'Connecticut':'Hartford','Delaware':'Dover',
    'Florida':'Tallahassee','Georgia':'Atlanta',
    'Hawaii':'Honolulu','Idaho':'Boise',
    'Illinois':'Springfield','Indiana':'Indianapolis',
    'Iowa':'Des Moines','Kansas':'Topeka',
    'Kentucky':'Frankfort','Louisiana':'Baton Rouge',
    'Maine':'Augusta','Maryland':'Annapolis',
    'Massachusetts':'Boston','Michigan':'Lansing',
    'Minnesota':'Saint Paul','Mississippi':'Jackson',
    'Missouri':'Jefferson City','Montana':'Helena',
    'Nebraska':'Lincoln','Nevada':'Carson City',
    'New Hampshire':'Concord','New Jersey':'Trenton',
    'New Mexico':'Santa Fe','New York':'Albany',
    'North Carolina':'Raleigh','North Dakota':'Bismarck',
    'Ohio':'Columbus','Oklahoma':'Oklahoma City',
    'Oregon':'Salem','Pennsylvania':'Harrisburg',
    'Rhode Island':'Providence','South Carolina':'Columbia',
    'South Dakota':'Pierre','Tennessee':'Nashville',
    'Texas':'Austin','Utah':'Salt Lake City',
    'Vermont':'Montpelier','Virginia':'Richmond',
    'Washington':'Olympia','West Virginia':'Charleston',
    'Wisconsin':'Madison','Wyoming':'Cheyenne'}
    input("Welcome to the state capitals quiz! (Press enter to continue)")
    input("You will get questions until you enter 'quit'. (Press enter to start)")
    runs=0
    answer=""
    while answer.lower()!="quit" and len(capitals)>0:
        keys=[x for x in capitals.keys()]
        state=keys[random.randint(0,len(keys)-1)]
        capital=capitals[state]
        question=f"What is the capital of {state}?"
        answer=input(question)
        if answer.lower()=="quit":
            break
        elif answer.lower()==capital.lower():
            print("That is correct!")
            right+=1
        else:
            print("That's not right!")
            print("The correct answer was",capital)
        del capitals[state]
        runs+=1
    percentage=(right/10)*100
    print(f"You got {percentage:.2f}% correct.")
    if percentage==100:
        print("Perfect! Great job!")
    elif percentage>60:
        print("That's almost all of them! Not bad!")
    elif percentage==50:
        print("Only half? C'mon now.")
    elif percentage<50:
        print("Did you pass 5th grade? Try again...")
    
    
main()

