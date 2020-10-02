from django.conf.urls import url
from .views import *

urlpatterns = [url("quiz", Quiz.as_view(), name="quiz")]
