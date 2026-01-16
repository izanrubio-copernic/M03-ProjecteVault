import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):

    def test_password_length(self):
        self.assertFalse(check_password("Abc1"))

    def test_has_number(self):
        self.assertFalse(check_password("Abcdefgh")) # No num

    def test_has_upper(self):
        self.assertFalse(check_password("abcdefg1")) # No mayus

    def test_no_admin(self):
        self.assertFalse(check_password("admin1234")) # Contiene admin

    def test_valid_password(self):
        self.assertTrue(check_password("SuperSecret1"))

if __name__ == '__main__':
    unittest.main()
