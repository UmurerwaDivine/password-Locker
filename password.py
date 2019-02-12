import pyperclip
class User:
    # """
    # Class that generates new instances of contacts
    # """
    account_list = []

    def __init__(self,user_name,email,password):
        

        # docstring removed for simplicity

        self.user_name = user_name
        self.email = email
        self.password = password

    def save_account(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.account_list.append(self)
        
        
    def delete_account(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.account_list.remove(self)
    @classmethod

    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for account in cls.account_list:
            if account.user_name == user_name:
                return account
    @classmethod
    def account_exist(cls,user_name):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.account_list:
            if account.user_name == user_name:
                    return True

        return False               
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.account_list   

    # @classmethod
    # def copy_email(cls,user_name):
    #     account_found = User.find_by_user_name(user_name)
    #     pyperclip.copy(account_found.email)             