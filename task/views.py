from django.shortcuts import render, redirect
from pytube import YouTube
import os

url= ''
def hom(request):

    return render (request, 'task/hom.html',{})

def youtbdown(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    resolutions = []
    videos = yt.streams.filter(progressive=True, file_extension='mp4').all()
    for video in videos:
        resolutions.append(video.resolution)
    resolutions = list(dict.fromkeys(resolutions))
    embed_link = url.replace('youtu.be/', 'youtube.com/embed/')
    name = yt.title
    print('name:',name)

    return render (request, 'task/youtbdown.html', {"res":resolutions , "emb":embed_link, 'name':name})


def download(request, res):
      
    global url
    homedir = os.path.expanduser('~')
    drs = homedir + 'Downloads'
    if request.method == 'POST':
        YouTube(url).streams.get_by_resolution(res).download('E:\Downloads')
        return render(request, 'task/downloaded.html')
    else:
        return render(request, 'task/sorry.html')