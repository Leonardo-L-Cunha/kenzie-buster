from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all(), message='email already registered.')]
        )
    username = serializers.CharField(
        max_length=150, 
        validators=[UniqueValidator(queryset=User.objects.all(), message='username already taken.')]
        )
    first_name =serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    password = serializers.CharField(max_length= 127, write_only=True)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True, default=False)
    
    def create(self, validated_data) -> User:
        is_employee = validated_data.get('is_employee')
        
        if is_employee:
            return User.objects.create_superuser(**validated_data)
        
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data:dict):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')

        for key, value in validated_data.items():
            setattr(instance, key , value)

        instance.save()

        return instance

    
