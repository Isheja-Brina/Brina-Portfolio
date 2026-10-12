from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, "core/index.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(
                request,
                "Thank you! Your message has been received."
            )
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})