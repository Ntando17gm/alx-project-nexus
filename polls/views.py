from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from .serializers import PollCreateSerializer, PollDetailSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone


class PollViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Poll.objects.filter(is_active=True)
        if queryset.exists():
            queryset = queryset.filter(expires_at__gt=timezone.now())
        serializer = PollDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollDetailSerializer(poll)
        return Response(serializer.data)

    def create(self, request):
        serializer = PollCreateSerializer(data=request.data)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollDetailSerializer(poll).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        poll = get_object_or_404(Poll, pk=pk)
        choice_id = request.data.get('choice_id')

        if not choice_id:
            return Response({"detail": "choice_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        choice = get_object_or_404(Choice, id=choice_id, poll=poll)

        # Prevent duplicate voting
        ip = request.META.get('REMOTE_ADDR')
        if request.user.is_authenticated:
            already_voted = Vote.objects.filter(poll=poll, user=request.user).exists()
        else:
            already_voted = Vote.objects.filter(poll=poll, ip_address=ip).exists()

        if already_voted:
            return Response({"detail": "You have already voted on this poll."},
                            status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(choice=choice, poll=poll, user=request.user if request.user.is_authenticated else None, ip_address=ip)
        return Response(PollDetailSerializer(poll).data)

# Create your views here.
