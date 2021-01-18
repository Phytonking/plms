from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "web"
urlpatterns = [
    path("", views.index, name="index"),
    path("rules", views.rules, name="rules"),
    path("participant_register", views.p_reg, name="p_reg"),
    path("team_register", views.t_reg, name="t_reg"),
    path("contact", views.contact, name="contact"),
    path("thanks", views.thanks, name="thanks"),
    path("leaderboard", views.lad, name="leaderboard")
]