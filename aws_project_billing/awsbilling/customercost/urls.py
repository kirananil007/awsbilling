from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^customercost/$', views.login_view, name='login_view'),
)

