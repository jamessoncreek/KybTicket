import datetime


def ticket_generator(date: datetime.date, passenger: str):
    print(date)
    print("Ticket is generating...\n")
    ticketTitle = '\
     _______________________________________________________________________________\n\
    | _   _ _     _ _____  _    _  _____   _____ _   _                              |\n\
    | |   /  \   /  |   |  |    | |     | |      |   /                              |\n\
    | |__/    \ /   |___/  |____| |_____| |      |__/  |    _ _ _  _ ___  ___       |\n\
    | |  \     |    |   \  |    | |     | |      |  \  |     |  |\ | |__ |__        |\n\
    | |   \    |    |____| |    | |     | |_____ |   \ |___ _|_ | \| |__ ___|       |\n\
    |===============================================================================|\n'
    ticketPassenger= f'\
    |                                  | Passenger: {passenger}                     |\n'
    ticketInfo=f'\
    | Estimated Departure: 07:15 AM    | Departure: Detroit ===> Arrival: New-York  |\n\
    | Gate: B5                         | Date and time: {date}                  |\n\
    |                                  |                                            |\n\
    | Estimated Arrival Time: 08:55 AM |                                            |\n\
    | Gate: A11                        | Class: First Class                         |\n\
    |                                  | Seat: 1D                                   |\n\
    |_______________________________________________________________________________|\n\
    '
    readyTicket = ticketTitle+ticketPassenger+ticketInfo
    return readyTicket


date = datetime.date.today()
passenger = 'James Creek'
out = ticket_generator(date, passenger)
print(out)