class User:
    """
    Class that generates new instances of contacts
    """
    account_list = []

    def __init__(self,user_name,email,password):

        # docstring removed for simplicity

        self.user_name = user_name
        self.email = email
        self.password = password