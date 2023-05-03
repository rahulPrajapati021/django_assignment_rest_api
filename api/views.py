from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Work, Client
from .serializers import WorkSerializer, ClientSerializer
# Create your views here.

@api_view(['GET'])
def works(request):
    artist = request.query_params.get('artist')
    work_type = request.query_params.get('work_type')
    if artist is not None:
        works = Work.objects.filter(artist_name=artist)
    elif work_type is not None:
        works = Work.objects.filter(work_type=work_type)
    else:
        works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def register(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def creatework(request):
    serializer = WorkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(request.data)

def page_not_found_view(request, exception):
    msg = {"msg": "page not found"}
    return Response(msg)