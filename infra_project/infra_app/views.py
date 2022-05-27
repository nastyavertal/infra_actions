from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось и я почти все понимаю!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
