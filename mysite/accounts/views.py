from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods

# forms
from rest_framework.decorators import api_view

from .forms import MyUserCreationForm, MyUserLoginForm
from django.contrib.auth.forms import PasswordChangeForm

# models
from .models import MyUser


@require_http_methods(["GET", "POST"])
@api_view(["GET", "POST"])
def signup_view(request):
    """회원가입을 도와주는 함수
    GET: form 양식 리턴
    POST:   (1) 성공시 -> welcom으로 리다이렉트
            (2) 실패시 -> form을 다시 반환
    """
    if request.method == "GET":
        form = MyUserCreationForm()
        return render(request, "accounts/signup.html", context={"form": form})

    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(True)
            user_email = form.cleaned_data.get("email")
            return redirect(f"{reverse('accounts:welcome')}/?email={user_email}")
        else:
            return render(request, "accounts/signup.html", context={"form": form})


@require_http_methods(["GET"])
def welcome_view(request):
    """회원가입을 환영하는 함수 (GET)
    (1) query string 이 없으면 400
    (2) user 가 없으면 404
    (3) 정상일 경우 welcome 출력
    """
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


@require_http_methods(["GET", "POST"])
def login_view(request):
    """로그인 진행 함수"""
    if request.method == "GET":
        form = MyUserLoginForm
        return render(request, "accounts/login.html", context={"form": form})

    else:
        form = MyUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse(data={"user_email": user.email})
            else:
                return JsonResponse(data={"message": "login fail"})
        else:
            return render(request, "accounts/login.html", context={"form": form})


@require_http_methods(["GET"])
def about_user_view(request, id):
    """유저 정보 확인 함수"""
    user = get_object_or_404(MyUser, pk=id)
    return render(request, "accounts/about_user.html", context={"user": user})


@require_http_methods(["GET", "POST"])
def change_password(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login"))

    if request.method == "GET":
        form = PasswordChangeForm(MyUser)
        return render(request, "accounts/change_password.html", context={"form": form})

    else:
        user = request.user
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "accounts/change_password_complete.html", context={})
        else:
            return render(
                request,
                "accounts/change_password.html",
                context={"form": form},
            )


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse("accounts:login"))
