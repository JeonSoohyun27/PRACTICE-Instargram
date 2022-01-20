from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate

app_name = "photo"
urlpatterns = [
    path("create/",PhotoCreate.as_view(), name = 'create'),
    path("detail/<int:pk>/",PhotoDetail.as_view(), name = 'detail'),
    path("delete/<int:pk>/",PhotoDelete.as_view(), name = 'delete'),
    path("update/<int:pk>/",PhotoUpdate.as_view(), name = 'update'),
    path('', PhotoList.as_view(),name = 'index'),
]
