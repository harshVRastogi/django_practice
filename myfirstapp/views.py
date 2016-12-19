from django.http import HttpResponse
from .models import Album
from django.template import loader


# Create your views here.

def index(request):
    album_all = Album.objects.all()
    template = loader.get_template('myfirstapp/index.html')
    context = {
        'album_all': album_all
    }
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    return HttpResponse("<h1>Details of the Album Id:" + str(album_id) + "</h1>")
