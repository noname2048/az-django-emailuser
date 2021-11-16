from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import MyUserCreationForm, MyUserLoginForm
from .models import MyUser


@require_http_methods(["GET", "POST"])
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

            LoginView
            user = authenticate(request, email=email)
            if user is not None:
                user_id = user.id
                # TODO: LOGIN
                return JsonResponse(data={"user_email": user.email})
            else:
                return JsonResponse(data={"message": "login fail"})
            return redirect(reverse("accounts:about_user", id=user_id))


@require_http_methods(["GET"])
def about_user_view(request, id):
    """유저 정보 확인 함수"""
    user = get_object_or_404(MyUser, pk=id)
    return render(request, "accounts/about_user.html", context={"user": user})
