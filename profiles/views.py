from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class mobile_api(APIView):

    serializer_class = serializers.ser

    def get(self, request, format=None):

        an_apiview = [
            'first msg', 
            'second msg',
            'third msg'
        ]
        return Response({'message':'Loser', 'an_apiview': an_apiview})

    def post(self, request):

        serializer = serializers.ser(data=request.data)
        
        if serializer.is_valid():
            fname = serializer.data.get('first_name')
            message = 'hey {0}'.format(fname)

            return Response({'message':message})
        
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):

        return Response({'methode':'Put'})
        
    def patch(self, request, pk=None):

        return Response({'methode':'Patch'})
        
    def detete(self, request, pk=None):

        return Response({'methode':'Delete'})
       

def abc(request, format=None):
    return render(request, 'abc.html')