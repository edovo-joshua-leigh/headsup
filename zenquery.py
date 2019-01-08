import zenpy

creds = {
        'email' : 'joshua.leigh@edovo.com',
        'token' : 'R1kSdprZ0k8obqp5ETVF9O2MOOYyrY4IxsriSOxV',
        'subdomain' : 'edovo'
}

zenpy_client = zenpy.Zenpy(**creds)

ticket_search = zenpy_client.search(status='open', brand_id=2209347)
open_ticket_ids=[]
for ticket in ticket_search:
    open_ticket_ids.append(ticket.id)

#print(open_ticket_ids)

class Ticket(object):
    """
    A ticket with the attributes of
    - number / name
    - description / subject
    - latest comment
    """

    def __init__(self, number):
        self.id = number
        self.subject = zenpy_client.tickets(id=number).subject
        self.last_comment = zenpy_client.tickets.comments(ticket=number)[:][-1].body

open_tickets={}
for id in open_ticket_ids:
    open_tickets[id] = Ticket(id)

print("Ticket | Subject")
print("---------------------------------------------------")
for ticket in open_tickets:
    print(str(open_tickets[ticket].id) + "  | " + str(open_tickets[ticket].subject))
