from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('notice/', include('notice.urls')),
    path('accounts/', include('accounts.urls')),
]