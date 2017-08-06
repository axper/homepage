from django.views.generic import ListView

from challenges.models import Challenge


class ChallengeList(ListView):
    model = Challenge
