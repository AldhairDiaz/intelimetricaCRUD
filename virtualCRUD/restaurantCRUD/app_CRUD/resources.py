from pyexpat import model
from import_export import resources
from .models import Restaurant

class RestauranResource(resources.ModelResource):
    class Meta:
        model = Restaurant