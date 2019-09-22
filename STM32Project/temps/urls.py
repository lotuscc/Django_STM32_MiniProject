
from django.urls import path, include

import temps.views

urlpatterns = [

    path('index', temps.views.index),
]