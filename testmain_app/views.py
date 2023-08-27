from django.shortcuts import render, redirect

# Define the home view function
def home(request):
    # Render the 'index.html' template
    return render(request, 'index.html')


