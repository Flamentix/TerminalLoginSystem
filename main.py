from database.login import *
from getpass import *

if __name__ == '__main__':
    login = input('Do you want to test this login script?').lower().strip()
    if login == 'yes':
        sign = input('Do you have an account?').lower().strip()
        if sign == 'yes':
            username = input("What's your username?")
            password = str(getpass("What's your password?"))
            check = CheckLogin(username, password)
            try:
                if check[0] == True:
                    print("\nYou've successfully logged in.")
                    print('Your username is {u}.'.format(u=check[1]))
                else:
                    print('A fatal error has occured.')
            except TypeError:
                if check == False:
                    print("\nYour username or password was incorrect.")
                else:
                    print('A fatal error has occured.')
        elif sign == 'no':
            errors = ''
            make_new = input('Do you want to create a new account?').lower().strip()
            if make_new == 'yes':
                print('\nEnter quit to stop at any time.\n')
                while errors != None:
                    username = input('What do you want your username to be? ').strip()
                    username = username.replace(" ", "")
                    if username.strip().lower() == 'quit':
                        print('Goodbye!')
                        break
                    password = str(getpass("What do you want your password to be?"))
                    if password.strip().lower() == 'quit':
                        print('Goodbye!')
                        break
                    errors = AppendLogin(username, password)
                    if errors == 1:
                        print("----\nSorry, you can't have symbols other than '_' or '.' in your username.\n----")
                    elif errors == 2:
                        print("----\nSorry, the '}' symbol cannot be in your password.\n----")
                    elif errors == 3:
                        print("----\nSorry, that username is already taken!\n----")
                    elif errors == 4:
                        print("----\nSorry, your username should be between 6 to 12 characters.\n----")
                    elif errors == 5:
                        print("----\nSorry, your password should be between 8 to 20 characters.\n----")
                    else:
                        print('\nYour username is {u}. Any spaces present were removed.'.format(u=username))
                        print('Thanks for signing up. Re-execute the code to login.')

                        break
                else:
                    print('\nThanks for running our program.')
        else:
            print('\nYour answer is invalid.')
            pass
    elif login == 'no':
        pass
    else:
        print('\nYour answer is invalid.')
        pass

    #--Functions--#
