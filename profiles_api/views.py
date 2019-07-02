from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions

class HelloAPIView(APIView):
    """Class for sample API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to the traditional Django view',
            'Gives you the most control over the app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with the name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request,pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})
        

class HelloViewSet(viewsets.ViewSet):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a basic list of responses"""
        a_viewset = [
            "Uses actions (list, create, update, delete, partial update)",
            "Automatically maps to URLS using routers",
            "Provides more functionality using less code"
        ]

        return Response({'message':'hello','a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message':f'Hello {name}'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk=None):
        """Handle getting an object by ID"""
        return Response({'http_method':'retrieve'})

    def update(self, request,pk=None):
        """Handle update of an object"""
        return Response({'http_method':'update'})

    def partial_update(self, request,pk=None):
        """Handle partial update an object"""
        return Response({'http_method':'partial update'})
    
    def destroy(self, request,pk=None):
        """Handle deleting an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating viewsets"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)