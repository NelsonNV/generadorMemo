from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MemorandumForm, TipoMemoForm
from django.contrib.auth.decorators import login_required


@login_required
def formulario_memorandum(request):
    if request.method == "POST":
        form = MemorandumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Memorandum guardado con éxito.")
            return redirect("formulario_memorandum")
        else:
            messages.error(
                request,
                "Hubo un error al guardar el memorandum. Por favor, corrige los errores e inténtalo de nuevo.",
            )
    else:
        usuario_actual = request.user if request.user.is_authenticated else None
        form = MemorandumForm(initial={"remitente": usuario_actual})
    return render(request, "formulario.html", {"form": form})


@login_required
def formulario_tipo_memo(request):
    if request.method == "POST":
        form = TipoMemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de memorandum guardado con éxito.")
            return redirect("formulario_tipo_memo")
        else:
            messages.error(
                request,
                "Hubo un error al guardar el tipo de memorandum. Por favor, corrige los errores e inténtalo de nuevo.",
            )
    else:
        form = TipoMemoForm()
    return render(request, "formulario.html", {"form": form})
