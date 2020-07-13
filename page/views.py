from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home.html')

def result(request):
    number_list = list()
    for a in range(6):
        number = request.GET['number' + str(a+1)]
        number_list.append(int(number))

    random_list = list()

    for b in range(7):
        number = random.randomint(1,45)
        random_list.append(int(number))

    count = 0
    for a in range (6) :
        for b in range(7) :
            if( number_list[a] == random_list[b]) :
                count = count + 1 
    return render(request, "result.html", {'number_list':number_list, 'random_list':random_list, 'count' :count } )
    

