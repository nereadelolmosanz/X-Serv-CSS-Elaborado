from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def main_page(request):
    response = '<h1>Ejercicio 15.6: Django-CMS_PUT</h1>'
    response += '<h3>(Use GET or PUT to add new pages).</h3>'
    pages_list = Pages.objects.all()
    if len(pages_list) != 0:
        response += '<p>Saved pages:</p>'
        response += '<ul>'
        for page in pages_list:
            response += '<p>' + str(page) + '</p>'
        response += '</ul>'
    return HttpResponse(response)


@csrf_exempt
def page_searching(request, resource):
    cont_type = "text/html"

    if request.method == 'GET':
        try:
			#Para asegurar que el navegador aplica la hoja de estilos
            if resource == 'css/main.css':
                cont_type = "text/css"

            pageSearched = Pages.objects.get(name=resource)
            response = pageSearched.page
            return HttpResponse(response,content_type=cont_type)

        except Pages.DoesNotExist:
            return HttpResponseNotFound('<h1>' + resource + ' not found.</h1>')

    elif request.method == 'POST':
        newPage = Pages(name=resource, page=request.body)
        newPage.save()
        return HttpResponse('<h1>Page added successfully.</h1>')

    else:
        return HttpResponse('<h1>Invalid method.</h1>')
