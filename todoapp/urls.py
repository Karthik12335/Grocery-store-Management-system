from django.urls import path
from todoapp import views
urlpatterns = [
    path('',views.dash_product),
    path('home',views.index),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('index',views.home),
    path('contact',views.contact),
    path('product',views.product),
    path('username/<username>',views.username),
    path('pdashboard',views.dash_product),
    #path('elec',views.filter_electronic),
    #path('groc',views.filter_grocery),
    #path('cloth',views.filter_cloths)
    path('filter/<vcat>',views.filter),
    path('pfilter/<p>',views.pfilter),
    path('sort/<sv>',views.sort),
    path('prange',views.prange),
    path('formapi',views.formapi),
    path('modelform',views.modelform),
    path('register',views.register),
    path('login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    path('logout',views.user_logout),

    
]

