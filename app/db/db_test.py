import unittest

from db import find_users


class TestDb(unittest.TestCase):
    """
    " "   this is a file containing a test - you can run it without running the whole web server
    """

    def test_find_users(self):
        users = find_users("%ant%")
        self.assertEqual(len(users), 1)  # check the length

        # get the zeroth element of the list has an attribute called id with value 1 - this is like
        # checking of a column called id in the zeroth row
        self.assertEqual(users[0]['id'], 1)

        self.assertEqual(users[0]['email'], 'ant@somerandomdomain.com') # check the email address

        # other examples:
        # assertTrue
        # assertFalse
        # with self.assertRaises(TypeError):
