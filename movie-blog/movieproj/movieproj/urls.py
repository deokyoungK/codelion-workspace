from django.contrib import admin
from django.urls import path
from movieapp import views as m_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', m_views.index, name="index"),
    path('detail/<str:movie_id>', m_views.detail, name="detail"),
]
