
from .models import *
def create_dynamic_model(model_name, data):

    json_field={}
    for key, val in data.items():
        if val == 'CharField':
            json_field[key]="str"
        elif val == 'IntegerField':
            json_field[key]="int"
        elif val == 'BooleanField':
            json_field[key]="bool"
        else:
            raise ValueError(f"Unsupported field type: {val} for field {key}")
    

    try:
        DynamicModelDetails.objects.create(model_name=model_name.capitalize(), fields=json_field)
    except:
        raise ValueError(f"modal name is already exists")
    

    return DynamicModelDetails


