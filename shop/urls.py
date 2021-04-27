from django.conf.urls import url, include
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    path('product_list', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

    path('contact', views.contact, name='contact'),

    path('home', views.home, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetConfirmView.as_view(), name="reset_password_complete"),



    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
    name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetConfirmView.as_view(), name="reset_password_complete"),

]