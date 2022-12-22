from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'POST':
        return Response('Created', status=status.HTTP_201_CREATED)

    return Response('List of the books', status=status.HTTP_200_OK)


# Routing to a class method
class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)


# Routing class-based views
class BookView(APIView):
    def get(self, request, pk):
        return Response({'message': 'single book with id ' + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({'title': request.data.get('title')}, status.HTTP_200_OK)


# Routing classes that extend viewsets
class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'All books'}, status.HTTP_200_OK)

    def create(self, request):
        return Response({'message': 'Creating a book'}, status.HTTP_201_CREATED)

    def update(self, request):
        return Response({'message': 'Updating a book'}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({'message': 'Displaying a book'}, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({'message': 'Partially updating a book'}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({'message': 'Deleting a book'}, status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "Secrete message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only Manager Should See This"}, 200)
    else:
        return Response({"message": "You are not authorized"}, 403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttles_check(request):
    return Response({"message": "successful"})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message": "message for the logged in users only"})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth_in_ten(request):
    return Response({"message": "message for the logged in users only"})
