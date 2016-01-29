from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib import auth
from django.contrib.auth import login
from django.core.context_processors import csrf

def index(request):
	template = loader.get_template('customercost/login.html')
	return HttpResponse(template.render())
    #return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

def login_view(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'post':
		username = request.POST['Username']
		password = request.POST['Password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return render_to_response(request, "customercost/index.html", c)
			else:
				error = 'Invalid account.'
				return errorHandler(error)
		else:
				error = 'Invalid details entered.'
				return errorHandler(error)

	return HttpResponseRedirect('customercost/login.html')

	def logout_view(request):
		auth.logout(request)
		return HttpResponseRedirect("customercost/login.html")