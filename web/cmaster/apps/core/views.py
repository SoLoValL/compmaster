from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings
import requests

from .forms import RequestForm
from .api_client import (
    get_services,
    get_device_types,
    get_portfolio,
    get_blog_posts,
    get_reviews,
    get_calculator_categories,
)


API_BASE_URL = "http://127.0.0.1:8000/api"


def home(request):
    """Главная страница"""
    context = {
        "services": get_services(),
        "device_types": get_device_types(),
        "portfolio": get_portfolio()[:6],
        "calculator_categories": get_calculator_categories(),
        "request_sent": False,
    }

    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            # Создаём запрос через API
            try:
                data = form.cleaned_data
                requests.post(f"{API_BASE_URL}/requests/", data=data)
                context["request_sent"] = True
                messages.success(request, "Заявка отправлена! Мы свяжемся с вами.")
            except requests.RequestException:
                messages.error(request, "Ошибка при отправке заявки. Попробуйте позже.")
    else:
        form = RequestForm()
        context["form"] = form

    return render(request, "core/home.html", context)


def blog_list(request):
    """Список постов блога"""
    posts = get_blog_posts()
    context = {"posts": posts}
    return render(request, "core/blog.html", context)


def blog_detail(request, pk):
    """Детальная страница поста"""
    try:
        response = requests.get(f"{API_BASE_URL}/blog/posts/{pk}/")
        response.raise_for_status()
        post = response.json()
    except requests.RequestException:
        post = None

    context = {"post": post}
    return render(request, "core/blog_detail.html", context)


def portfolio(request):
    """Портфолио работ"""
    works = get_portfolio()
    context = {"works": works}
    return render(request, "core/portfolio.html", context)


def reviews(request):
    """Отзывы"""
    reviews_list = get_reviews()
    context = {"reviews": reviews_list}
    return render(request, "core/reviews.html", context)


def calculator(request):
    """Калькулятор стоимости"""
    categories = get_calculator_categories()
    context = {"categories": categories}
    return render(request, "core/calculator.html", context)


def services(request):
    """Страница услуг"""
    services_list = get_services()
    device_types = get_device_types()
    context = {"services": services_list, "device_types": device_types}
    return render(request, "core/services.html", context)


def user_login(request):
    """Страница входа"""
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = AuthenticationForm()

    return render(request, "core/login.html", {"form": form})


def user_register(request):
    """Страница регистрации"""
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        try:
            response = requests.post(f"{API_BASE_URL}/users/users/register/", json={
                "username": request.POST.get("username"),
                "email": request.POST.get("email"),
                "password": request.POST.get("password"),
                "password_confirm": request.POST.get("password_confirm"),
            })
            
            if response.status_code == 201:
                messages.success(request, "Регистрация успешна! Теперь войдите.")
                return redirect("login")
            else:
                errors = response.json()
                for field, error_list in errors.items():
                    for error in error_list:
                        messages.error(request, f"{field}: {error}")
        except requests.RequestException:
            messages.error(request, "Ошибка при регистрации. Попробуйте позже.")
    else:
        form = {
            "username": "",
            "email": "",
        }

    return render(request, "core/register.html", {"form": form})


@login_required
def user_profile(request):
    """Профиль пользователя"""
    try:
        response = requests.get(f"{API_BASE_URL}/users/users/me/", 
                              headers={"Authorization": f"Bearer {request.session.get('access_token')}"})
        if response.status_code == 200:
            user_data = response.json()
        else:
            user_data = None
    except requests.RequestException:
        user_data = None

    context = {"user_data": user_data}
    return render(request, "core/profile.html", context)


@login_required
def user_logout(request):
    """Выход из системы"""
    logout(request)
    messages.success(request, "Вы вышли из системы.")
    return redirect("home")


def about(request):
    """Страница 'О нас'"""
    return render(request, "core/about.html")


def contacts(request):
    """Страница 'Контакты'"""
    return render(request, "core/contacts.html")


def masters(request):
    """Страница 'Мастера'"""
    return render(request, "core/masters.html")


def faq(request):
    """Страница 'Частые вопросы'"""
    return render(request, "core/faq.html")


def order(request):
    """Страница 'Заказать ремонт'"""
    context = {
        "request_sent": False,
    }

    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                requests.post(f"{API_BASE_URL}/requests/", data=data)
                context["request_sent"] = True
                messages.success(request, "Заявка отправлена! Мы свяжемся с вами.")
            except requests.RequestException:
                messages.error(request, "Ошибка при отправке заявки. Попробуйте позже.")
        else:
            context["form"] = form
            return render(request, "core/order.html", context)
    else:
        form = RequestForm()
        context["form"] = form

    return render(request, "core/order.html", context)
