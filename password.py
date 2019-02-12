import pyperclip
class User:
    """
    Class that generates new instances of accounts
    """
    account_list = []

    def __init__(self,user_name,email,password):
        

        # docstring removed for simplicity

        self.user_name = user_name
        self.email = email
        self.password = password

    def save_account(self):

        '''
        save_account method saves d objects into account_list
        '''

        User.account_list.append(self)
        
        
    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        User.account_list.remove(self)
    @classmethod

    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a number and returns a account that matches that username.

        Args:
            username: user to search for
        Returns :
            account of person that matches the username.
        '''

        for account in cls.account_list:
            if account.user_name == user_name:
                return account
    @classmethod
    def account_exist(cls,user_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.user_name == user_name:
                    return True

        return False               
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list 
    # @classmethod
    # def delete_account(cls,self):
    #  for account_exist in cls.account_list: 
    #      if account_exist.user_name==user_name: 

    #          return True
    #          return False

    @classmethod
    def copy_email(cls,user_name):
        account_found = User.find_by_user_name(user_name)
        pyperclip.copy(account_found.email)             