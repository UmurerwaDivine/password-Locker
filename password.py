class Password:
    """
    Class that generates new instances of accounts.
    """

    password_list = [] # Empty contact list

    def __init__(self,username,email,password):

      # docstring removed for simplicity

        self.username = username
        self.email = email
        self.password = password