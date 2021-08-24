from django.urls import path
from django.urls import path

# from counter_details_api_app import views
from .views import CounterDetailsApi
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("fetch/", CounterDetailsApi.as_view()),
    path("fetch/<str:pk>/", CounterDetailsApi.as_view()),
]
# urlpatterns = [
#     path(r"fetch/", views.counter_details_api),
#     path(r"fetch/<str:pk>", views.counter_details_api),  # for update and delete
# ]
