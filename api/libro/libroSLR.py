from api.models import Libro
from rest_framework import  serializers

class LibroSerializado(serializers.ModelSerializer):
    id =  serializers.IntegerField(required = False)
    nombre = serializers.CharField(required = False)
    autor = serializers.CharField(required = False)
    sinopsis = serializers.CharField()
    precio = serializers.IntegerField(required = False)
    stock = serializers.IntegerField(required = False)
    publicacion = serializers.DateField()

    class Meta:
        model = Libro
        fields = '__all__'
