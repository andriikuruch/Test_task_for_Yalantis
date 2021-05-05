from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course


class CourseCreateTestCase(APITestCase):
    def test_create_course_success(self):
        """Test successful creating of course"""

        url = reverse('catalog:create-course')
        data = {
            'title': 'Python School',
            'date_start': '2021-05-05',
            'date_end': '2021-06-05',
            'number_of_lectures': 7
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        count = Course.objects.count()
        self.assertEqual(count, 1)

        course = Course.objects.get()
        self.assertEqual(course.title, 'Python School')

    def test_create_course_with_wrong_end_date(self):
        """Creating of course with wrong end date"""

        url = reverse('catalog:create-course')
        data = {
            'title': 'Python School',
            'date_start': '2021-05-05',
            'date_end': '2021-04-05',
            'number_of_lectures': 7
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_course_with_wrong_number_of_lectures(self):
        """Creating of course with wrong number of lectures"""

        url = reverse('catalog:create-course')
        data = {
            'title': 'Python School',
            'date_start': '2021-05-05',
            'date_end': '2021-06-05',
            'number_of_lectures': -7
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CourseSearchTestCase(APITestCase):
    def setUp(self):
        Course.objects.create(title='Android Course', date_start='2021-05-05',
                              date_end='2021-06-05', number_of_lectures=5)
        Course.objects.create(title='Android School', date_start='2021-06-05',
                              date_end='2021-07-05', number_of_lectures=5)
        Course.objects.create(title='Python School', date_start='2021-05-05',
                              date_end='2021-06-05', number_of_lectures=5)
        Course.objects.create(title='Python Course', date_start='2021-04-17',
                              date_end='2021-06-05', number_of_lectures=5)

    def test_search_by_title(self):
        """Search courses by title. Choose all courses which starts with ?search=name"""
        url = reverse('catalog:courses') + '?search=Python'
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_filter_by_date_start(self):
        """Filter courses by start date"""
        url = reverse('catalog:courses') + '?date_start=2021-05-05'
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_filter_by_date_end(self):
        """Filter courses by end date"""
        url = reverse('catalog:courses') + '?date_end=2021-06-05'
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)

    def test_search_and_filter_course(self):
        """Search courses by name and filter them by end date"""
        url = reverse('catalog:courses') + '?search=Python' + '&date_end=2021-06-05'
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_get_all_courses(self):
        """Give all courses in catalog"""
        url = reverse('catalog:courses')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 4)


class CourseRetrieveUpdateDestroyTestCase(APITestCase):
    def setUp(self):
        Course.objects.create(title='Android Course', date_start='2021-05-05',
                              date_end='2021-06-05', number_of_lectures=5)
        Course.objects.create(title='Android School', date_start='2021-06-05',
                              date_end='2021-07-05', number_of_lectures=5)
        Course.objects.create(title='Python School', date_start='2021-05-05',
                              date_end='2021-06-05', number_of_lectures=5)
        Course.objects.create(title='Python Course', date_start='2021-04-17',
                              date_end='2021-06-05', number_of_lectures=5)

    def test_retrive_course(self):
        """Get course by id"""
        url = reverse('catalog:course', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_update_course(self):
        """Update course with concrete id"""
        url = reverse('catalog:course', args=[1])
        data = {
            'title': 'Android Course',
            'date_start': '2021-05-05',
            'date_end': '2021-06-05',
            'number_of_lectures': 15
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number_of_lectures'], 15)

    def test_destory_course(self):
        """Delete course by id"""
        url = reverse('catalog:course', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('catalog:courses')
        response = self.client.get(url)
        self.assertEquals(len(response.data), 3)
