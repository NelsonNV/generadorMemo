from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tipo_memo, Memorandum, Documento
from datetime import date


class ModelsTestCase(TestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.user3 = User.objects.create_user(username="user3", password="password")

        # Create Tipo_memo instance
        self.tipo_memo = Tipo_memo.objects.create(
            nombre="Tipo 1", formato="path/to/formato1.pdf"
        )

        # Create Memorandum instance
        self.memo = Memorandum.objects.create(
            destinatario=self.user1,
            remitente=self.user2,
            copia_destinatario=self.user3,
            asunto="Asunto 1",
            fecha=date.today(),
            cuerpo="Cuerpo del memorandum",
            cierre="Cierre del memorandum",
            tipo=self.tipo_memo,
        )

        # Create Documento instance
        self.documento = Documento.objects.create(documento="path/to/documento.pdf")

    def test_tipo_memo_creation(self):
        tipo_memo = Tipo_memo.objects.get(id=self.tipo_memo.id)
        self.assertEqual(tipo_memo.nombre, "Tipo 1")
        self.assertEqual(tipo_memo.formato, "path/to/formato1.pdf")

    def test_memorandum_creation(self):
        memo = Memorandum.objects.get(id=self.memo.id)
        self.assertEqual(memo.destinatario, self.user1)
        self.assertEqual(memo.remitente, self.user2)
        self.assertEqual(memo.copia_destinatario, self.user3)
        self.assertEqual(memo.asunto, "Asunto 1")
        self.assertEqual(memo.fecha, date.today())
        self.assertEqual(memo.cuerpo, "Cuerpo del memorandum")
        self.assertEqual(memo.cierre, "Cierre del memorandum")
        self.assertEqual(memo.tipo, self.tipo_memo)

    def test_documento_creation(self):
        documento = Documento.objects.get(id=self.documento.id)
        self.assertEqual(documento.documento, "path/to/documento.pdf")

    def test_memorandum_str(self):
        memo = Memorandum.objects.get(id=self.memo.id)
        self.assertEqual(str(memo), f"{self.memo.asunto} - {self.memo.fecha}")

    def test_tipo_memo_str(self):
        tipo_memo = Tipo_memo.objects.get(id=self.tipo_memo.id)
        self.assertEqual(str(tipo_memo), self.tipo_memo.nombre)
