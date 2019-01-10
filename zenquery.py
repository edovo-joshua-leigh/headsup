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
    print()
    print("| Ticket | Status | Subject | last comment |")
    print("|---|---|---|---|")
    for ticket in search:
        print("| " + 
                str(ticket.id) + " | " + 
                ticket.status + " | " + 
                shorten(ticket.subject, 40) + " | " + 
                shorten(get_last_comment(ticket), 80) + " |")
    print()

def append_results(search, label):
    results=[]
    results.append("")
    results.append(label + " tickets (" + str(search.count) + ")" )
    results.append("")
    results.append("| Ticket | Status | Subject | last comment |")
    results.append("|---|---|---|---|")
    for ticket in search:
        results.append("| " + 
                str(ticket.id) + " | " + 
                ticket.status + " | " + 
                shorten(ticket.subject, 40) + " | " + 
                shorten(get_last_comment(ticket), 80) + " |")
    return results

def get_last_comment(ticket):
    last_comment=zenpy_client.tickets.comments(ticket=ticket)[:][-1].body
    return last_comment.replace('\n',' ')

def shorten(long_string, length):
    if len(long_string) > length:
        return long_string[0:length] + "..."
    else:
        return long_string

open_tickets_search = search_for("open")
new_tickets_search = search_for("new")
pending_tickets_search = search_for("pending")
hold_tickets_search = search_for("hold")

#print_results(open_tickets_search, label="Open")
#print_results(new_tickets_search, label="New")
#print_results(pending_tickets_search, label="Pending")
#print_results(hold_tickets_search, label="Hold")

#open tickets table
ott=append_results(open_tickets_search, label="Open")
#new tickets table
ntt=append_results(new_tickets_search, label="New")
#pending tickets table
ptt=append_results(pending_tickets_search, label="Pending")
#hold tickets table
htt=append_results(hold_tickets_search, label="Hold")
#all tickets table
att=ott + ntt + ptt + htt
with open('test.md', 'w') as w:
    for line in att:
        w.writelines(f"{line}\n")
#    print(line)

