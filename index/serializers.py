from django.contrib.auth.models import User, Group
from rest_framework import serializers

from index.models import Role


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'role']

    def get_role(self, obj):
        return obj.role_set.get().get_role()

    def create(self, validated_data):
        user = super().create(validated_data)
        user.role_set.create(role=self.initial_data.get('role'))
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.role_set.update(role=self.initial_data.get('role'))
        return instance


class RoleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Role
        fields = ['user', 'role']
