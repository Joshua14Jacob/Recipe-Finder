import os
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
import requests
from recipes_finder.forms import InputForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from recipes_finder.ai_imp import run


# Load the model and labels
model = load_model(r"C:\Users\joshu\Desktop\CODE\Projects\Recipe Finder\Recipe-Finder\recipes_finder\FV.h5")

labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
          7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
          14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
          26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
          32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

fruits = ['apple', 'banana', 'bello pepper', 'chilli pepper', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'mango', 'orange',
          'paprika', 'pear', 'pineapple', 'pomegranate', 'watermelon']
vegetables = ['beetroot', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'corn', 'cucumber', 'eggplant', 'ginger',
              'lettuce', 'onion', 'peas', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato',
              'tomato', 'turnip']



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
    # run()
    if request.method == 'POST':
        # Handle image upload
        uploaded_image = request.FILES['image']
        # Save the uploaded image to a temporary location
        with open('temp_image.jpg', 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)
        
        # Perform image classification
        prediction = classify_image('temp_image.jpg')
        
        # Delete the temporary image file
        os.remove('temp_image.jpg')
        
        return render(request, 'recipes_finder/about.html', {'prediction': prediction})
    return render(request, 'recipes_finder/about.html')


def classify_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    y_class = classes.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    predicted_class = int(y)
    # predicted_class = labels[y]
    # print(y_class)
    # predicted_class = np.argmax(classes)
    if labels[predicted_class] in fruits:
        return "Fruit: " + labels[predicted_class]
    elif labels[predicted_class] in vegetables:
        return "Vegetable: " + labels[predicted_class]
    else:
        return "Unknown"