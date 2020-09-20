from django.shortcuts import render


def videos(request, slug):
    videos = {
        "motivacao": {"titulo": "Vídeo Aperitivo: Motivação", "vimeo_id": 459799222},
        "instalacao-windows": {"titulo": "Instalação Windows", "vimeo_id": 251497668},
    }
    video = videos[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
