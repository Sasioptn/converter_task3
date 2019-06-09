from .celery import app
from django.core.mail import send_mail
from django.conf import settings


@app.task
def convert_video(link):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    ydl = YoutubeDL(options)
    extracted_info_about_video = ydl.extract_info(link, download=False)
    download_link = extracted_info_about_video['url']
    return download_link


@app.task
def sendMusicToGmail(link, email):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    ydl = YoutubeDL(options)
    extracted_info_about_video = ydl.extract_info(link, download=False)
    download_link = extracted_info_about_video['url']
    link = ('http://127.0.0.1:8000/media/' + download_link).replace(" ", "%20") + '.mp3'
    send_mail('Click to download', link, settings.EMAIL_HOST_USER, [email], fail_silently=False)