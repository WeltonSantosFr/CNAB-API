from django.shortcuts import render
from django.http import HttpResponse

def upload(request):
    return render(request, "upload.html")

def process_cnab(request):
    cnab = request.POST.get("cnab")
    formulario = open(cnab)
    formulario = formulario.readlines()
    print(formulario)

    dataform = []
    for linhas in formulario:
        tipo = linhas[0:1]
        data = linhas[1:9]
        valor = linhas[10:19]
        cpf = linhas[20:30]
        cartao = linhas[31:42]
        hora = linhas[43:48]
        dono_da_loja = linhas[49:62]
        nome_da_loja = linhas[63:81]
        dataform.append({"tipo": tipo, "data": data, "valor": valor, "cpf": cpf, "cartao": cartao, "hora": hora, "dono_da_loja": dono_da_loja.strip("ƒ"), "nome_da_loja": nome_da_loja})
        print(dataform)
        
        

    return HttpResponse(dataform)
    
        

