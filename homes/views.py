from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Home
from .serializers import HomeSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_homes(request):
    homes = Home.objects.all()
    serializer = HomeSerializer(homes, many=True)
    return Response({"homes": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_home(request, pk):
    home = get_object_or_404(Home, id=pk)
    serializer = HomeSerializer(home)
    return Response({"home": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_home(request):
    serializer = HomeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(
            {"home": serializer.data},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_home(request, pk):
    home = get_object_or_404(Home, id=pk)

    if home.user != request.user:
        return Response(
            {"error": "You do not have permission to update this home"},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = HomeSerializer(home, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"home": serializer.data}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_home(request, pk):
    home = get_object_or_404(Home, id=pk)

    if home.user != request.user:
        return Response(
            {"error": "You do not have permission to delete this home"},
            status=status.HTTP_403_FORBIDDEN
        )

    home.delete()
    return Response(
        {"message": "Home deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


