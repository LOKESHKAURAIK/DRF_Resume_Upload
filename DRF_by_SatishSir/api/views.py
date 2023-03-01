from django.shortcuts import render
from rest_framework.response import Response
from . models import Profile
from .serializer import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            serializer = ProfileSerializer(candidates)
            return Response(serializer.data, status=status.HTTP_200_OK)
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            serializer = ProfileSerializer(candidates, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data Updated'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        
    def patch(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            serializer = ProfileSerializer(candidates, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data Partialy Updated'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        
    
    def delete(self, request, pk=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            candidates.delete()
            return Response({'msg':'data deleted'})
            
