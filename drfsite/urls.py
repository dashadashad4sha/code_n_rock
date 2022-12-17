from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('admin/', admin.site.urls),
]
