from django.conf import settings
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from baby.forms import UpdateBabyForm
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
        context['baby_name'] = baby.name
        if baby.born_on is not None:
            context['time'] = baby.born_on.time()
            context['date'] = baby.born_on.date()
    else:
        context['answer'] = settings.NO_DISPLAY
        context['due_date'] = baby.due_date
    if request.user.is_authenticated and request.user.is_staff:
        context['show_admin_link'] = True
        context['admin_link'] = baby.get_absolute_url()

    return render(request, 'baby/home.html', context)


def secret(request, secret_id):
    baby = get_object_or_404(Baby, secret_id=secret_id)
    if request.method == 'POST':
        form = UpdateBabyForm(data=request.POST, instance=baby)
        if form.is_valid():
            form.save()
            from django.shortcuts import redirect
            return redirect('home')
    else:
        form = UpdateBabyForm(instance=baby)
    return render(request, 'baby/secret.html', {
        'baby_name': baby.name,
        'form': form,
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
