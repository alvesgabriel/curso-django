from django.shortcuts import render

videos = [
    {"slug": "motivacao", "titulo": "Vídeo Aperitivo: Motivação", "vimeo_id": 459799222},
    {"slug": "instalacao-windows", "titulo": "Instalação Windows", "vimeo_id": 251497668},
]

videos_dct = {video["slug"]: video for video in videos}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
