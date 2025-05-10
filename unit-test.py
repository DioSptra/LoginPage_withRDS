import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    # Setup test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test rute login
    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login to NeoVault', response.data)

    # Test rute register
    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create an Account', response.data)

    # Test rute dashboard (harus login dulu)
    def test_dashboard_page(self):
        # Simulasi login
        self.app.post('/login', data=dict(username='admin', password='admin123'))
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, admin 🚀', response.data)

if __name__ == '__main__':
    unittest.main()
