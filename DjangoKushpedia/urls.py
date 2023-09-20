
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

    path('rest_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('rest_password_sent/', auth_views.PasswordChangeDoneView.as_view(), name="password_reset_done"),
    path('rest/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('rest_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
