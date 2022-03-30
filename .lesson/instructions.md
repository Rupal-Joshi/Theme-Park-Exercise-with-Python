# Instructions  

Copington Adventure Theme Park has just purchased an automated ticketing system and would like you to program the interface for customers to use. The ticketing system should ask the customer various questions about their visit requirements before it provides a total charge, asks for payment, and issues a ticket. 

The program should:

- Provide a welcome message
- Display the entrance ticket prices
- Ask how many adult tickets are required
- Ask how many child tickets are required
- Ask how many senior citizen tickets are required
- Ask how many of the visitors would like wristbands for the rides
- Ask for the lead booker surname (for the ticket)
- Ask if they require a parking pass for the car park
- Display the total cost
- Ask for payment (the machine only accepts £10 and £20 notes, each note entered will need to be counted)
- Display change (if any)
- Print a ticket (display lead booker surname, tickets purchased, wristbands purchased, today’s date*)
- Print a car parking pass (if requested)
- Use data validation techniques to avoid runtime errors through incorrect data entry 
- Thank the customer for their purchase

\* You will need to investigate how to add today's date to the ticket.

A structure chart has already been created for the automated ticket machine to help you begin your design. This is available in the workbook.

Use pseudocode or a flowchart to design the algorithm for the program. 

Think carefully about what will be needed in the main program and in each function. 

You should iteratively test your program as you create it. This should help you to quickly find and fix any syntax, logic, or runtime errors. You should then perform final testing by completing the test table (in the workbook) to ensure that all aspects of your program are functioning correctly. 

## Explorer Task

- The program should continue to run until the machine is switched off at the end of the day. It should sit and wait for the next customer once the current customer has finished. Add additional functionality to your program to allow this to happen. 
- The maximum capacity for the theme park is 500. The program should track the amount of tickets that have been sold and not allow more tickets to be purchased if the visitor limit is reached. 
- The manager would like to be able to modify the ticket prices through an ‘admin’ feature. They should be able to type a code at the beginning of the program to access the admin feature. 
