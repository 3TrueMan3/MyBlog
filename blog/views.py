from django.shortcuts import render


def posts_list(request):
    n = ['Michael', 'Masha', 'Kolya', 'Ksu']
    return render(request, 'blog/index.html', context={'names': n})
