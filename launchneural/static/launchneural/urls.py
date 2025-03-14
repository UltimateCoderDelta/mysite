from django.urls import path
from . import views

urlpatterns = [
    path("predictive_models/", views.predictive_models, name="predictive_models"),
    path("home/", views.home, name="home"),
    path("chatbot/", views.anxio, name="chatbot"),
    path("pneumonia_form/", views.pneumonia_form, name="pneumonia_form"),
    path("deepneural_blog/", views.deepneural_blog, name="deepneural_blog"),
    path("deepneural_intro/", views.deepneural_blog_one, name="deepneural_intro"),
]