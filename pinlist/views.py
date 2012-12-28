# Create your views here.
from pinlist.models import Pin
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.template.response import TemplateResponse
from django.template import Context, loader, RequestContext

def home(request):

    video = Pin.objects.all().order_by('-published')

    return render_to_response('pinlist/home.html', {"video":video},context_instance=RequestContext(request))


def register(request):
    if not settings.ALLOW_NEW_REGISTRATIONS:
        messages.error(request, "The admin of this service is not "
                                "allowing new registrations.")
        return HttpResponseRedirect(reverse('pins:recent-pins'))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering, you can now '
                                      'login.')
            return HttpResponseRedirect(reverse('pinlist:login'))
    else:
        form = UserCreationForm()

    return render_to_response('pinlist/register.html', {'form': form} ,context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect(reverse('core:home'))