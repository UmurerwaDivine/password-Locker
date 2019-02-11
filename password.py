class User:
    """
    Class that generates new instances of accounts.
    """

    account_list = [] # Empty contact list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password

    def create_account(username,email,password):
    '''
    Function to create a new account
    '''
    new_account = User(username,email,password)
    return new_account