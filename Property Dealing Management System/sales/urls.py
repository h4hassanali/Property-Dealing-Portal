from django.urls import path
from . import views

urlpatterns = [

    path('',views.login,name="login"),
    path('index',views.index,name="index"),
    path('add_prop',views.add_prop,name="add_prop"),
    path('home_search',views.home_search,name="home_search"),
    path('home_delete',views.home_delete,name="home_delete"),
    path('home_add',views.home_add,name="home_add"),
    path('add_new',views.add_new,name="add_new"),
    path('search_property',views.search_property_for_rent,name="search_property"),
    path('search_result',views.search_result,name="search_result"),
    path('del_rec',views.del_record,name="del_rec"),
    path('del_confirm',views.del_confirm,name="del_confirm"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('search_owner_prop',views.search_owner_prop,name="search_owner_prop"),
    path('owner_with_prop',views.search_owner_prop,name="owner_with_prop"),
]