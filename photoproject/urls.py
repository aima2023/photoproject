from django.contrib import admin
from django.urls import path, include
#auth.viewsをインポートして、auth_viewsという名前を設定
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    path('', include('accounts.urls')),
    #パスワードリセットの依頼ページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name = 'password_reset.html'),
         name='password_reset'),
    #メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name = 'password_reset_sent.html'),
         name='password_reset_done'),
    #パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name = 'password_reset_form.html'),
         name='password_reset_confirm'),
    #パスワード再設定(リセット)完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name = 'password_reset_done.html'),
         name='password_reset_complete'),
    
]

urlpatterns+=static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)