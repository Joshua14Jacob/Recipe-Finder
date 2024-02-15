from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
import requests
from recipes_finder.forms import InputForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']

            try:
                response = requests.get('https://api.edamam.com/search', params={'q': user_input, 'app_id': '17d883af', 'app_key': '91f71924206bd50b299d417b819a84eb'})
                response.raise_for_status()  # Raise exception for HTTP errors
                data = response.json()
                return render(request, 'recipes_finder/home.html', {'form': form, 'data': data})
            except requests.RequestException as e:
                # Handle request exceptions (e.g., network errors, API changes)
                return HttpResponse("An error occurred: {}".format(e))
        else:
            # Form is not valid, render form with validation errors
            return render(request, 'recipes_finder/home.html', {'form': form})
    else:
        form = InputForm()
    return render(request, 'recipes_finder/home.html', {'form': form})


def about(request):
    return render(request, 'recipes_finder/about.html')