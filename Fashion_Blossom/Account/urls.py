from django.urls import URLPattern,path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signin',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('forget_pass',views.forget_password,name='forget'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete",)
]