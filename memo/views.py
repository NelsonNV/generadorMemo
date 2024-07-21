from django.shortcuts import render, redirect
from .forms import MemorandumForm, TipoMemoForm
from django.contrib.auth.decorators import login_required


@login_required
def formulario_memorandum(request):
    if request.method == "POST":
        form = MemorandumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("formulario_memorandum")
    else:
        form = MemorandumForm()
    return render(request, "formulario.html", {"form": form})


@login_required
def formulario_tipo_memo(request):
    if request.method == "POST":
        form = TipoMemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("formulario_tipo_memo")
    else:
        form = TipoMemoForm()
    return render(request, "formulario.html", {"form": form})
