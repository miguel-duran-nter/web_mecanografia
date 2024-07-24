from django.contrib import admin
from django.urls import path, include
from meca import views as meca_views
from api.views import user_update_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', meca_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', meca_views.login_view, name='login'),
    path('api/v1/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='docs'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='docs')),
    path('scoreboard/', include('scoreboard.urls')),
    path('register/', meca_views.register, name='register'),
    path('logout/', meca_views.logout, name='logout'),
    path('profile/<int:pk>/', user_update_view, name='user-update'),
]
