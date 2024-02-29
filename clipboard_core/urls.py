
from django.contrib import admin
from django.urls import path
from clipboard_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clipboard/', views.ClipboardListCreateAPIView.as_view(), name='clipboard-list-create'),
    path('clipboard/<int:pk>/', views.ClipboardRetrieveUpdateDestroyAPIView.as_view(), name='clipboard-retrieve-update-destroy'),
]
