from django.shortcuts import render
from rest_framework import viewsets,status
from admin.products.serializers import ProductsSerializer
from .models import Product
from rest_framework.response import Response 

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products   (get request)
        products = Product.object.objects.all
        serializer = ProductsSerializer(products , many=True)   
        return Response(serializer.data) 
            
    def create(self , request):  #/api/products    (post request)
        serializer = ProductsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    
    def retrieve(self , request , pk=None): #/api/products /<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    
    def update(self , request , pk=None): #/api/products /<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductsSerializer(instance=product , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    def destroy(self , request , pk=None): #/api/products /<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
