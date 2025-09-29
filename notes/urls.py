from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/hello/', views.hello_world, name='hello'),
]