from django.shortcuts import render
from rest_framework import viewsets
from .models import CNAB, CNABData
from .serializers import CNABSerializer, CNABDataSerializer
from django.http import HttpResponse

def parse_file(cnab_file):
    cnab_data = cnab_file.readlines()
    for lines in cnab_data:
        type = lines[0:1].decode("utf-8")
        data = lines[1:9].decode("utf-8")
        value = lines[9:19].decode("utf-8")
        cpf = lines[19:30].decode("utf-8")
        card = lines[30:42].decode("utf-8")
        hour = lines[42:48].decode("utf-8")
        store_owner = lines[48:62].decode("utf-8")
        store_name = lines[62:81].decode("utf-8")
        cnab_data = {'type': type, 'data': data, 'value': value, 'cpf': cpf, 'card': card, 'hour': hour, 'store_owner': store_owner, 'store_name': store_name}
        CNABData.objects.create(**cnab_data)
    

class CNABViewSet(viewsets.ModelViewSet):
    queryset = CNAB.objects.all()
    serializer_class = CNABSerializer

    def perform_create(self, serializer):
        cnab_file = self.request.data.get('file')
        
        cnab_data = parse_file(cnab_file)
        cnab = serializer.save()
    
class CNABDataViewSet(viewsets.ModelViewSet):
    queryset = CNABData.objects.all()
    serializer_class = CNABDataSerializer

    def get_queryset(self):
        queryset = CNABData.objects.all()
        store_name = self.request.query_params.get('store_name', None)
        if store_name is not None:
            queryset = queryset.filter(store_name=store_name)
        return queryset

def search(request):
    return render(request, template_name='cnab/templates/list.html')