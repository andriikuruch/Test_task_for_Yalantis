from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'date_start', 'date_end', 'number_of_lectures')

    def validate(self, data):
        errors = []

        if data['date_start'] > data['date_end']:
            errors.append({'date_end': 'Finish date must be occur after start.'})

        if data['number_of_lectures'] < 0:
            errors.append({'number_of_lectures': 'Number of lectures must be positive number.'})

        if errors:
            raise serializers.ValidationError(*errors)
