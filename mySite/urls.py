from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SirGrossAlot.blog.urls')),  # Home page points to blog app
    path('reviews/', include('reviews.urls')),  # Properly namespaced reviews app
]
