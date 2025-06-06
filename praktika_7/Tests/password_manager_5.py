import unittest


class PasswordManager:
    def __init__(self):
        self._storage = {}

    def save_password(self, service, password):
        self._storage[service] = password

    def get_password(self, service):
        return self._storage.get(service)

    def delete_password(self, service):
        if service in self._storage:
            del self._storage[service]


class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.pm = PasswordManager()

    def test_get_password_returns_none_if_service_not_found(self):
        self.assertIsNone(self.pm.get_password("nonexistent_service"))

    def test_save_and_get_password(self):
        self.pm.save_password("gmail", "mypassword123")
        self.assertEqual(self.pm.get_password("gmail"), "mypassword123")

    def test_delete_password(self):
        self.pm.save_password("github", "ghpass")
        self.pm.delete_password("github")
        self.assertIsNone(self.pm.get_password("github"))

    def test_delete_nonexistent_service(self):
        self.pm.delete_password("unknown_service")
        self.assertIsNone(self.pm.get_password("unknown_service"))


if __name__ == "__main__":
    unittest.main()
