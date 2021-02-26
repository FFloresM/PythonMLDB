from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('intra/', include('intra.urls')),
    path('admin/', admin.site.urls),
]
