from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MemorandumForm, TipoMemoForm  # Importa los formularios necesarios
from django.contrib.auth.decorators import login_required


@login_required
def formulario_memorandum(request):
    if request.method == "POST":
        form = MemorandumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "success"
            )  # Redirige a una página de éxito o a donde quieras
    else:
        form = MemorandumForm()
    return render(request, "formulario.html", {"form": form})


@login_required
def formulario_tipo_memo(request):
    if request.method == "POST":
        form = TipoMemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "success"
            )  # Redirige a una página de éxito o a donde quieras
    else:
        form = TipoMemoForm()
    return render(request, "formulario.html", {"form": form})
