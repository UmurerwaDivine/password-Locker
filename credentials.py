class Credentials:


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

        Credentials.account_list.append(self)
        
        
    def delete_account(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credentials.account_list.remove(self)