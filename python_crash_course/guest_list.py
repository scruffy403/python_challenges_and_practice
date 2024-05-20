def print_guest_list(list):
    for name in list:
        print(f"Hello, {name.title()}. I would like to invite you to dinner\n")
        
def send_guests_message(list, message):
    for name in list:
        print(f"Dear, {name.title()}. {message}\n")
        
guest_list = ['cesar chavez', 'bishop romero', 'ram dass']
print_guest_list(guest_list)

cancelled_guest = guest_list.pop(0)
print(f"{cancelled_guest.title()} can't make it anymore!\n")

guest_list.insert(0, 'alan watts')
print_guest_list(guest_list)
bigger_table = "A bigger table has been found. A new set of invitations will be sent shorlty.\n"

send_guests_message(guest_list, bigger_table)
guest_list.insert(0, 'keanu reeves')
guest_list.insert(-1, 'colin powell')
guest_list.insert(2, 'maya angelou')

print_guest_list(guest_list)

while len(guest_list) > 2:
    postpone_guest = guest_list.pop()
    print(f"Dear, {postpone_guest.title()}, I am very sorry, but I will have to postpone dinner plans with you!\n")
    
print_guest_list(guest_list)
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)
