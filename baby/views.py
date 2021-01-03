from django.conf import settings
from django.shortcuts import render

from baby.models import Baby


def home(request):
    baby = Baby.objects.default()
    if baby.born:
        return render(request, 'baby/home.html', {
            'mother': settings.MOTHERS_NAME,
            'answer': 'Yep.',
        })
    else:
        return render(request, 'baby/home.html', {
            'mother': settings.MOTHERS_NAME,
            'answer': 'Nope.',
        })
