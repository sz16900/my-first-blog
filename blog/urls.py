from django.conf.urls import url
# Import all of our views
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
