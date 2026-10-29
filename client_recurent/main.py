


def first_recurrent_client(orders : list, minimum : int) -> str:
    if len(orders) < 1: 
        return '-1'
    dictionary_client = {}
    min_orders = False
    for elements in orders: 
        client : str =  elements.get('client')
        client =  client.strip()
        client_uppered = client.upper()
        found_in_dict = False
        for member ,  number in dictionary_client.items():
            member_to_upper = member.upper()
            if member_to_upper == client_uppered :
                found_in_dict = True
                number += 1
                dictionary_client[member] = number
                if number >= minimum : 
                    min_orders = True
                    return member
        if found_in_dict == False:
            dictionary_client[client] = 1
    if min_orders == False: 
        return '-1'




                
            






data = [
    {'ref': 'S001', 'client': 'Azure Interior'},
    {'ref': 'S002', 'client': 'Deco Addict'},
    {'ref': 'S003', 'client': 'deco addict '},
    {'ref': 'S004', 'client': 'Azure Interior'},
    {'ref': 'S005', 'client': ' AZURE interior'}
]
data_2 = [
    {'ref': 'S001', 'client': 'Azure Interior'},
    {'ref': 'S002', 'client': 'Deco Addict'},
    {'ref': 'S003', 'client': 'deco addict '},
    {'ref': 'S004', 'client': 'Azure Interior'},
    {'ref': 'S005', 'client': ' AZURE interior'}
]
data_3 = [
    {'ref': 'S001', 'client': 'Azure Interior'},
    {'ref': 'S002', 'client': 'Deco Addict'},
    {'ref': 'S003', 'client': 'deco addict '},
    {'ref': 'S004', 'client': 'Azure Interior'},
    {'ref': 'S005', 'client': ' AZURE interior'}
]


print(first_recurrent_client(data_3, 4))