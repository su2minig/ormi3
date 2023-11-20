from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # 추가
    path('api-auth/', include('rest_framework.urls')), # 웹 브라우저에서 로그인이 되게해줍니다(테스트)
]