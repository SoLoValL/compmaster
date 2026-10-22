from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("calculator/", views.calculator, name="calculator"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("reviews/", views.reviews, name="reviews"),
    path("contacts/", views.contacts, name="contacts"),
    path("masters/", views.masters, name="masters"),
    path("faq/", views.faq, name="faq"),
    path("order/", views.order, name="order"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.user_profile, name="profile"),
]
