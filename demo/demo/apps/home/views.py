from django.shortcuts        import render
from django.shortcuts        import render_to_response
from django.template         import RequestContext
from demo.apps.ventas.models import producto
from demo.apps.home.forms    import ContactForm
from django.core.mail        import EmailMultiAlternatives

def index_view(request):
    return render_to_response('home/index.html',
        context_instance=RequestContext(request))

def about_view(request):
    mensaje="esto es un mensaje"
    ctx={'msg':mensaje}
    return render_to_response('home/about.html',
       ctx,context_instance=RequestContext(request))
def productos_view(request):
    prod=producto.objects.filter(estatus=True)
    ctx={'productos':prod}
    return render_to_response('home\productos.html',
        ctx,context_instance=RequestContext(request))

def contacto_view(request):
    
    info_enviado=False #definir si se envio la info\
    email= ""
    titulo=""
    texto=""
    if request.method=="POST":
        formulario=ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado=True
            email=formulario.cleaned_data['Email']
            titulo=formulario.cleaned_data['Titulo']
            texto=formulario.cleaned_data['Texto']
            to_admin='moist.medina@gmail.com'
            html_content="informacion recibida <br><br><br>Mensaje<br><br><br>%s"%(texto)
            msg=EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()
    else:
           formulario=ContactForm()    


    ctx={'form':formulario,'email':email,'titulo':titulo
    ,'texto':texto,'info_enviado':info_enviado}
    return render_to_response('home/contacto.html',ctx,
        context_instance=RequestContext(request))