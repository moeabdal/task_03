from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [
    		{
    			"restaurant_name" : "Sakura",
    			"food_type" : "Sushi"
    		}, 
    		{
    			"restaurant_name" : "Burger Boutique",
    			"food_type" : "Burgers"
    		}, 
    		{
    			"restaurant_name" : "Terrace Grill",
    			"food_type" : "Steaks"
    		}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
    		"restaurant_name" : "Sakura",
    		"food_type" : "Sushi"
    	}

    }
    return render(request, 'detail.html', context)
