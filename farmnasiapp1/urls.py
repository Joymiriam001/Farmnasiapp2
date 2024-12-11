from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import submit_county

urlpatterns = [
    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),

    # Home and other pages
    path('home/', views.home, name='my_home'),
    path('seasons/', views.seasons, name='seasons'),
    path('product/', views.product, name='product'),
    path('cereals/', views.cereals, name='cereals'),
    path('beverage/', views.beverage, name='beverage'),
    path('fruits/', views.fruits, name='fruits'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('legumes/', views.legumes, name='legumes'),
    path('contact/', views.contact, name='contact'),

    path('submit_county',views.submit_county,name='submit_county'),


    # Optional: Redirect root path to login
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='root_login'),
]
