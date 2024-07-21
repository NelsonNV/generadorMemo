from django import forms
from memo.models import Memorandum, Tipo_memo, Documento, User


class BaseModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})


class MemorandumForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
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
        widgets = {
            "destinatario": forms.SelectMultiple(),
            "copia_destinatario": forms.SelectMultiple(),
            "fecha": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                    "class": "input",
                    "placeholder": "Selecciona una fecha",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        class_multi_select = "input SelectMultiple"
        super().__init__(*args, **kwargs)
        self.fields["copia_destinatario"].widget.attrs.update(
            {"class": class_multi_select}
        )
        self.fields["destinatario"].widget.attrs.update({"class": class_multi_select})
        self.fields["cuerpo"].widget.attrs.update({"class": "textarea", "rows": "10"})
        self.fields["cierre"].widget.attrs.update({"class": "textarea", "rows": "2"})
        self.fields["remitente"].widget.attrs.update(
            {"disabled": True, "class": "input"}
        )


class TipoMemoForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Tipo_memo
        fields = ["nombre", "formato"]


class DocumentoForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Documento
        fields = ["documento"]
