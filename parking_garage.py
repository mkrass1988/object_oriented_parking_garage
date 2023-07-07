class ParkingGarage():

    def __init__(self):
        self.tickets = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        self.currentTicket = {}
        self.parkingSpaces = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
        self.taken_tickets = []
        self.taken_spaces = []

    def takeTicket(self):
        if len(self.tickets) == 0:
            print('\nSorry, you cannot park here, please try again later')
        else: 
            print('\nTo park here you must take a ticket')
            ticket = input("\nPress [1] to take a ticket, press [2] to quit and leave: ")
            if ticket == '1':
                self.taken_tickets.append(self.tickets.pop(0))
                self.taken_spaces.append(self.parkingSpaces.pop(0))
                print('\nYou have ticket number ' + self.taken_tickets[-1])
                print('You have parking space letter ' + self.taken_spaces[-1])
                print('\nPlease enter your car information')
                self.color = input('What color is your vehicle?: ')
                self.car_type = input('\nWhat is your car make? (ex. BMW, Honda, Toyota, etc): ')
                print('\nPlease proceed to spot ' + self.taken_spaces[-1])
                self.currentTicket[self.taken_spaces[-1]] = {
                    'color': self.color,
                    'make': self.car_type,
                    'ticket_number': self.taken_tickets[-1],
                    'parking_space': self.taken_spaces[-1],
                    'paid': False,
                }
                print('\nHere is your information on your vehicle: ')
                print(self.currentTicket[self.taken_spaces[-1]])

            elif ticket == '2':
                print('\nHope to see you another time')
            else:
                print('\nInvalid entry, please enter [1] or [2]')

    def payForParking(self):
        try:
            self.payment = input("\nHow much will you pay for parking? ")
            self.payment = int(self.payment)
            while self.payment == 0:
                print("\nYou must give an amount to pay or you cannot leave!")
                self.payment = input("How much will you pay for parking? ")
                self.payment = int(self.payment)
            print('\nYour ticket has been paid, you have 15 min to leave')
            while True:
                self.key = input('\nWhich parking space did you have? ')
                if self.key.upper() in self.currentTicket:
                    self.currentTicket[self.key.upper()]['paid'] = True
                    print(self.currentTicket[self.key.upper()])
                    break
                else:
                    print('\nIncorrect entry, please enter the correct parking space')
        except:
            print('\nInvalid Entry, please enter an amount to pay as an integer')
            
    def leaveGarage(self):
        print('\nIf you want to leave the Garage, I just need to make sure you have paid')
        self.key1 = input('Which parking space did you have? ')
        if self.currentTicket[self.key1.upper()]['paid'] == True:
            self.ticket_number = self.currentTicket[self.key1.upper()]['ticket_number']
            self.parking_space = self.currentTicket[self.key1.upper()]['parking_space']
            self.tickets.append(self.ticket_number)
            self.parkingSpaces.append(self.parking_space)
            print("\nThank you, have a nice day")
            del self.currentTicket[self.key1.upper()]
        else:
            print('\nYou have not paid for parking yet, please pay and then you can leave!')

KrassGarage = ParkingGarage()

while True:
    garage = input('\nWelcome to the Garage, what would you like to do? \nPress [T] to take a ticket \nPress [P] to pay\nPress [L] to leave the garage\nPress [Q] to quit: ')
    if garage.lower() == 't':
        KrassGarage.takeTicket()
    elif garage.lower() == 'p':
        KrassGarage.payForParking()
    elif garage.lower() == 'l':
        KrassGarage.leaveGarage()
    elif garage.lower() == 'q':
        print("\nThank you, have a nice day")
        break



