from django.shortcuts import render
from .models import userinfo
from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        obj=userinfo.objects.all()
        userserial=userSerializer(obj,many=True)
        return Response(userserial.data,status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def getstid(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    userserail=userSerializer(stid)
    if request.method=='PUT':
        updatedt=userSerializer(stid,data=request.data)
        if updatedt.is_valid():
            updatedt.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(userserail.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteid(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    userinfo.delete(stid)
    
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def savestdata(request):
    if request.method=='POST':
        newuser=userSerializer(data=request.data)
        if newuser.is_valid():
            newuser.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatedata(request,id):
    try:
        stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        updatedt=userSerializer(stid,data=request.data)
        if updatedt.is_valid():
            updatedt.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    




