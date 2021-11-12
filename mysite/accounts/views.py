from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import MyUserCreationForm
from .models import MyUser


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.method == "GET":
        form = MyUserCreationForm()
        return render(request, "accounts/signup.html", context={"form": form})

    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(True)
            return redirect(f"{reverse('accounts:welcome')}/?email={form.email}")
        else:
            return render(request, "accounts/signup.html", context={"form": form})


@require_http_methods(["GET"])
def welcome_view(request):
    email = request.GET.get("email", None)
    if email:
        try:
            user = MyUser.objects.get(email=email)
        except ObjectDoesNotExist:
            raise Http404("User not Exists")
        email = user.email
        return render(request, "accounts/welcome.html", context={"email": email})
    else:
        return HttpResponseBadRequest("No Email")
