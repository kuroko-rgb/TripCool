from django.shortcuts import render


def post_list(request):
    return render(request, 'Reserva/post_list.html', {})
