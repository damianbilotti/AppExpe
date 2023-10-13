from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def primer_template (req):

    miHtml = open("E:\PROGRAMACION\expedicioncultural\expedicioncultural\templates")
    plantilla = Template(miHtml.read())
    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)
    return HttpResponse(documento)































