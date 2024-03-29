from django.urls import path,include
from . import views
# app_name='finaltaskapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('placeorder',views.placeorder, name='placeorder'),
    path('order', views.order, name='order'),
    path('confirm',views.confirm,name='confirm'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
]
