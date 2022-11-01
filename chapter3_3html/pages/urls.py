from django.urls import path
# from .views import homePageView
from .views import HomePageView, AboutPageView  # newww

# urlpatterns = [
#     path("", homePageView, name="home"),
# ]

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("", HomePageView.as_view(), name="home"),
]