from django.urls import path
from .views import CourseListView, CourseCreateView, CourseRetrieveUpdateDestroyView

app_name = 'catalog'

urlpatterns = [
    path('', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('course/<int:pk>', CourseRetrieveUpdateDestroyView.as_view()),
]
