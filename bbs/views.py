# Class 기반 View 처리
from bbs.models import Bbs
from bbs.serializers import BbsSerializer
from rest_framework import generics

class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer

class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer


# 함수 기반 View 처리
# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from bbs.models import Bbs
# from bbs.serializers import BbsSerializer
#
#
# @api_view(['GET', 'POST'])
# def bbs_list(request, format=None):
#     if request.method == 'GET':
#         bbs = Bbs.objects.all()
#         serializer = BbsSerializer(bbs, many=True) # many 값이 True 이면 다수의 Data instance를 직렬화할 수 있다.
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BbsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','POST','DELETE'])
# def bbs_detail(request, pk, format=None):
#     try:
#         bbs = Bbs.objects.get(pk=pk)
#     except Bbs.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = BbsSerializer(bbs)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = BbsSerializer(bbs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         bbs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)