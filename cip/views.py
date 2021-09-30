from django.shortcuts import render
from cip.models import bienAmbiente, bienImag, bienPersonal, bienpat,dependencia,ambiente,personal,certiDigital
from rest_framework import viewsets, permissions, filters
from cip.serializers import bienAmbienteSerializer, bienImagSerializer, bienPersonalSerializer, bienpatSerializer,dependenciaSerializer,ambienteSerializer,personalSerializer,certiDigitalSerializer

class bienpatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienpat.objects.all()
    serializer_class = bienpatSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['codEti']

class dependenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = dependencia.objects.all()
    serializer_class = dependenciaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['codDep']

class ambienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ambiente.objects.all()
    serializer_class = ambienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=dependencia__id']

class personalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = personal.objects.all()
    serializer_class = personalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=codPlaPer']

class bienImagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienImag.objects.all()
    serializer_class = bienImagSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class bienPersonalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienPersonal.objects.all()
    serializer_class = bienPersonalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class bienAmbienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienAmbiente.objects.all()
    serializer_class = bienAmbienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class certiDigitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = certiDigital.objects.all()
    serializer_class = certiDigitalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=personal__id']
