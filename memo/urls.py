# urls.py
from django.urls import path, include
from memo.views import formulario_memorandum, formulario_tipo_memo

urlpatterns = [
    path("formulario-memorandum/", formulario_memorandum, name="formulario_memorandum"),
    path("formulario-tipo-memo/", formulario_tipo_memo, name="formulario_tipo_memo"),
    path("accounts/", include("django.contrib.auth.urls")),
]
