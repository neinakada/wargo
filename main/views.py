from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Neina Akada Maula',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
