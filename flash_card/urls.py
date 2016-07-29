from django.conf.urls import url
from . import views

app_name = 'flash_card'

urlpatterns = [
    # /
    url(r'^flash_card/?$',                            views.index,    name='index'),
    # /flash_card/create
    url(r'^flash_card/create/?$',                     views.create_set, name='create'),
    # /flash_card/112
    url(r'^flash_card/(?P<set_id>[0-9]+)(:show)?/?$', views.show_set, name='show'),
    # /flash_card/112:edit
    url(r'^flash_card/(?P<set_id>[0-9]+)/edit/?$',    views.edit_set, name='edit'),
    # /flash_card/112:save
    url(r'^flash_card/(?P<set_id>[0-9]+)/save/create=(?P<create>[0-9]+)/?$',  views.save_set, name='save'),
    # /flash_card/112/learn
    url(r'^flash_card/(?P<set_id>[0-9]+)/learn/?$', views.learn, name='learn'),
    # /flash_card/112/flip
    url(r'^flash_card/(?P<set_id>[0-9]+)/flip/?$', views.flip, name='flip'),
]