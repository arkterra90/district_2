from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path('api/contact-form/', views.handle_form_submission, name='handle_form_submission'),


]