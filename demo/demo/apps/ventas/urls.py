from django.conf.urls import patterns,include,url
urlpatterns=patterns('demo.apps.ventas.views',
	url(r'^add/producto/$','add_product_view',name='vista_addProducto'),
	)