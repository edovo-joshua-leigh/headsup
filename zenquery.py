import zenpy

creds = {
        'email' : 'joshua.leigh@edovo.com',
        'token' : '',
        'subdomain' : 'edovo'
}

zenpy_client = zenpy.Zenpy(**creds)

def search_for(status):
    search = zenpy_client.search(status=status, type='ticket', sort_by='created_at', brand_id=2209347)
    return search

def print_results(search, label):
    print()
    print(label + " tickets (" + str(search.count) + ")" )
    print("Ticket | Status | Subject | last comment")
    print("-----------------------------------------------")
    for ticket in search:
        print(str(ticket.id) + " | " + ticket.status + " | " + short(ticket.subject) + " | " + get_last_comment(ticket))
    print()

def get_last_comment(ticket):
    last_comment_long=zenpy_client.tickets.comments(ticket=ticket)[:][-1].body
    last_comment=last_comment_long[0:60] + "..."
    return last_comment.replace('\n',' ')

def short(long_string):
    abrev=long_string[0:40] + "..."
    return abrev

open_tickets_search = search_for("open")
new_tickets_search = search_for("new")
pending_tickets_search = search_for("pending")
hold_tickets_search = search_for("hold")

print_results(open_tickets_search, label="Open")
print_results(new_tickets_search, label="New")
print_results(pending_tickets_search, label="Pending")
print_results(hold_tickets_search, label="Hold")

