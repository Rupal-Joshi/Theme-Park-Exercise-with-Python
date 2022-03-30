from time import sleep
from tqdm import tqdm
import time
import datetime

def typewrite(text, delay):
    for character in f"{text}\n":
        print(character, end="", flush=True)
        sleep(delay)

ticket = True

name=input("please enter lead bookers last name: ")

reset = "\033[0m"

text_black = "\033[30m"
text_red = "\033[31m"

bg_red = "\033[41m"
bg_green = "\033[42m"
bg_gold="033[43m"

text_black_bg_red = "\033[30;41m"
text_black_bg_gold="\033[30;43m"

print(" \033{4m Copington Theme Park \033{0m ")

print(
f"""{bg_red}{text_black}
🎉🎉🎉🎉🎉 WELCOME 🎉🎉🎉🎉🎉
    to the adventure park    
{reset}"""
)

typewrite(" \033{ \ The best theme park ever!\n" ,0.08)


print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
print ("Tickets available:" )
print("""
  🔴Adults(16+):     £40
  🔴Child(under 16): £20
  🔴Senior(65+):     £30\n
  🔴 admin fee:      £10


    Wristband(all):   £20

    parking:          Free
  """)

print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")

  
# Selecting tickets:
while ticket==True:
  try:
    ticket_num=int(input("\nhow many tickets would you like? max of 10: "))
    if ticket_num > 10:
      raise NameError
    adult_num=int(input("how many adult tickets would you like: "))
    child_num=int(input("how many child tickets would you like: "))
    senior_num=int(input("how many senior tickets would you like: "))
    if adult_num + child_num + senior_num != ticket_num:
      raise NameError
    ticket = False
  except ValueError:
    print("\033[31mYou can ONLY use numbers!\033[0m")
  except NameError:
    print("\033[31mYou must enter a number in range!\033[0m")

# Calculate cost of tickets
calc1=adult_num*20
calc2=child_num*12
calc3=senior_num*11

total_tickets=calc1+calc2+calc3

# Wristbands:
wristband=input("would you also like a wristbands for rides y/N").lower()

if wristband=="y":
    wristbands=int(input("please enter how many wristbands you would like: "))
    wristbands_calc=wristbands*20
else:
    print("please continue, 0 wristbands ordered")
    wristbands_calc = 0

# Parking:
print()
parking_pass=input("free car parking is available, would you like a parking pass y/N").lower()
parking_total=0

# loading ticket bar
for i in tqdm([1,2,3]):
  time.sleep(0.3)

# total ticket fee:
total_payment = total_tickets + wristbands_calc + parking_total
total_fee= (f"""total_tickets: £{total_tickets}
wristband(s): £{wristbands_calc}
parking: £{parking_total}
Total: £{total_payment}
{reset}""")

print(total_fee)

# Payment
print("enter payment with £10 and £20 notes only, each note enterted will be counted")
remaining_balance = total_payment

while remaining_balance > 0:
  payment = input(">>> £")
  if payment == "10" or payment == "20":
    remaining_balance -= int(payment)
    print (f"£{remaining_balance} is remaining")
  else:
    print("Please enter £10 or £20 only")
  
print("Payment complete, no outstanding fee remaining. Change will now be calculated.")

#loading ticket info 2
for i in tqdm([1,2,3]):
  time.sleep(0.3)

# Calculate change
change = -remaining_balance
print(f"You will now receive £{change}.")

#printing complete tickets
print(f"""
{text_black_bg_gold}ticket booked for {name}, tickets purchased include: 
Adult: {adult_num}, 
Child: {child_num}, 
Senior: {senior_num}, 
Wristbands purchased: {wristband}{reset}""")

now=datetime.datetime.now()
print("Current date and time is: ")
print(now.strftime("%y-%m-%d %H: %M: %H"))

print("thank you for your purchase")
