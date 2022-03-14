from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'price', 'estimated_time', 'details', 'reserved', 'created_at', 'user']
        read_only_fields = ['reserved', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, attrs):
        self.price_between(attrs)

        self.price_and_estimated_time_limit(attrs)

        return super().validate(attrs)

    def price_between(self, attrs):
        if attrs['price'] < 1000 or attrs['price'] > 50000:
            raise serializers.ValidationError({'price': 'The price should be between 1000 and 50,000.'})

    def price_and_estimated_time_limit(self, attrs):
        if attrs['estimated_time'] <= 3 and attrs['price'] >= 30000:
            raise serializers.ValidationError(
                {'error': 'The cost of work less than three days should be less than 30,000'})
