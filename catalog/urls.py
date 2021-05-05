from django.urls import path
from .views import CourseListView, CourseCreateView, CourseRetrieveUpdateDestroyView

app_name = 'catalog'

urlpatterns = [
    path('', CourseListView.as_view(), name="courses"),
    path('create/', CourseCreateView.as_view(), name="create-course"),
    path('course/<int:pk>', CourseRetrieveUpdateDestroyView.as_view(), name="course"),
]
