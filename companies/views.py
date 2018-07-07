from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializer import StockSerializer

# Create your views here.

# Lists all stocks or lets you create a new stock.
# stocks/
class  StockList(APIView):

    def get(self, request):
        all_stocks = Stock.objects.all()
        serialized_data = StockSerializer(all_stocks, many=True)
        return Response(serialized_data.data)

    def post(self, request):
        serialized_data = StockSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
