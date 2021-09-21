from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json

def variables_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            variable = vl.get_variable(id)
            variable_dto = serializers.serialize('json', variable)
            return HttpResponse(variable_dto, 'application/json')
        else:
            variables = vl.get_variables()
            variables_dto = serializers.serialize('json', variables)
            return HttpResponse(variables_dto, 'application/json')

    if request.method == 'POST':
        variable = vl.create_variable(request, json.loads(request.body))
        variable_dto = serializers.serialize('json', variable)
        return HttpResponse(variable_dto, 'application/json')


def variable_view(request, pk):
    if request.method == 'GET':
        variable = vl.get_variable(pk)
        variable_dto = serializers.serialize('json', variable)
        return HttpResponse(variable_dto, 'application/json')

    if request.method == 'PUT':
        variable = vl.update_variable(pk)
        variable_dto = serializers.serialize('json', variable)
        return HttpResponse(variable_dto, 'application/json')