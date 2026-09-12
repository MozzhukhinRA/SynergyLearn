from django.test import TestCase
from django.urls import reverse
from .models import UserName


class GreetingViewTests(TestCase):
    def test_home_page_opens(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_name_is_saved(self):
        response = self.client.post(reverse("home"), {"name": "Роман"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserName.objects.filter(name="Роман").exists())
        self.assertContains(response, "Здравствуйте, Роман!")

    def test_empty_name_is_not_saved(self):
        response = self.client.post(reverse("home"), {"name": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserName.objects.count(), 0)

    def test_spaces_are_removed_from_name(self):
        self.client.post(reverse("home"), {"name": "  Роман  "})
        self.assertTrue(UserName.objects.filter(name="Роман").exists())

    def test_name_with_space_and_hyphen_is_saved(self):
        response = self.client.post(reverse("home"), {"name": "Анна-Мария Иванова"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserName.objects.filter(name="Анна-Мария Иванова").exists())

    def test_name_with_special_characters_is_not_saved(self):
        for name in ["Роман*", "Иван)", "Анна;", "Петр%", "№Роман"]:
            with self.subTest(name=name):
                UserName.objects.all().delete()
                response = self.client.post(reverse("home"), {"name": name})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(UserName.objects.count(), 0)
                self.assertContains(
                    response,
                    "Имя может содержать только буквы, пробелы и дефис.",
                )
