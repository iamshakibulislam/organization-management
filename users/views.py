from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth
import json
from django.http import JsonResponse

def signup(request):
	if request.method == 'GET':
		return render(request,'signup.html')


	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		organization = request.POST['organization']
		password = request.POST['password']
		password2 = request.POST['password2']


		if password != password2:
			return render(request,'signup.html',{'error':'password did not match !'})


		if len(User.objects.filter(email=email)) != 0:
			return render(request,'signup.html',{'error':'User with this email already exists !'})


		if(len(User.objects.filter(organization=organization))!=0):
			return render(request,'signup.html',{'error':'This organization is already registered.Contact Administrator to join you !'})



		create_user=User.objects.create_user(email=email,organization=organization,first_name=first_name,last_name=last_name,password=password)
		create_user.save()

		

		return render(request,'signup.html',{'success':'Account has been created ! Try login'})







def login(request):
	if request.method == 'GET':
		return render(request,'login.html')


	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']


		check_user = User.objects.filter(email=email)

		if len(check_user) == 0:
			return render(request,'login.html',{'alert':'Email or password is wrong !'})


		else :

			authenticate = auth.authenticate(email=email,password=password)

			if authenticate is not None :

				auth.login(request,authenticate)
				print(authenticate)

				return redirect('home')


			else :
				return render(request,'login.html',{'alert':'Email or password is wrong !'})






def addMember(request):
	if request.method == 'GET':
		first_name = request.GET['first_name']
		last_name = request.GET['last_name']
		email = request.GET['email']
		role = request.GET['role']
		password = request.GET['password']
		phone = request.GET['phone']

		if(len(User.objects.filter(email=email))!=0):
			return JsonResponse({'status':'user exists'})


		
		if(role == 'Administrator'):
			User.objects.create_user(first_name=first_name,last_name=last_name,email=email,is_admin=True,password=password,organization=request.user.organization,phone=phone,added_by_user_id=request.user.id)



		if(role == 'Officer'):
			User.objects.create_user(first_name=first_name,last_name=last_name,email=email,is_officer=True,is_admin=False,password=password,organization=request.user.organization,phone=phone,added_by_user_id=request.user.id)



		if(role == 'Moderator'):
			User.objects.create_user(first_name=first_name,last_name=last_name,email=email,is_moderator=True,is_admin=False,password=password,organization=request.user.organization,phone=phone,added_by_user_id=request.user.id)



		return JsonResponse({'status':'user created'})

