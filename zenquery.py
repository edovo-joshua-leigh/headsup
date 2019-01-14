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

def shorten(long_string, length):
    if len(long_string) > length:
        return long_string[0:length] + "..."
    else:
        return long_string

def get_last_comment(ticket):
    last_comment=zenpy_client.tickets.comments(ticket=ticket)[:][-1].body
    return last_comment.replace('\n',' ')

def make_dict(search):
#    ticket_table={name: { "col": ["ticket", "subject", "comment"], "rows": [] }}
    new_dict={ "col": ["ticket", "subject", "comment"], "rows": [], "count": search.count }
    t_row=0
    for ticket in search:
#        print(ticket_table[name])
#        print(ticket_table[name]['rows'])
        new_dict['rows'].append([])
        new_dict['rows'][t_row].append(str(ticket.id))
        new_dict['rows'][t_row].append(shorten(ticket.subject,40))
        new_dict['rows'][t_row].append(shorten(get_last_comment(ticket),80))
        t_row+=1

#    print(ticket_table[name]['rows'][0])
#    print(f"number of {name} tickets: " + str((len(ticket_table[name]['rows']) -1)))
#    print(ticket_table)
#    return ticket_table
    return new_dict

def make_html_table(title, table):
#    html_string="<html>\n<table border='1'>\n"
#    print(table)
    html_string=f"<h1>{title} ({table['count']})</h1>"
    html_string+="\n<table border='1'>\n"
    html_string+="<tr>"
    for col in table['col']:
        html_string+=f"<th>{col}</th>"
    html_string+="</tr>\n"
    for row in table['rows']:
        html_string+="<tr>"
        for col in row:
            html_string+=f"<td>{col}</td>"
        html_string+="</tr>\n"
    html_string+="</table>\n"
    html_string+="<br/"
    html_string+="<hr>"
#    print(html_string)
    return html_string

def make_full_html_file(html_strings):
    html_text="<html>"
    for string in html_strings:
        html_text+=string
    html_text+="</html>"
#    print(html_text)
    with open('index.html', 'w') as w:
            w.write(html_text)

open_tickets_search = search_for("open")
open_tickets_table=make_dict(open_tickets_search)
new_tickets_search = search_for("new")
new_tickets_table=make_dict(new_tickets_search)
pending_tickets_search = search_for("pending")
pending_tickets_table=make_dict(pending_tickets_search)
hold_tickets_search = search_for("hold")
hold_tickets_table=make_dict(hold_tickets_search)
open_html_table=make_html_table("Open tickets", open_tickets_table)
new_html_table=make_html_table("New tickets", open_tickets_table)
pending_html_table=make_html_table("Pending tickets", pending_tickets_table)
hold_html_table=make_html_table("Hold tickets", hold_tickets_table)

all_tables_html=[open_html_table, new_html_table, pending_html_table, hold_html_table]

make_full_html_file(all_tables_html)
