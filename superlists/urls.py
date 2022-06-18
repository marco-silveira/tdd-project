from django.conf.urls import url
from lists import views as list_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/new$', list_views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', list_views.view_list, name='view_list'),

    url(r'^accounts/send_email$', accounts_views.send_login_email, name='send_login_email'),
    url(r'^accounts/login$', accounts_views.login, name='login'),
    url(r'^accounts/logout$', accounts_views.logout, name='logout'),
]