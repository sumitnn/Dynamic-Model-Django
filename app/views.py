import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import create_dynamic_model
from .models import DynamicModelDetails



def create_view(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name', '')
        field_names = request.POST.getlist('field_name')
        field_types = request.POST.getlist('field_type')
        fields = dict(zip(field_names, field_types))

        if DynamicModelDetails.objects.filter(model_name=model_name.capitalize()).exists():
            messages.warning(request, "Modal Name is Already Exists") 
            return render(request, 'index.html')
       
        DynamicModel = create_dynamic_model(model_name, fields)
        messages.success(request, "Create Table Successfully")
        return render(request, 'index.html')

    
    return render(request, 'index.html')

def add_data(request, model_name):
    temp_dict={}

    queryset = DynamicModelDetails.objects.get(model_name=model_name)
    temp_dict["data"]=queryset
    temp_dict["modal_name"]=model_name
    if request.method =="GET":
        return render(request, 'add-data.html',temp_dict)
  
    post_data = {}
    prv_data = json.loads(queryset.value) if queryset.value else []

    for key, val in queryset.fields.items():
        post_data[key] = request.POST.get(key)

    if isinstance(prv_data, list):
        prv_data.append(post_data)
    else:
        prv_data = [prv_data, post_data]


    queryset.value = json.dumps(prv_data)
    queryset.save()

    messages.success(request, "add Data in Table Successfully")  
    return render(request, 'add-data.html',temp_dict)
    


def add_data_page(request):
    temp_dict={}
    queryset = DynamicModelDetails.objects.all()
    temp_dict["modal_names"]= queryset 
    return render(request, 'add-data-page.html',temp_dict)

def show_data(request,model_name):
    temp_dict={}
    queryset = DynamicModelDetails.objects.get(model_name=model_name.capitalize())
    temp_dict["data"]=json.loads(queryset.value) if queryset.value else None
    temp_dict["table_head"]=queryset.fields
    temp_dict["model_name"]=queryset.model_name
    return render(request, 'show-data.html',temp_dict)