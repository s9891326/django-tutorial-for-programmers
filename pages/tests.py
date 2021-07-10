from django.test import TestCase

# Create your tests here.
class HomeViewTest(TestCase):
    def test_home_view(self):
        print("test home view")

        # client 是一個虛擬的瀏覽物件，可以用來測試 Django 有沒有正常運作
        # （但並沒有真的發 HTTP request，而是用 mocking 直接測試 URL routing 與 views）
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # 是 Django 特製的測試方法，用來測試某個 template 是否有真的被用到。
        self.assertTemplateUsed(response, "pages/home.html")
