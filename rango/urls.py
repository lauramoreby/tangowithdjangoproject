from django.conf.urls import url #imports the relevant django machinery for URL mappings
from rango import views #imports the views module from rango
#(allows us to call the function url and point to the index view for the mapping in urlpatterns)

urlpatterns = [
    url(r'^$', views.index, name='index'), #handles the remaining URL string and map the empty string to the index view
]