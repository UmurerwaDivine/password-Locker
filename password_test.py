
import unittest # Importing the unittest module
from password import User # Importing the account class
import pyperclip
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = User("din","din@gmail.com","on1") # create new account

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.user_name,"din")
        self.assertEqual(self.new_account.email,"din@gmail.com")
        self.assertEqual(self.new_account.password,"on1")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(User.account_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.account_list = []

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = User("Test","di@gmail.com","user") # new account
            test_account.save_account()
            self.assertEqual(len(User.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account =User("Test","user","din@gmail.com") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(User.account_list),1)

    def test_find_account_by_user_name(self):
        '''
        test to check if we can find a account by phone number and display information
        '''

        self.new_account.save_account()
        test_account = User("Test","user","di@gmail.com") # new account
        test_account.save_account()

        found_account = User.find_by_user_name("Test")

        self.assertEqual(found_account.email,test_account.email)
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = User("Test","user","test@user.com") # new account
        test_account.save_account()

        account_exists = User.account_exist("Test")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):  
        '''
        method that returns a list of all account saved
        '''  
 
        self.assertEqual(User.display_accounts(),User.account_list)
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found account
        '''

        self.new_account.save_account()
        User.copy_email("din")

        self.assertEqual(self.new_account.email,pyperclip.paste())   
if __name__ == '__main__':
    unittest.main()