from django.test import TestCase
from django.urls import reverse, resolve
from memo.views import formulario_memorandum, formulario_tipo_memo


class URLTests(TestCase):
    def test_formulario_memorandum_url(self):
        url = reverse("formulario_memorandum")
        self.assertEqual(resolve(url).func, formulario_memorandum)

    def test_formulario_tipo_memo_url(self):
        url = reverse("formulario_tipo_memo")
        self.assertEqual(resolve(url).func, formulario_tipo_memo)
