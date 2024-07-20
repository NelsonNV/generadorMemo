# tests/test_forms.py
from django.test import TestCase
from django.contrib.auth.models import User
from memo.models import Tipo_memo, Memorandum
from memo.forms import MemorandumForm
from datetime import date


class MemorandumFormTestCase(TestCase):
    def setUp(self):
        # Crear usuarios
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.user3 = User.objects.create_user(username="user3", password="password")
        self.user4 = User.objects.create_user(username="user4", password="password")

        # Crear instancia de Tipo_memo
        self.tipo_memo = Tipo_memo.objects.create(
            nombre="Tipo 1", formato="path/to/formato1.pdf"
        )

    def test_memorandum_form_valid(self):
        form_data = {
            "destinatario": self.user1.id,
            "remitente": self.user2.id,
            "copia_destinatario": [self.user3.id, self.user4.id],
            "asunto": "Asunto de prueba",
            "fecha": date.today(),
            "cuerpo": "Cuerpo del memorandum de prueba",
            "cierre": "Cierre del memorandum de prueba",
            "tipo": self.tipo_memo.id,
        }
        form = MemorandumForm(data=form_data)
        self.assertTrue(form.is_valid())
        memorandum = form.save()
        self.assertEqual(memorandum.destinatario, self.user1)
        self.assertEqual(memorandum.remitente, self.user2)
        self.assertEqual(
            list(memorandum.copia_destinatario.all()), [self.user3, self.user4]
        )
        self.assertEqual(memorandum.asunto, "Asunto de prueba")

    def test_memorandum_form_invalid(self):
        form_data = {
            "destinatario": "",  # Campo obligatorio vacío
            "remitente": self.user2.id,
            "copia_destinatario": [self.user3.id, self.user4.id],
            "asunto": "Asunto de prueba",
            "fecha": date.today(),
            "cuerpo": "Cuerpo del memorandum de prueba",
            "cierre": "Cierre del memorandum de prueba",
            "tipo": self.tipo_memo.id,
        }
        form = MemorandumForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("destinatario", form.errors)

    def test_memorandum_form_valid_with_empty_copia_destinatario(self):
        form_data = {
            "destinatario": self.user1.id,
            "remitente": self.user2.id,
            "copia_destinatario": [],  # Lista vacía para 'copia_destinatario'
            "asunto": "Asunto de prueba",
            "fecha": date.today(),
            "cuerpo": "Cuerpo del memorandum de prueba",
            "cierre": "Cierre del memorandum de prueba",
            "tipo": self.tipo_memo.id,
        }
        form = MemorandumForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertNotIn("copia_destinatario", form.errors)

    def test_memorandum_form_empty_data(self):
        form = MemorandumForm(data={})
        self.assertFalse(form.is_valid())

        # Verifica que hay errores en el formulario
        self.assertGreater(len(form.errors), 0)

        # Verifica que los campos obligatorios están en los errores
        self.assertIn("destinatario", form.errors)
        self.assertIn("remitente", form.errors)
        self.assertIn("asunto", form.errors)
        self.assertIn("fecha", form.errors)
        self.assertIn("cuerpo", form.errors)
        self.assertIn("cierre", form.errors)
        self.assertIn("tipo", form.errors)
