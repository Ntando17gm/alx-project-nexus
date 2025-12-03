from rest_framework import serializers
from .models import Poll, Choice, Vote


class ChoiceSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'vote_count']


class PollCreateSerializer(serializers.ModelSerializer):
    choices = serializers.ListField(
        child=serializers.CharField(max_length=200), write_only=True
    )

    class Meta:
        model = Poll
        fields = ['question', 'expires_at', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data)
        for text in choices_data:
            Choice.objects.create(poll=poll, choice_text=text)
        return poll


class PollDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ['id', 'question', 'created_at', 'expires_at', 'is_active', 'choices', 'total_votes']

    def get_total_votes(self, obj):
        return Vote.objects.filter(poll=obj).count()