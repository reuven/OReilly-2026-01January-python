def menu(choices):
    while True:
        user_choice = input(f'Enter your choice ({choices}): ').strip()
    
        if user_choice in choices:    # did the user choose something in choices?
            return user_choice        # return their choice

        print(f'Illegal choice; try again!')

s = menu(['a', 'b', 'c'])
print(f'User chose {s}')
