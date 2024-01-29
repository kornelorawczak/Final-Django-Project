from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email' : 'testmail@gmail.com',
            'password': 'testpassword',
            # Dodaj inne pola użytkownika, jeśli są wymagane
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.login_url = reverse('login')

    def test_login_view_authenticated_user(self):
         # Sprawdź, czy niezalogowany użytkownik może zobaczyć stronę logowania
        self.client.logout()
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')  # Oczekiwany szablon dla strony logowania

    def test_login_view_unauthenticated_user(self):
        # Sprawdź, czy niezalogowany użytkownik może zobaczyć stronę logowania
        self.client.logout()
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')  # Oczekiwany szablon dla strony logowania

    def test_login_view_successful_login(self):
        # Sprawdź, czy użytkownik może zalogować się poprawnymi danymi
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login_success.html')  # Oczekiwane przekierowanie po udanym logowaniu
        # Możesz dodać więcej asercji, aby sprawdzić, czy użytkownik jest teraz zalogowany, itp.