from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('books/<int:id1>',views.display), 
    path('books/<int:id1>',views.add)
]
