from django.shortcuts import render

posts = [
	{
		'author':'Harshil',
		'title':'Blog post 1',
		'content': 'First post content',
		'date_posted':'16 february, 2019'

	},
	{
		'author':'macbook',
		'title':'Blog post 2',
		'content':'second post content',
		'date_posted':'17 february, 2019'

	}
]

def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog/home.html',context) 

def about(request):
	return render(request, 'blog/about.html') 

