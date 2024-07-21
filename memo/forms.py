from django import forms
from memo.models import Memorandum, Tipo_memo, Documento, User


class BaseModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


class MemorandumForm(forms.ModelForm):
    copia_destinatario = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,  # Permite que este campo esté vacío
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Memorandum
        fields = [
            "destinatario",
            "remitente",
            "copia_destinatario",
            "asunto",
            "fecha",
            "cuerpo",
            "cierre",
            "tipo",
        ]


class TipoMemoForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Tipo_memo
        fields = ["nombre", "formato"]


class DocumentoForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Documento
        fields = ["documento"]
