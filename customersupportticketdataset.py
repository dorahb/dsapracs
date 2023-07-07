
DATA1 = """
Ticket ID,Customer Name,Customer Email,Customer Age,Product Purchased,Date of Purchase,Ticket Type,Ticket Subject,Ticket Status,Ticket Priority,Ticket Channel,First Response Time,Time to Resolution,Customer Satisfaction Rating
1,Marisa Obrien,carrollallison@example.com,32,GoPro Hero,2021-03-22,Technical issue,Product setup,Pending Customer Response,Critical,Social media,2023-06-01 12:15:36,,
2,Jessica Rios,clarkeashley@example.com,42,LG Smart TV,2021-05-22,Technical issue,Peripheral compatibility,Pending Customer Response,Critical,Chat,2023-06-01 16:45:38,,
3,Christopher Robbins,gonzalestracy@example.com,48,Dell XPS,2020-07-14,Technical issue,Network problem,Closed,Low,Social media,2023-06-01 11:14:38,2023-06-01 18:05:38,3.0
4,Christina Dillon,bradleyolson@example.org,27,Microsoft Office,2020-11-13,Billing inquiry,Account access,Closed,Low,Social media,2023-06-01 07:29:40,2023-06-01 01:57:40,3.0
5,Alexander Carroll,bradleymark@example.com,67,Autodesk AutoCAD,2020-02-04,Billing inquiry,Data loss,Closed,Low,Email,2023-06-01 00:12:42,2023-06-01 19:53:42,1.0
6,Rebecca Fleming,sheenasmith@example.com,53,Microsoft Office,2020-07-28,Cancellation request,Payment issue,Open,Low,Social media,,,
7,Jacqueline Wright,donaldkeith@example.org,24,Microsoft Surface,2020-02-23,Product inquiry,Refund request,Open,Critical,Social media,,,
8,Denise Lee,joelwilliams@example.com,23,Philips Hue Lights,2020-08-09,Refund request,Battery life,Open,Critical,Social media,,,
9,Nicolas Wilson,joshua24@example.com,60,Fitbit Versa Smartwatch,2020-07-16,Technical issue,Installation support,Pending Customer Response,Low,Social media,2023-06-01 10:32:47,,
10,William Dawson,clopez@example.com,27,Dyson Vacuum Cleaner,2020-03-06,Refund request,Payment issue,Pending Customer Response,Critical,Phone,2023-06-01 09:25:48,,
11,Joseph Moreno,mbrown@example.org,48,Nintendo Switch,2021-01-19,Cancellation request,Data loss,Closed,High,Phone,2023-06-01 17:46:49,2023-05-31 23:51:49,1.0
12,Brandon Arnold,davisjohn@example.net,51,Microsoft Xbox Controller,2021-10-24,Product inquiry,Software bug,Closed,High,Chat,2023-06-01 12:05:51,2023-06-01 09:27:51,1.0
13,Tamara Hahn,jensenwilliam@example.net,27,Nintendo Switch Pro Controller,2021-05-26,Technical issue,Hardware issue,Pending Customer Response,Low,Chat,2023-06-01 19:03:53,,
14,Sandra Barnes,gwendolyn51@example.net,65,Nest Thermostat,2020-07-13,Technical issue,Product setup,Pending Customer Response,Low,Chat,2023-06-01 20:34:54,,
15,Amy Hill,medinasteven@example.net,48,Sony PlayStation,2020-02-29,Billing inquiry,Product setup,Closed,High,Chat,2023-06-01 06:22:55,2023-05-31 23:08:55,4.0
16,Elizabeth Foley,amy41@example.net,18,GoPro Action Camera,2021-06-24,Billing inquiry,Product recommendation,Pending Customer Response,High,Social media,2023-06-01 15:09:57,,
17,Julia Salazar,watkinsbarbara@example.com,63,Xbox,2021-10-13,Product inquiry,Account access,Closed,Critical,Chat,2023-06-01 19:46:59,2023-06-01 15:58:59,4.0
18,Joshua Castillo,mooredeborah@example.org,56,Microsoft Xbox Controller,2020-09-07,Product inquiry,Payment issue,Pending Customer Response,High,Chat,2023-06-01 21:05:01,,
19,Wendy Davis,brenda20@example.net,19,LG Washing Machine,2021-09-23,Product inquiry,Peripheral compatibility,Open,High,Social media,,,
20,Jeffrey Robertson,jameslopez@example.com,39,Canon EOS,2021-03-08,Refund request,Software bug,Closed,Low,Chat,2023-06-01 00:46:04,2023-06-01 20:29:04,5.0
"""


