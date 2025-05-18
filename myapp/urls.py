from django.urls import path
from .views import BookViewSet

# Define the app's URL patterns manually
urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book-detail'),
]