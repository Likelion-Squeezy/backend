from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from tabs.models import Tab
from eezy.models import Eezy
from users.models import User

class EezyViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.tab = Tab.objects.create(user=self.user, title="UX란?", url="www.com")
        self.eezy = Eezy.objects.create(title="UX UI 기초", content="대충 페이지 요약한 내용.....", tab=self.tab)

    def test_get_eezy(self):
        url = reverse('eezy-detail', args=[self.eezy.id])
        response = self.client.get(url)

        expected_data = {
            "id": self.eezy.id,
            "title": self.eezy.title,
            "content": self.eezy.content,
            "tab": {
                "id": self.tab.id,
                "title": self.tab.title,
                "url": self.tab.url
            }
        }
        self.assertEqual(response.json(), expected_data)
