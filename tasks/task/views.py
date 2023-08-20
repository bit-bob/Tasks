from django.http import HttpResponse
from django.template import loader


def task(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
