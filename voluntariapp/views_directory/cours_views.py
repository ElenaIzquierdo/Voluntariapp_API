# voluntariapp/views_directory/cours_views.py
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from voluntariapp.models import Cours
from voluntariapp.serializers import CoursSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from django.http import JsonResponse

class ListCoursView(generics.ListAPIView):
    queryset = Cours.objects.all()
    parser_classes = (MultiPartParser, JSONParser,)
    serializer_class = CoursSerializer

    def get(self, request, *args, **kwargs):
        queryset = Cours.objects.all()
        serializer = CoursSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET cours/:id/
    PUT cours/:id/
    DELETE cours/:id/
    """
    queryset = Cours.objects.all()
    parser_classes = (MultiPartParser, JSONParser)
    serializer_class = CoursSerializer

    def get(self, request, id_cours):
        a_cours = get_object_or_404(Cours,pk=id_cours)
        serializer = CoursSerializer(a_cours, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id_cours):
        a_cours = get_object_or_404(Cours, pk=id_cours)
        serializer = CoursSerializer(a_cours, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id_cours):
        a_cours = get_object_or_404(Cours, pk=id_cours)
        a_cours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)