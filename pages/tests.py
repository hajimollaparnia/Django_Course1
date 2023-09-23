from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class AboutUsPageTests(TestCase):
    def test_aboutus_page_url_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'About Us')

    def test_aboutus_page_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'aboutus.html')
