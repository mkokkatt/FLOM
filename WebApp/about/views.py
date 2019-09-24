from django.shortcuts import render_to_response

# Create your views here. A view is a Python function that takes a web request and returns a web response.

def index(request):
	'''
	@return the display for the about page
	'''
	return render_to_response('about/templates/html/about.html')

