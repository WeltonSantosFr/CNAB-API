from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import CNAB, CNABData
from .serializers import CNABSerializer, CNABDataSerializer, Store

def parse_file(cnab_file):
    cnab_data = cnab_file.readlines()
    for lines in cnab_data:
        type = lines[0:1].decode("utf-8")
        data = lines[1:9].decode("utf-8")
        value = lines[9:19].decode("utf-8")
        cpf = lines[19:30].decode("utf-8")
        card = lines[30:42].decode("utf-8")
        hour = lines[42:48].decode("utf-8")
        store_owner = lines[48:62].strip().decode("utf-8")
        store_name = lines[62:81].strip().decode("utf-8")
        cnab_data = {'type': type, 'data': data, 'value': value, 'cpf': cpf, 'card': card, 'hour': hour, 'store_owner': store_owner, 'store_name': store_name}
        CNABData.objects.create(**cnab_data)
    
def parse_queryset(queryset):
    total_value = 0
    for data in queryset:
        
        object = CNABData.objects.get(pk=data.pk)
        
        total_value += object.value
        print(total_value)
        return_object = {type: object.type, total_value: total_value}
    
    return return_object
        
        

class CNABViewSet(viewsets.ModelViewSet):
    queryset = CNAB.objects.all()
    serializer_class = CNABSerializer

    def perform_create(self, serializer):
        cnab_file = self.request.data.get('file')
        
        cnab_data = parse_file(cnab_file)
        cnab = serializer.save()
    
def store_data_view(request):
    store_name = request.GET.get('store_balance')
    stores = CNABData.objects.get(store_name=store_name)
    print(stores)
    return render(request, 'store_data.html', {'stores': stores})

def store_form_view(request):
    stores = CNABData.objects.all()
    
    store_balance = {}
    for store in stores:
        store_name = store.store_name
        value = store.value
        type = store.type

        if store_name not in store_balance:
            store_balance[store_name] = 0
        
        if type == 1 or 4 or 5 or 6 or 7 or 8:
            store_balance[store_name] += value
        
        else:
            store_balance[store_name] -= value
    # for store_name, value in store_balance.items():
    #     print(f"{store_name}: {value}")
    print(store_balance)

    return render(request, 'store_form.html', {'store_balance': store_balance})