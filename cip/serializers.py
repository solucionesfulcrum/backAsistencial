from cip.models import bienAmbiente, bienPersonal, bienpat,dependencia,ambiente,personal, bienImag, certiDigital
from rest_framework import serializers

class bienpatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienpat
        fields = '__all__'

class bienImagSerializer(serializers.HyperlinkedModelSerializer):
    datos_bienpat = bienpatSerializer(source = "bienpat", read_only=True)
    class Meta:
        model = bienImag
        fields = '__all__'

class dependenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dependencia
        fields = '__all__'

class ambienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ambiente
        fields = '__all__'  

class personalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = personal
        fields = '__all__'     

class bienPersonalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienPersonal
        fields = '__all__'    

class bienAmbienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienAmbiente
        fields = '__all__'         

class certiDigitalSerializer(serializers.HyperlinkedModelSerializer):
    datosPersonal = personalSerializer(source="personal", read_only=True)  
    class Meta:
        model = certiDigital
        fields = '__all__'       