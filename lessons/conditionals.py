"""Testing Conditionals with low card example"""

low_card: int = 2
current_card: int = 3

if current_card < low_card:
    low_card = current_card
else:
    print(str(current_card) + " is not the low card")
print("The low card is " + str(low_card))

my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print("Right")
else: 
    print("Wrong")
print("My number is " + str(my_number) + ".")