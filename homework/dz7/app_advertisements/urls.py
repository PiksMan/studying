from django.urls import path
from .views import index, top_sellers, post_adv, register, login, profile

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('post-adv/', post_adv, name='post-adv'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
]
