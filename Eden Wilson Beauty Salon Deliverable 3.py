"""
Eden Wilson
CIS 113
October 13 2024
Beauty Shop Deliverable 3
Full Project Algorithm:
1. Initialize lists containing beauty shop data, baseprices, styles, addOns, and addOnsMenuPrices,contianing styles names, addons and prices,
2. Welcome the user
3. Print the menu
    Around the way curl ($55.99)
    Silk Press ($65.50)
    Two Strand Twists ($85.00)
    Wash and Go ($55.99)
    Crochet Faux Locs ($199.99)
4. Take input from the user to choose a style and make sure it is between 1-5, else ask the question again
5. Add style price to subtotal and save style price in styleprice and style name in stylename variable
6. Initialize addOnNames and addOnPrices to store the corresponding names and prices of add ons later
7. Start new while loop using the selection2 variable, while selection2!=6, initializing it as selection2=-1
8. Print extra services menu
    Trim (requires Two Strand Twists or Silk Press ($15)
    Deep conditioning mask ($20)
    Detangling ($15)
    Steam treatment (requires around the way curl or wash and go) ($35)
    Take down service (requires Crochet Faux Locs) ($50)
    Done
9. Repeat displaying menu and asking for choice until the user enters 6 for done. If not 1-6, repeat the question
10. When the user enters 6 for done, break.
11. If choice does not correspond to style, print that they must have a different style and to try again
12. For each choice, add style name to addOnNames, add its price to the subtotal, and add the price to the addOnPrices list
13. request tip amount but validate the input to be positive so the user can't reduce their subtotal
14. Print original style name from stylename variable and price from styleprice variable
15. for x in range 0 to length of addOnNames, print out the add on name addOnNames[x] and addOnPrices[x] for the receipt
16. Print subtotal with tip and total
"""
#initialize menu style, price, and add on data
baseprices=[55.99,65.50,85.00,55.99,199.99]
styles=["Around the Way Curl","Silk Press","Two Strand Twists","Wash and Go","Crochet Faux Locs"]
addOns=["Trim","Deep conditioning mask","Detangling","Steam treatment","Take down service"]
addOnsMenuPrices=[15.00,20.00,15.00,35.00,50.00]
print("Welcome to Curlicious salon!")
#get base style from user using menu
selection=-1
while (selection<1 or selection>5):
    #print style menu
    print("Please select one of our signature styles.")
    print("1. Around the way curl ($55.99)")
    print("2. Silk Press ($65.50)")
    print("3. Two Strand Twists ($85.00)")
    print("4. Wash and Go ($55.99)")
    print("5. Crochet Faux Locs ($199.99)")
    selection=int(input("Please choose a style(1-5): "))
    #validate input
    if selection<1 or selection>5 :
        print("Please enter a menu option from 1-5")

#add style price to subtotal and save style name and price
subtotal=baseprices[selection-1]
styleprice=baseprices[selection-1]
stylename=styles[selection-1]
print(f"Selection: {stylename}")
#initialize add on lists
addOnNames=[]
addOnPrices=[]
#get add ons from user using menu
selection2=-1
while (selection2!=6):
    #print style menu
    print("Feel free to select any add-ons:")
    print("1. Trim (requires Two Strand Twists or Silk Press)($15)")
    print("2. Deep conditioning mask ($20)")
    print("3. Detangling ($85.00)")
    print("4. Steam treatment (requires around the way curl or wash and go)($55.99)")
    print("5. Take down service (Requires faux locs) ($199.99)")
    print("6. Done")
    selection2=int(input("Any extras?"))
    if selection2==6:
        break
    #validate input
    if selection2<1 or selection2>6:
        print("Please enter a menu option from 1-6")
    else:
        if selection2==1 and (selection!=2 and selection!=3):
            #they chose trim and the style was NOT two strand twist or silk press
            print("This extra is only available with two strand twist or silk press.")
        elif selection2==4 and (selection!=1 and selection!=4):
            #they chose steam teatment and the style was NOT around the way curl or wash and go
            print("This extra is only available with the around the way curl or wash and go.")
        elif (selection2==5 and selection!=5):
            #they chose take down service and the style was NOT faux locs
            print("This extra is only available with faux locs.")
        else:
            addOnNames.append(addOns[selection2-1])
            addOnPrices.append(addOnsMenuPrices[selection2-1])
            subtotal+=addOnsMenuPrices[selection2-1]
            print(f"You've added {addOns[selection2-1]}.")
#final subtotal, tip, and total
print(f'Your subtotal is: ${subtotal:.2f}')
tip=-1
tip=float(input("How much would you like to tip? $"))
#make sure the tip isn't negative so the customer can't reduce their total
while tip<0:
    tip=float(input("The tip must be a positive number. How much would you like to tip? $"))
total=subtotal+tip
#print reciept
print("********Reciept*********")
print(f'Style: {stylename} (${styleprice:.2f})')
for x in range(0,len(addOnNames)):
    print(f'Extra: {addOnNames[x]} (${addOnPrices[x]:.2f})')
print(f'Subtotal: ${subtotal:.2f}\nTip: ${tip:.2f}\nTotal: ${total:.2f}')


