#!/usr/bin/env python3.6
from password import User
def create_account(user_name,email,password):
    '''
    Function to create a new account
    '''
    new_account = User(user_name,email,password)
    return new_account
def save_accounts(account):
    '''
    Function to save accountt
    '''
    account.save_account()
def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()
def find_user_name(user_name):
    '''
    Function that finds an account by number and returns the account
    '''
    return User.find_by_user_name(user_name)
def check_existing_accounts(user_name):
    '''
    Function that check if an account exists with that number and return a Boolean
    '''
    return User.account_exist(user_name)
def display_accounts():
    '''
    Function that returns all the saved account
    '''
    return User.display_accounts()
def delete_account():
    '''
    Function that delete the saved account
    '''
    return User.delete_account()   

def main():
    print("Hello Welcome to your account list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
             print("Use these short codes : cc - create a new account, dc - display account, fc -find an account, ex -exit the account list, de -delete account ")

             short_code = input()

             if short_code == 'cc':
                         print("New Account")
                         print("-"*10)

                         print ("User Name ...")
                         user_name = input()


                         print("E-mail ...")
                         email = input()

                         print("password ...")
                         password = input()


                         save_accounts(create_account(user_name,email,password)) # create and save new contact.
                         print ('\n')
                         print(f"New account {user_name} {email} created")
                         print ('\n')

             elif short_code == 'dc':

                     if display_accounts():
                              print("Here is a list of all your accounts")
                              print('\n')

                              for account in display_accounts():
                                      print(f"{account.user_name} {account.email} .....{account.password}")

                                      print('\n')
                     else:
                                      print('\n')
                                      print("You dont seem to have any accounts saved yet")
                                      print('\n')

             elif short_code == 'fc':


                       print("Enter the user_name you want to search for")

                       search_user_name = input()

                       if check_existing_accounts(search_user_name):
                                search_account = find_user_name(search_user_name)
                                print(f"{search_account.user_name} {search_account.email}")
                                print('-' * 20)

                                print(f"password.......{search_account.password}")
                       else:
                                print("That account does not exist")
             elif short_code == 'de':
                       if delete_account():
                           for account in delete_account():
                                print("delete this account:"f"{search_account.user_name} {search_account.email}")
                                print('\n')
                       else:
                                print('\n')
                                print(f"{search_account.user_name}""the account is deleted")             
             elif short_code == 'ex':
                         print("Bye .......")
                         break
             else:
                         print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

 main()
