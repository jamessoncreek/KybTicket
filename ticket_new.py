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
    ticketPassenger = f'\
    |                                  | Passenger: {passenger}                         |\n'
    ticketInfo = f'\
    | Estimated Departure: unknown    | Departure: unknown ===> Arrival: unknown    |\n\
    | Gate: unknown                         | Date and time: {date}             |\n\
    |                                  |                                            |\n\
    | Estimated Arrival Time: unknown |                                             |\n\
    | Gate: unknown                        | Class: unknown                         |\n\
    |                                  | Seat: unknown                              |\n\
    |_______________________________________________________________________________|\n\
    '
    readyTicket = ticketTitle+ticketPassenger+ticketInfo
    return readyTicket


date = datetime.date.today()
passenger = 'unknown'
out = ticket_generator(date, passenger)
print(out)
