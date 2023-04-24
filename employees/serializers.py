from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }

    def create(self, validated_data):
        return Employee.objects.create_user(**validated_data)
