from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404

from baby.models import Baby


def home(request):
    baby = Baby.objects.default()
    context = {
        'mother': settings.MOTHERS_NAME,
        'show_banner': settings.SHOW_BANNER,
    }
    if baby.born:
        context['answer'] = settings.YES_DISPLAY
    else:
        context['answer'] = settings.NO_DISPLAY
        context['due_date'] = baby.due_date
    return render(request, 'baby/home.html', context)


def secret(request, secret_id):
    baby = get_object_or_404(Baby, secret_id=secret_id)

    return render(request, 'baby/home.html', {
        'mother': settings.MOTHERS_NAME,
        'answer': f'Secret page for {baby.name}',
    })


def api(request):
    if request.method == 'POST':
        raise Http404()

    baby = Baby.objects.default()
    data = {
        'born': baby.born,
    }
    if baby.born:
        data['display'] = settings.YES_DISPLAY
    else:
        data['display'] = settings.NO_DISPLAY
        data['due_date'] = baby.due_date
    return JsonResponse(data)
