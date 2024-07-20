from django.db import models
from django.contrib.auth.models import User


class Tipo_memo(models.Model):
    nombre = models.CharField(max_length=40)
    formato = models.FileField()

    def __str__(self):
        return f"{self.nombre}"


class Memorandum(models.Model):
    destinatario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="memorado_para"
    )
    remitente = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="memorado_por"
    )
    copia_destinatario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="memorado_como_copia",
    )
    asunto = models.CharField(max_length=90)
    fecha = models.DateField()
    cuerpo = models.TextField()
    cierre = models.TextField()
    tipo = models.OneToOneField(Tipo_memo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.asunto} - {self.fecha}"


class Documento(models.Model):
    documento = models.FileField()
