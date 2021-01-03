from django.conf import settings
from django.shortcuts import render, get_object_or_404

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
            'due_date': baby.due_date
        })


def secret(request, secret_id):
    baby = get_object_or_404(Baby, secret_id=secret_id)

    return render(request, 'baby/home.html', {
        'mother': settings.MOTHERS_NAME,
        'answer': f'Secret page for {baby.name}',
    })
