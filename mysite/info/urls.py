from django.urls import path

from .views import HomePageView

app_name = 'info'
urlpatterns = [
    path('', HomePageView.as_view(template_name="info/home.html")),
]
