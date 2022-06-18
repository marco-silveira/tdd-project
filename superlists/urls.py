from django.conf.urls import url
from lists import views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    url(r'^accounts/send_login_email$', accounts_views.send_login_email, name='send_login_email'),
]
