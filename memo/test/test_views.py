from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from memo.models import Tipo_memo
from memo.forms import MemorandumForm, TipoMemoForm


class ViewTests(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.tipo_memo = Tipo_memo.objects.create(
            nombre="Tipo 1", formato="path/to/formato1.pdf"
        )

    def test_formulario_memorandum_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("formulario_memorandum"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario.html")
        self.assertIsInstance(response.context["form"], MemorandumForm)
        self.assertContains(response, "Asunto")
        self.assertContains(response, "Fecha")

    def test_formulario_tipo_memo_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("formulario_tipo_memo"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formulario.html")
        self.assertIsInstance(response.context["form"], TipoMemoForm)
        self.assertContains(response, "Nombre")
        self.assertContains(response, "Formato")

    def test_formulario_memorandum_view_anonymous_user(self):
        response = self.client.get(reverse("formulario_memorandum"))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, "/accounts/login/?next=/formulario-memorandum/")

    def test_formulario_tipo_memo_view_anonymous_user(self):
        response = self.client.get(reverse("formulario_tipo_memo"))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, "/accounts/login/?next=/formulario-tipo-memo/")
