from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name="home"),
    path('contact/', views.contact, name="contact"),
    path('book_table/', views.book_table, name="book_table"),
]