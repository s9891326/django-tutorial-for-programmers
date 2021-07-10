from django.test import TestCase
from .models import Store, MenuItem

# Create your tests here.

class StoreViewTest(TestCase):
    def setUp(self) -> None:
        self.notes = "咖拉讚"
        Store.objects.create(name="麥當勞", notes=self.notes)
        mcdonalds = Store.objects.create(name='McDonalds')
        MenuItem.objects.create(store=mcdonalds, name='大麥克餐', price=99)

    def tearDown(self) -> None:
        Store.objects.all().delete()

    def test_list_view(self):
        r = self.client.get("/store/")
        self.assertEqual(r.status_code, 200)
        self.assertContains(
            r, '<a class="navbar-brand" href="/">午餐系統</a>',
            html=True
        )
        self.assertContains(r, '<a href="/store/1">麥當勞</a>', html=True)
        self.assertContains(r, self.notes)

    def test_detail_view(self):
        r = self.client.get("/store/2")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, '<tr><td>大麥克餐</td><td>99</td></tr>', html=True)
