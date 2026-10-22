import requests
from django.conf import settings


API_BASE_URL = "http://127.0.0.1:8000/api"


def get_services():
    """Получить список услуг из API"""
    try:
        response = requests.get(f"{API_BASE_URL}/services/services/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []


def get_device_types():
    """Получить список типов устройств"""
    try:
        response = requests.get(f"{API_BASE_URL}/services/device-types/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []


def get_portfolio():
    """Получить портфолио из API"""
    try:
        response = requests.get(f"{API_BASE_URL}/portfolio/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []


def get_blog_posts():
    """Получить посты из блога"""
    try:
        response = requests.get(f"{API_BASE_URL}/blog/posts/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []


def get_reviews():
    """Получить отзывы"""
    try:
        response = requests.get(f"{API_BASE_URL}/reviews/reviews/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []


def get_calculator_categories():
    """Получить категории калькулятора"""
    try:
        response = requests.get(f"{API_BASE_URL}/calculator/categories/")
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []
