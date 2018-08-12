from django.conf.urls import url

from carav import views

urlpatterns = [
    url('^create_water_fountain$', views.create_water_fountain, name='create_water_fountain'),
    url('^all_water_fountains$', views.all_water_fountains, name='all_water_fountains'),
    url('^delete_water_fountain$', views.delete_water_fountain, name='delete_water_fountain'),
    url('^update_water_fountain$', views.update_water_fountain, name='update_water_fountain'),
]