# rows = DATA1.strip().split('\n')
# title = rows[0]   
# rest_of_data = rows[1:]

# parsed_data = []

# for row in rest_of_data:
#     row_keys = title.split(',')
#     row_values = row.split(',')
#     row_dict = dict(zip(row_keys, row_values))
#     parsed_data.append(row_dict)
# # print(parsed_data)

# # (1) What is the most common ticket type in the data set?

# ticket_types_frequency = {}

# for row in parsed_data:
#     ticket_type = row['Ticket Type']
#     if ticket_type in ticket_types_frequency:
#         ticket_types_frequency[ticket_type] += 1
#     else:
#         ticket_types_frequency[ticket_type] = 1
  
# most_common_ticket_type = max(ticket_types_frequency, key=lambda x: ticket_types_frequency[x])
# print('The most common ticket type is:', most_common_ticket_type)
   
    

# # (2) What are the IDs of the tickets that are still unresolved?

# ids_of_unresolved_tickets = []

# for row in parsed_data:
#     ticket_id = row['Ticket ID']
#     ticket_status = row ['Ticket Status']
#     if ticket_status != 'Closed':
#         ids_of_unresolved_tickets.append(ticket_id)

# print("The IDs of the tickets that are still unresolved are:", ids_of_unresolved_tickets)


# # (3) Excluding tickets with no first response, what is the average first response time for "critical" priority tickets?

# tickets_response_time = 0
# tickets_count = 0

# for row in parsed_data:
#     first_response_time = row ['First Response Time']
#     ticket_priority = row['Ticket Priority']
    
#     if first_response_time:
#         if ticket_priority == 'Critical':
#             tickets_response_time +=1
#             tickets_count +=1
        
# if tickets_count > 0:
#     average_first_response_time = tickets_response_time/tickets_count
#     print('The average first response time for critical priority tickets', average_first_response_time)


def extract_customer_support_ticket(dataset):
    rows = dataset.strip().split('\n')
    title = rows[0]
    rest_of_data = rows[1:]

    parsed_data = []

    for row in rest_of_data:
        row_keys = title.split(',')
        row_values = row.split(',')
        row_dict = dict(zip(row_keys, row_values))
        parsed_data.append(row_dict)

    return parsed_data
    
# (1) What is the most common ticket type in the data set?

def most_common_ticket_type(dataset):
    ticket_types_frequency = {}

    for row in dataset:
        ticket_type = row['Ticket Type']
        if ticket_type in ticket_types_frequency:
            ticket_types_frequency[ticket_type] += 1
        else:
            ticket_types_frequency[ticket_type] = 1

    most_common_ticket_type = max(ticket_types_frequency, key=lambda x: ticket_types_frequency[x])
    return most_common_ticket_type

common_ticket = most_common_ticket_type(extract_customer_support_ticket(DATA1))
print('The most common ticket type is:',common_ticket)

# (2) What are the IDs of the tickets that are still unresolved?

def unresolved_ticket_ids(dataset):
    ids_of_unresolved_tickets = []

    for row in dataset:
        ticket_id = row['Ticket ID']
        ticket_status = row['Ticket Status']
        if ticket_status != 'Closed':
            ids_of_unresolved_tickets.append(ticket_id)

    return ids_of_unresolved_tickets

unresolved = unresolved_ticket_ids(extract_customer_support_ticket(DATA1))
print("The IDs of the tickets that are still unresolved are:",unresolved)

# (3) Excluding tickets with no first response, what is the average first response time for "critical" priority tickets?

def average_first_response_time(dataset):
    tickets_response_time = 0
    tickets_count = 0

    for row in dataset:
        first_response_time = row ['First Response Time']
        ticket_priority = row['Ticket Priority']
    
        if first_response_time:
            if ticket_priority == 'Critical':
                tickets_response_time +=1
                tickets_count +=1
        
    if tickets_count > 0:
        average_first_response_time = tickets_response_time/tickets_count
        return average_first_response_time
        
average = average_first_response_time(extract_customer_support_ticket(DATA1))
print('The average first response time for critical priority tickets:',average)