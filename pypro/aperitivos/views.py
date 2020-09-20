from django.shortcuts import render


def videos(request, slug):
    video = {"titulo": "Vídeo Aperitivo: Motivação", "vimeo_id": 459799222}
    return render(request, "aperitivos/video.html", context={"video": video})
