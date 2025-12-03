from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)

    @property
    def vote_count(self):
        return self.votes.count()

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['poll', 'user'], name='unique_user_vote', condition=models.Q(user__isnull=False)),
            models.UniqueConstraint(fields=['poll', 'ip_address'], name='unique_ip_vote', condition=models.Q(ip_address__isnull=False)),
        ]

    def __str__(self):
        return f"Vote for {self.choice}"

# Create your models here.
