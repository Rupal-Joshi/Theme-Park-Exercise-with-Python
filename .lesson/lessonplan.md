# Lesson plan
  
The following code was provided originally:

```python
# Copington Adventure Theme Park has just purchased an automated ticketing system and would like you to program the interface for customers to use. The ticketing system should ask the customer various questions about their visit requirements before it provides a total charge, asks for payment, and issues a ticket. 
ADULT_PRICE = 20
CHILD_PRICE = 12
SENIOR_PRICE = 11
WRISTBAND_PRICE = 20

def display_prices():
  print(f"""
    {"-"*8} "PRICES" {"-"*8}
    Adult Ticket: £{ADULT_PRICE}
    Child Ticket: £{CHILD_PRICE}
    Senior Ticket: £{SENIOR_PRICE}

    Wristbands: £{WRISTBAND_PRICE}
    {"-"*26}
  """)

def ask_tickets():
  try:
    adult_num = int(input("How many adult tickets would you like?\t"))
    child_num = int(input("How many child tickets would you like?\t"))
    senior_num = int(input("How many senior tickets would you like?\t"))
    total_in_party = adult_num + child_num + senior_num
    wrist_num = int(input("How many wristbands would you like?\t"))
    if wrist_num not in [x for x in range(total_in_party+1)]:
      print("You can buy at most one wristband per person (up to " + str(total_in_party) + " for your party)")
  except ValueError:
    print("Please enter a number.\n\n")
    ask_tickets()

def more_questions():
  booker_name = input("Please enter the surname of the lead booker:\t")
  booker_name = booker_name.replace('-', '')
  if not booker_name.isalpha():
    print("Please enter a surname with no spaces.")
  
# The program should:

# Provide a welcome message
print("Welcome to Copington Adventure Theme Park!")
# Display the entrance ticket prices
display_prices()

# Ask how many adult tickets are required
# Ask how many child tickets are required
# Ask how many senior citizen tickets are required
# Ask how many of the visitors would like wristbands for the rides
ask_tickets()
# Ask for the lead booker surname (for the ticket)
# Ask if they require a parking pass for the car park
more_questions()
# Display the total cost

# Ask for payment (the machine only accepts £10 and £20 notes, each note entered will need to be counted)
# Display change (if any)

# Print a ticket (display lead booker surname, tickets purchased, wristbands purchased, today’s date*)
# Print a car parking pass (if requested)

# Use data validation techniques to avoid runtime errors through incorrect data entry 

# Thank the customer for their purchase

def ask_tickets():
  try:
    adult_num = int(input("How many adult tickets would you like?\t"))
  except ValueError:
    print("Please enter a number.\n\n")
    ask_tickets()
```
  