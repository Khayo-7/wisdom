from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class mobile_api(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'first msg', 
            'second msg',
            'third msg'
        ]
        return Response({'message':'Loser', 'an_apiview': an_apiview})

def abc(request, format=None):
    return render(request, 'abc.html')