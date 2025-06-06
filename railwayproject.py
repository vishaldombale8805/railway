trains = [
    {"name": "Rajdhani Express", "from": "Mumbai", "to": "Delhi", "Time": "10:30 AM", "Price": 1500, "seats": 10},
    {"name": "Shatabdi Express", "from": "Pune", "to": "Chennai", "Time": "9:30 AM", "Price": 1800, "seats": 8},
    {"name": "Duronto Express", "from": "Hyderabad", "to": "Kolkata", "Time": "8:30 AM", "Price": 2000, "seats": 25},
    {"name": "Garib Rath", "from": "Delhi", "to": "Lucknow", "Time": "11:30 AM", "Price": 800, "seats": 15}
]

last_payment_method = None
booked_tickets = []


class Ticket:
    def __init__(self, name, age, email, seats, train_name, source, destination, time, price, total, payment_method, travel_class ,Passenger_Id):
        self.name = name
        self.age = age
        self.email = email
        self.seats = seats
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.time = time
        self.price = price
        self.total = total
        self.payment_method = payment_method
        self.travel_class = travel_class
        self.Passenger_Id = Passenger_Id


    def display(self):
        print("\n TICKET BOOKED SUCCESSFULLY")
        print("-----------------------------------")
        print("Passenger Name :", self.name)
        print("Age            :", self.age)
        print("Email          :", self.email)
        print("Train          :", self.train_name)
        print("From           :", self.source)
        print("To             :", self.destination)
        print("Time           :", self.time)
        print("Class          :", self.travel_class)
        print("Seats Booked   :", self.seats)
        print("Passenger_Id   :",",".join(self.Passenger_Id))
        print("Price per Seat :", self.price)
        print("Total Price    :", self.total)
        print("Payment Method :", self.payment_method)
        print(" ThankYou Happy Journey \n")


def show_trains():
    print("\n Available Trains:")
    for i, train in enumerate(trains, 1):
        print(f"{i}. {train['name']} - {train['from']} to {train['to']} | Time: {train['Time']} | Price: ₹{train['Price']} | Seats: {train['seats']}")


def book_ticket():
    global last_payment_method
    show_trains()
    choice = input("\nEnter train number to book (1 to {}): ".format(len(trains)))

    if not choice.isdigit() or not (1 <= int(choice) <= len(trains)):
        print(" Invalid train number.\n")
        return

    train = trains[int(choice) - 1]

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    seats = int(input("Enter number of tickets: "))

    if seats > train["seats"]:
        print(" Not enough seats available.\n")
        return
    
    Passenger_Id = []
    if seats >= 2:
        print("You are booking more than 2 tickets. Enter ID for each passenger:")
        for i in range(seats):
            pid = input(f"Enter ID for passenger {i+1}: ")
            Passenger_Id.append(pid)
    else:
        pid=input(f"enter Id for passenger:")
        Passenger_Id.append(pid)    

    print("\nTravel Classes:")
    print("1. AC (40% extra)")
    print("2. Non-AC (20% extra)")
    print("3. General")
    class_choice = input("Choose class (1-3): ")

    if class_choice == "1":
        travel_class = "AC"
        price_per_seat = int(train["Price"] * 1.4)
    elif class_choice == "2":
        travel_class = "Non-AC"
        price_per_seat = int(train["Price"] * 1.2)
    elif class_choice == "3":
        travel_class = "General"
        price_per_seat = train["Price"]
    else:
        print(" Invalid class selection.\n")
        return

    total = price_per_seat * seats

    print("\nPayment Methods:")
    print("1. UPI")
    print("2. Cash")
    print("3. Card")
    payment_choice = input("Choose payment method (1-3): ")

    if payment_choice == "1":
        payment_method = "UPI"
    elif payment_choice == "2":
        payment_method = "Cash"
    elif payment_choice == "3":
        payment_method = "Card"
    else:
        print(" Invalid payment method.\n")
        return

    train["seats"] -= seats
    last_payment_method = payment_method

    ticket = Ticket(name, age, email, seats, train["name"], train["from"], train["to"], train["Time"],
                    price_per_seat, total, payment_method, travel_class ,Passenger_Id)
    booked_tickets.append(ticket)
    ticket.display()


def cancel_ticket():
    if not booked_tickets:
        print(" No bookings found.\n")
        return

    email = input("Enter your email to cancel ticket: ")

    for ticket in booked_tickets:
        if ticket.email == email:
            print(f"\nYou have booked {ticket.seats} seat(s) on {ticket.train_name}.")
            cancel_seats = int(input("How many seats do you want to cancel? "))

            if cancel_seats <= 0 or cancel_seats > ticket.seats:
                print(" Invalid number of seats to cancel.\n")
                return

            charge = cancel_seats * 100
            refund = (ticket.total / ticket.seats) * cancel_seats - charge

            print(f" Cancellation Charge: ₹{charge} (₹100 per seat)")
            print(f" Refund Amount: ₹{refund}")

            confirm = input("Confirm cancellation? (yes/no): ").lower()
            if confirm == "yes":
                for train in trains:
                    if train["name"] == ticket.train_name:
                        train["seats"] += cancel_seats

                if cancel_seats == ticket.seats:
                    booked_tickets.remove(ticket)
                    print(" All seats cancelled. Ticket removed.\n")
                else:
                    ticket.seats -= cancel_seats
                    ticket.total = ticket.seats * ticket.price
                    print(f" {cancel_seats} seat(s) cancelled. Updated ticket:")
                    ticket.display()
            else:
                print(" Cancellation aborted.\n")
            return

    print(" Ticket not found with given email.\n")


def main():
    while True:
        print("===== Train Ticket Booking System =====")
        print("1. View Trains")
        print("2. Book Ticket")
        print("3. View Last Payment Method")
        print("4. Cancel Ticket")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_trains()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            if last_payment_method:
                print("\n Last Payment Method Used:", last_payment_method, "\n")
            else:
                print("\n No payment has been made yet.\n")
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print(" Thank you for using Train Booking System! Goodbye.")
            break
        else:
            print(" Invalid choice. Please try again.\n")


# Start the program
main()
