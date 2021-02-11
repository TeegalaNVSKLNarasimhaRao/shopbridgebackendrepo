from django.conf.urls import url 
from Inventory import views 
 
urlpatterns = [ 
    url(r'^api/inventorys$', views.inventory_list, name="inventorys"),
    url(r'^api/inventorys/(?P<pk>[0-9]+)$', views.inventory_detail, name="inventory_detail")
]