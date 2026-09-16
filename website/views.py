from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse ("<h1>Home page</h1>") 

def about_view(request):
    return HttpResponse ("<h1>about us </h1>")


def contact_view(request):
    return HttpResponse ("<h1>contact us</h1>")