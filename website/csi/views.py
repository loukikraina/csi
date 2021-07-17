from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.http import JsonResponse
from django.views.generic.base import TemplateView  # new
from django.shortcuts import render, get_object_or_404, redirect


from django.urls import reverse
from django.db import IntegrityError
# from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Events


def get_events(request, pk):
    obj = get_object_or_404(Events, pk=pk)
    return render(request, 'donor/donor_profile.html', context = {'object' : obj})


def home(request):
    context = {}
    return render(request, 'csi\index.html', context)



class Events1(generic.ListView):
    model = Events
    template_name = 'csi\events.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f_obj'] = Events.objects.all().filter(current = True)
        return context
    # def get_queryset(self):
    #     return Events.objects.filter(do)

# def events(request):
#     # obj = get_object_or_404(Events, pk=pk)
#     # context = {'object' : obj}
#     event = Events.objects.all()

#     return render(request, 'csi\events.html', context = {'object_list': event })

def event_detail_view(request, pk):
    if request.is_ajax():
        obj = Events.objects.get(pk=pk)
        data = {
            'name': obj.name,
            'link': obj.link,
            'description': obj.description,
            'date': obj.date,
            'image': obj.image_url,
        }
        return JsonResponse({'data': data})
    return redirect('events')



def contactus(request):
    context = {}
    return render(request, 'csi\contactus.html', context)


def about_us(request):
    context = {}
    return render(request, 'csi\\about_us.html', context)
