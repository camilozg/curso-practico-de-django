from .models import Link


def context(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context
