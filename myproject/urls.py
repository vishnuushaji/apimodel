
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import MyModelViewSet

router = routers.DefaultRouter()
router.register(r'mymodels', MyModelViewSet)
                
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
