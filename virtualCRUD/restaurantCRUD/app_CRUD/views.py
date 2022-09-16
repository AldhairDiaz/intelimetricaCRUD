import tablib

from django.http import HttpResponse
from import_export import resources
from .models import Restaurant

def import_data(request):
    with open('restaurantes.csv','r',encoding='utf8') as csv_file:
        
        restaurant_resource = resources.modelresource_factory(model=Restaurant)()
        dataset = tablib.Dataset(headers=[field.name for field in Restaurant._meta.fields]).load(csv_file)
        result = restaurant_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            
            restaurant_resource.import_data(dataset, dry_run=False)
        
        
    
    return HttpResponse(
        "Archivo CSV cargado con exito!!!"
    )
