from django.urls import path
from . import views

app_name = "photo"
urlpatterns = [
    path("", views.PhotoList.as_view(), name='index'),
    path("create/", views.PhotoCreate.as_view(), name='create'),
    path("detail/<int:pk>/", views.PhotoDetail.as_view(), name='detail'),
    path("update/<int:pk>/", views.PhotoUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", views.PhotoDelete.as_view(), name='delete'),
]