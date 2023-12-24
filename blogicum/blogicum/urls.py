from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='homepage')),
    path('pages/', include('pages.urls', namespace='pages')),
]
