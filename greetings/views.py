from django.shortcuts import render, reverse
# Create your views here.


def index_view(request):
    if request.GET:
        context = {'name': "{}!".format(request.GET['name']), 'message': request.GET['message']}
        if request.META.get('QUERY_STRING') != "name=Rekruto&message=%D0%94%D0%B0%D0%B2%D0%B0%D0%B9+%D0%B4%D1%80%D1%83%D0%B6%D0%B8%D1%82%D1%8C!":
            context["name"] = "Hello, "+request.GET['name']+'!'
            context["message"] = request.GET['message']+'!'
        return render(request, 'greetings/index2.html', context=context)
    else:
        return redirect('https://rekruto-test.herokuapp.com/?name=Rekruto&message=Давай+дружить!')




