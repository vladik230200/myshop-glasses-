from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.basket_detail, name='basket_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.basket_add, name='basket_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.basket_remove, name='basket_remove'),
    url('clear/', views.basket_clear, name='basket_clear'),
]