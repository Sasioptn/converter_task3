from __future__ import unicode_literals

from django.shortcuts import render
from .forms import DownloadForm
from .models import Video
from .tasks import *
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            Video.objects.create(link=link, email=email)
            sendMusicToGmail.delay(link, email)
            messages.success(request,'Ваш видео сконвертировано и отправлено вам на gmail')
            return render(request, 'convert/index.html', {'form': form})
    else:
        form = DownloadForm()
    return render(request, 'convert/index.html', {'form': form})