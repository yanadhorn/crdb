import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from crdb.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize
# Create your views here.
# def detail_view(request):
#     return render() # return JSON data XML - > JS Object Notion
#     return HttpResponse(get_template().render({}))

def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrive
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

class JsonCBV(View):
    def get(self,request,*args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self,request,*args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)

class SerializedDetailViewb(View):
    def get(self,request,*args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

class SerializedListViewb(View):
    def get(self,request,*args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')