from django.shortcuts import render
from collections import Counter

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['message']
	reversed_text = user_text[::-1]
	number_words = len(user_text.split())
	return render(request, 'reverse.html', {'usertext':user_text, 'reversed':reversed_text, 'number_words':number_words})