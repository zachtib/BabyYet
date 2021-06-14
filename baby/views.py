from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404

from baby.models import Baby


def home(request):
    baby = Baby.objects.default()
    context = {
        'mother': settings.MOTHERS_NAME,
        'show_banner': settings.SHOW_BANNER,
        'show_admin_link': False
    }
    if baby.born:
        context['answer'] = settings.YES_DISPLAY
        if baby.name is not None and baby.name != '':
            context['name'] = baby.name
        if baby.born_on is not None:
            context['timestamp'] = baby.born_on
        if baby.extra is not None:
            context['extra'] = baby.extra
        if baby.announce_url is not None:
            context['url'] = baby.announce_url
    else:
        context['answer'] = settings.NO_DISPLAY
        context['due_date'] = baby.due_date
    if request.user.is_authenticated and request.user.is_staff:
        context['show_admin_link'] = True
        context['admin_link'] = f"/admin/baby/baby/{baby.id}/change/"

    return render(request, 'baby/home.html', context)


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
