from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('partners/', views.partners, name='partners'),
    path('platform/', views.platform, name='platform'),
    path('tools/', views.tools, name='tools'),
    path('trading/', views.trading, name='trading'),
    path('openaccount/', views.openaccount, name='openaccount'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]
