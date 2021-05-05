from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date_start', 'date_end']
    search_fields = ['^title']


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
