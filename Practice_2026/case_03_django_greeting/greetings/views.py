from django.shortcuts import render
from .forms import UserNameForm


def home(request):
    greeting_name = None

    if request.method == "POST":
        form = UserNameForm(request.POST)

        if form.is_valid():
            user_name = form.save()
            greeting_name = user_name.name
            form = UserNameForm()
    else:
        form = UserNameForm()

    return render(
        request,
        "greetings/home.html",
        {"form": form, "greeting_name": greeting_name},
    )
