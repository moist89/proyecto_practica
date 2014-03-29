from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import producto
def add_product_view(request):

	if request.method=="POST":
	   form=addProductForm(request.POST)
	   info="inicializando"
	   if form.is_valid():
	   	  print "no entro"
		  nombre=form.cleaned_data['nombre']
		  descripcion=form.cleaned_data['descripcion']
		  p=producto()
		  p.nombre=nombre
		  p.descripcion=descripcion
		  p.estatus=True
		  p.save()
		  print "no entrodd"
		  info="Se guardo Satisfactoriamente"
	   else:	
			info="informacion con datos incorrectos"
			form=addProductForm()
	   ctx={'form':form, 'info':info}	
	   return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		 form=addProductForm()
		 ctx={'form':form}
		 return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
