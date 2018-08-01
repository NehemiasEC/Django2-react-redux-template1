from django.shortcuts import render
from rest_framework import generics
# Create your views here.


from . import models


from . import serializers

class NoteList(generics.ListAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer



class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
