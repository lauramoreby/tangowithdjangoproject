from django.conf.urls import url #imports the relevant django machinery for URL mappings
from rango import views #imports the views module from rango
#(allows us to call the function url and point to the index view for the mapping in urlpatterns)

urlpatterns = [
    url(r'^$', views.index, name='index'), #handles the remaining URL string and map the empty string to the index view
    url(r'^about/',views.about,name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
]
