from django.urls import path
from . import views

urlpatterns = [
    path('<username>', views.dashboard),
    path('settings/', views.settings),
    path('top/', views.leaderboard)
]