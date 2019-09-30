from django.http import Http404, HttpResponse
from django.template.loader import render_to_string


def index(request):
    context = {
        'projects': Project.objects.all().order_by('name'),
        'nochwas': None,
        'und noch': None,
        'bla': None,
    }

    # Das könnte man besser machen.

    rendered = render_to_string('index.html', context=context)
    return HttpResponse(rendered)



def bla(request):
    #das ist auch was neues

    return HttpResponse('oK')
