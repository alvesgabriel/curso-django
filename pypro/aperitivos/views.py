from django.shortcuts import render


def videos(request, slug):
    return render(request, "aperitivos/video.html")
