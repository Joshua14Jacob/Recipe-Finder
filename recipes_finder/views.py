from django.shortcuts import render, HttpResponse

recipes = [
    {
        'title': 'Pasta Carbonara',
        'picture': 'pasta_carbonara.jpg',
        'ingredients': [
            'Spaghetti',
            'Eggs',
            'Bacon',
            'Parmesan',
            'Pepper'
        ],
        'instructions': [
            'Boil the spaghetti',
            'Fry the bacon',
            'Mix the eggs and parmesan',
            'Mix everything together'
        ]
    },
    {
        'title': 'Pasta Bolognese',
        'picture': 'pasta_bolognese.jpg',
        'ingredients': [
            'Spaghetti',
            'Beef',
            'Tomato sauce',
            'Onion',
            'Garlic'
        ],
        'instructions': [
            'Boil the spaghetti',
            'Fry the beef',
            'Fry the onion and garlic',
            'Mix everything together'
        ]
    },
    {
        'title': 'Pasta Pesto',
        'picture': 'pasta_pesto.jpg',
        'ingredients': [
            'Spaghetti',
            'Basil',
            'Pine nuts',
            'Parmesan',
            'Garlic'
        ],
        'instructions': [
            'Boil the spaghetti',
            'Blend the basil, pine nuts, parmesan, and garlic',
            'Mix everything together'
        ]
    }
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes_finder/home.html', context)

def about(request):
    return render(request, 'recipes_finder/about.html')