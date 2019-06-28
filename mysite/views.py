from django.shortcuts import render

# Create your views here.
def home_page(request):
	title="HomePage"
	return render(request,"try.html")
