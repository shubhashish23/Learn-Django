from django.urls import include, path
from app1.views import django_templating_lang

app_name ="app1"
urlpatterns = [
    path("", django_templating_lang , name='django_templating_lang'),
]
