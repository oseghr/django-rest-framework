from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Link
from .serializers import LinkSerializer

# Create your views here.


@api_view(["GET"])
def allLinks(request):
    ''' Gets all records '''
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def PostListApi(request):
    ''' Gets all records '''
    links = Link.objects.filter(active=True)
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def PostCreateApi(request):
    ''' Creates a new records '''
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(["GET"])
def PostDetailApi(request, id):
    ''' Gets a record with id '''
    try:
        link = Link.objects.get(id=id)
        if link:
            serializer = LinkSerializer(link, many=False)
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def PostDeleteApi(request, id):
    ''' Deletes a record with id '''
    try:
        link = Link.objects.get(id=id)
        if link:
            link.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
@api_view(["PUT"])
def PostUpdateApi(request, id):
    ''' Updates a record with id '''
    try:
        link = Link.objects.get(id=id)
        serializer = LinkSerializer(link, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)  
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)  
