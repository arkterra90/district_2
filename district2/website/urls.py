from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path('api/contact-form/', views.handle_form_submission, name='handle_form_submission'),
    path('blog', views.blogHome, name='blogHome'),
    path('blogEntry/<int:postID>/', views.blogEntry, name='blogEntry')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)