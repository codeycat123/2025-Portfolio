'''
Eden Wilson
CIS 113
18 November 2024
Purpose: Play a game of life with the user where they can buy houses, have kids, get paid, and experience events on the way to retirement on the 100th space. (Deliverable 2)
Algorithm attached to assignment
'''
import random
wealth=0
def main():
    global wealth
    print("Welcome to the game of life!")
    space=0
    mybabies=[]
    myhouses={}
    lastpayday=0
    salary=0
    debt=0
    vacations=0
    name=input("What is the name of your character?")
    wealth=1000
    #Allow the user to choose a career and set their salary
    print("E. Education: go into 40k debt but get a better job after graduating")
    print("C. Start your career now with low pay but no debt")
    edchoice="z"
    while edchoice.lower()!="c" and edchoice.lower()!="e":
            edchoice=input("Which do you choose? Enter E or C.")
    if edchoice.lower()=="c":
        space=11
        choice=displaymenu("career")
        if choice==1:
            salary=20000
        elif choice==2:
            salary=50000
        elif choice==3:
            salary=30000
        elif choice==4:
            salary=40000
        print("You have skipped the education part of the board and are now on space 11.")
    else:
        space=1
        debt=40000
        choice=displaymenu("education")
        if choice==1:
            salary=90000
        elif choice==2:
            salary=80000
        elif choice==3:
            salary=110000
        elif choice==4:
            salary=100000
        while space<11:
            input("Press enter to roll")
            roll=rolldie()
            if roll+space>11:
                print("Congratulations you've graduated and can now be paid!")
            else:
                print(f"You rolled a {roll} and landed on space {(roll+space)}/100. You are still in school and cannot be paid yet")
            space+=roll 

    #begin moving spaces
    lastpayday=0
    while space<100:
        input("Press enter to roll")
        roll=rolldie()
        if roll+space>100:
            space=100
        print(f"You rolled a {roll} and landed on space {(roll+space)}/100.")
        if roll+space>=100:
            endgame(mybabies, wealth, myhouses, vacations, debt,name)
        elif (roll+space)%8==0:
            print(f"It's payday! You've been paid your salary of ${salary}")
            wealth+=salary
            print(f"Your new balance is ${wealth}.")
            lastpayday=roll+space
        else:
            event=rolldie()
            if event==1:
                wealth-=unexpected_expense()
                if wealth<0:
                    wealth=0
                    debt+=(abs(wealth))
                    print(f"You had insufficient funds, so your balance is now ${wealth}. Your debt is ${debt}.")
                else:
                    print(f"Your balance is now ${wealth}.")
            elif event==2:
                houses = {"A cozy studio apartment in the heart of the city.": 100000,
                            "A small suburban house with two bedrooms and a backyard.": 150000,
                            "A modern one-bedroom condo with a balcony and city views.": 200000,
                            "A charming three-bedroom cottage near the countryside.": 250000,
                            "A spacious four-bedroom family home with a large garden.": 300000,
                            "A luxurious penthouse with three bedrooms and a rooftop pool.": 500000,
                            "A historic two-bedroom townhouse in a quaint neighborhood.": 220000,
                            "A beachside villa with five bedrooms and ocean views.": 800000,
                            "A rustic cabin in the mountains with a wood-burning fireplace.": 180000,
                            "A futuristic smart home with six bedrooms and cutting-edge technology.": 1000000,
                            "A minimalist tiny home in a serene forest setting.": 120000,
                            "A lavish mansion with a private theater and ten bedrooms.": 2000000,
                            "A quaint lakefront cottage with a dock and stunning sunsets.": 350000,
                            "A high-rise loft apartment with panoramic city skyline views.": 400000,
                            "An eco-friendly home with solar panels and sustainable features.": 280000
                            }
                newhouse=buy_house(myhouses)
                if newhouse!=None:
                    myhouses[newhouse]=houses[newhouse]
                    print("Congrats! You bought the house!")
                    print(f"Your balance is now ${wealth}.") 
            elif event==3:
                wealth+=win_prize()
                print(f"Your balance is now ${wealth}.")
            elif event==4:
                wealth-=vacation()
                if wealth<0:
                    wealth=0
                    debt+=(abs(wealth))
                    print(f"You had insufficient funds, so your balance is now ${wealth}. Your debt is ${debt}.")
                else:
                    print(f"Your balance is now ${wealth}.")
                    vacations+=1
            elif event==5:
                mybabies.append(have_baby())
                wealth-=50
                if wealth<0:
                    wealth=0
                    debt+=(abs(wealth))
                    print(f"Hospital bills were $50. You had insufficient funds, so your balance is now ${wealth}. Your debt is ${debt}.")
                else:
                    print(f"Hospital bills were $50. Your balance is now ${wealth}.")
    
            elif event==6:
                salary=promotion(salary)
            if (roll+space)-lastpayday>=8:
                print(f"It's payday! You've been paid your salary of ${salary}.")
                wealth+=salary
                print(f"Your new balance is ${wealth}.")
                lastpayday=((roll+space)//8)*8
        space+=roll
def unexpected_expense():
    cost=random.randint(100,1000)
    events=[f"Uh oh. Your car broke down! You must pay ${cost} to continue. Press enter to pay.",
            f"Surprise! That Nigerian prince in your email scammed you and you owe the bank ${cost}. Press enter to pay.",
            f"Darn! You broke your leg and have to pay a hospital bill of ${cost}. Press enter to pay.",
            f"You enter a dog show and have to pay a fee of ${cost}. Fluffy won! Press enter to pay.",
            f"It's the annual Children's Charity Ball! You donated ${cost}. Press enter to pay.",
            f"It's Thanksgiving! Ingredients cost ${cost}. Press enter to pay." ]
    event=events[rolldie()-1]
    input(event)
    return cost
def buy_house(myhouses):
    global wealth
    houses = {
    "A cozy studio apartment in the heart of the city.": 100000,
    "A small suburban house with two bedrooms and a backyard.": 150000,
    "A modern one-bedroom condo with a balcony and city views.": 200000,
    "A charming three-bedroom cottage near the countryside.": 250000,
    "A spacious four-bedroom family home with a large garden.": 300000,
    "A luxurious penthouse with three bedrooms and a rooftop pool.": 500000,
    "A historic two-bedroom townhouse in a quaint neighborhood.": 220000,
    "A beachside villa with five bedrooms and ocean views.": 800000,
    "A rustic cabin in the mountains with a wood-burning fireplace.": 180000,
    "A futuristic smart home with six bedrooms and cutting-edge technology.": 1000000,
    "A minimalist tiny home in a serene forest setting.": 120000,
    "A lavish mansion with a private theater and ten bedrooms.": 2000000,
    "A quaint lakefront cottage with a dock and stunning sunsets.": 350000,
    "A high-rise loft apartment with panoramic city skyline views.": 400000,
    "An eco-friendly home with solar panels and sustainable features.": 280000
    }
    myhouses=set(myhouses.keys())
    housesSet=set(houses)
    availables=housesSet.difference(myhouses)
    availables=list(availables)
    random.shuffle(availables)
    while len(availables)>3:
        availables.pop()
    num=1
    print("It's time to buy a house! Here are your options:")
    for x in availables:
        print(f"{num}. {x} \t${houses[x]}")
        num+=1
    print("4. None")
    answer=""
    while answer!="1" and answer!="2" and answer!="3" and answer!="4":
        answer=input("Which house would you like to buy? (Enter 1-4)")
    answer=int(answer)
    if answer==4:
        return None
    price=houses[availables[answer-1]]
    if wealth>=price:
        wealth-=houses[availables[answer-1]]
        return availables[answer-1]
    else:
        print("You don't have enough money. Try again next time.")
        return None    

def win_prize():
    prize=random.randint(100,1000)
    events=[f"You won the lottery and got ${prize}! Press enter to accept.",
            f"Merry Christmas! Your grandma gave you ${prize}. Press enter to accept.",
            f"Tax refund! You got ${prize}. Press enter to accept.",
            f"You won a pie eating contest and got ${prize}! Press enter to accept.",
            f"You won a halloween costume contest and got ${prize}! Press enter to accept.",
            f"You won a game of Uno and got ${prize}! Press enter to accept." ]
    event=events[rolldie()-1]
    input(event)
    return prize
def vacation():
    print("Time to go on vacation!")
    vacations = [
    "relax on the sunny beaches of Hawaii.",
    "explore the ancient ruins of Rome.",
    "go on a thrilling safari in Kenya.",
    "ski the snowy slopes of the Swiss Alps.",
    "take a road trip across the United States.",
    "cruise through the Caribbean islands."]
    vacationchosen=vacations[rolldie()]
    print("You went on a vacation to",vacationchosen)
    price=random.randint(100,1000)
    print(f"Your vacation cost ${price}.")
    return price
    
    
def have_baby():
    baby=[]
    print("You're having a baby!")
    input("Press enter to see if it's a boy or a girl.")
    gender=random.randint(1,2)
    if gender==1:
        baby.append("boy")
        print("It's a boy!")
    else:
        baby.append("girl")
        print("It's a girl!")
    name=input("What would you like to name your child?")
    baby.append(name)
    print(f"Congrats! You have a beautful baby {baby[0]} named {baby[1]}!")
    return baby
    
def promotion(salary):
    print("Congratulations! You got a promotion!")
    newpay=round(1.1*salary)
    print(f"Your salary increased by 10% from ${salary} to ${newpay}.")
    return newpay
def rolldie():
    return random.randint(1,6)
def endgame(mybabies, wealth, myhouses, vacations, debt,name):
    print(f"You reached retirement! Congrats {name}!")
    #babies
    if len(mybabies)>1:
        print(f"In your life, you had {len(mybabies)} children.")
        for x in range(len(mybabies)):
            if x==len(mybabies)-1:
                print(f"and a baby {mybabies[x][0]} named {mybabies[x][1]}.")
            else:
                print(f"A baby {mybabies[x][0]} named {mybabies[x][1]}")
    elif len(mybabies)==1:
        print(f"In your life, you had one baby {mybabies[0][0]} named {mybabies[0][1]}")
    else:
        print("You had no children.")
    #vacations
    print(f"You went on {vacations} vacations.")
    #houses
    propertyvalue=0
    if len(myhouses)>0:
        propertyvalue=sum(list(myhouses.values()))
        print(f"Your total property value is ${propertyvalue}.")
        print("Your houses:")
        for x in myhouses.keys():
            print(f"{x[:-1]} worth ${myhouses[x]}")
    else:
        print("You had no houses.")
    #debt
            
    finalwealth=wealth-debt
    print(f"You had ${debt} in debt and your final balance is ${finalwealth}")
    print(f"Your net worth is ${finalwealth+propertyvalue}")
    print("What a great life! Thank you for playing!")
def displaymenu(event):
    if event=="career":
        choice=0
        print("1. Hairdresser - 20k")
        print("2. Police - 50k")
        print("3. Musician - 30k")
        print("4. Secretary - 40k")
        while choice!="1" and choice!="2" and choice!="3" and choice!="4": 
            choice=(input("Please choose a job (Enter a number 1-4)"))
        return int(choice)  
    elif event=="education":
        choice=0
        print("1. Teacher - 90k")
        print("2. Social Worker - 80k")
        print("3. Entrepreneur - 110k")
        print("4. Lawyer - 100k")
        while choice!="1" and choice!="2" and choice!="3" and choice!="4":
            choice=(input("Please choose a job (Enter a number 1-4)"))
        return int(choice) 
main()
