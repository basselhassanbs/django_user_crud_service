from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer

class UserApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        # List all the users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the User with given user data
        '''
        data = {
            'username': request.data.get('username'), 
            'password': request.data.get('password'),
            'active': request.data.get('active'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailApiView(APIView):

    # 3. get by ID
    def get(self, request, id, *args, **kwargs):
    
        # get user by ID
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the user with given id if exists
        '''
        user = User.objects.get(id=id)
        if not user:
            return Response(
                {"res": "Object with user id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'username': request.data.get('username'), 
            'password': request.data.get('password'),
            'active': request.data.get('active'),
        }
        serializer = UserSerializer(instance = user, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, id, *args, **kwargs):
        '''
        Delete the user item with given id if exists
        '''
        user = User.objects.get(id=id)
        if not user:
            return Response(
                {"res": "Object with user id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )