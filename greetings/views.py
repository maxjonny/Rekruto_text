from django.shortcuts import render, redirect
# Create your views here.


def index_view(request):
    if request.GET:
        context = {'name': "Hello, {}!".format(request.GET['name']), 'message': request.GET['message']}
        return render(request, 'greetings/index2.html', context=context)
    else:
        return redirect('http://127.0.0.1:8000?name=Rekruto&message=Давай+дружить!')
