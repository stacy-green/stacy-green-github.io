from django.urls import path
from . import views

app_name = "earlshorten"

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('yeet/<str:url_code>', views.yeet, name='yeet')
]
