from django.shortcuts import render
from tasks.models import TaskModel
from .serializers import TaskModelSerializer, ResgisterSerializer, LoginSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator


# # Create your views here.


class RegisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = ResgisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status': True, 'message':'user created',},status.HTTP_201_CREATED)

class LoginAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data
        )
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        user = authenticate(username=serializer.data["username"], password=serializer.data["password"])
        if not user:
            return Response({
                'status': False,
                'message': "invalid credentials",
            }, status.HTTP_400_BAD_REQUEST)
        token,_ = Token.objects.get_or_create(user=user)
        print(token)

        return Response({'status': True, 'message':'user logged in','token':str(token)},status.HTTP_200_OK)
        

# FUNCTION BASED VIEW
# -----------------------------------------------------
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def dataview(request):

    if request.method=='GET':
        obj = TaskModel.objects.all()
        serializer = TaskModelSerializer(obj, many=True)  # Serialize the queryset
        page = request.GET.get('page', 1)
        page_size = 3
        if request.method == 'GET':
            return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = TaskModelSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method == "Put":
        print("Put")
        data = request.data
        obj = TaskModel.objects.get(id=data['id'])
        serializer = TaskModelSerializer(obj,data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "DELETE":
        print("DELETE")
        data = request.data
        obj = TaskModel.objects.get(id=data['id'])
        obj.delete()

        return Response({'message': 'Task Deleted'})

# #  CLASS BASED VIEWS
# # ---------------------------------

# class TaskAPIView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         tasks = TaskModel.objects.all()
#         serializer = TaskModelSerializer(tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TaskModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request):
#         try:
#             task = TaskModel.objects.get(id=request.data['id'])
#         except TaskModel.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = TaskModelSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         try:
#             task = TaskModel.objects.get(id=request.data['id'])
#         except TaskModel.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         task.delete()
#         return Response({'message': 'Task Deleted'}, status=status.HTTP_200_OK)

# #  GENERIC CLASS BASED VIEWS
# # ---------------------------------
# from rest_framework import generics
# from tasks.models import TaskModel
# from .serializers import TaskModelSerializer

# class TaskListCreateAPIView(generics.ListCreateAPIView):
#     queryset = TaskModel.objects.all()
#     serializer_class = TaskModelSerializer

# class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TaskModel.objects.all()
#     serializer_class = TaskModelSerializer
