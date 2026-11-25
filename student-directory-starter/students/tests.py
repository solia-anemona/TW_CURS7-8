from django.test import TestCase


class StudentsApiTests(TestCase):
    def test_list_returns_json(self):
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", response.json())

    def test_health_returns_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
