from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth
#import django messages
from django.contrib import messages
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
			create_user=User.objects.create_user(email=email,organization=organization,first_name=first_name,last_name=last_name,password=password,is_active=False,is_admin=False,is_officer=False,is_moderator=False,has_tour_perm=False)
			create_user.save()
			return render(request,'signup.html',{'error':'Registration successful ! Please Wait For Admin Approval !'})



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
			return render(request,'index.html',{'alert':'Email or password is wrong !'})

		
		elif len(check_user) != 0 and check_user[0].is_active == False:
			return render(request,'index.html',{'alert':'Your account is not approved yet !'})


		else :

			authenticate = auth.authenticate(email=email,password=password)

			if authenticate is not None :

				auth.login(request,authenticate)
				
				if request.user.is_admin:
					return redirect('home')

				if request.user.is_moderator:
					return redirect('home')
				
				if request.user.has_tour_perm:
					return redirect('tourmanagement')

				if request.user.has_procurement_perm:
					return redirect('main_procurement_page')

				if request.user.has_training_perm:
					return redirect('training_list')


				return redirect('home')


			else :
				return render(request,'index.html',{'alert':'Email or password is wrong !'})






def addMember(request):
	if request.method == 'GET':
		first_name = request.GET['first_name']
		last_name = request.GET['last_name']
		email = request.GET['email']
		role = request.GET['role']
		password = request.GET['password']
		phone = request.GET['phone']

		has_tour_perm = int(request.GET['has_tour_perm'])
		has_procurement_perm = int(request.GET['has_procurement_perm'])
		has_training_perm = int(request.GET['has_training_perm'])
		has_edit_perm = int(request.GET['has_edit_perm'])
		has_delete_perm = int(request.GET['has_delete_perm'])

		if(len(User.objects.filter(email=email))!=0):
			return JsonResponse({'status':'user exists'})


		
		if(role == 'Administrator'):
			User.objects.create_user(first_name=first_name,
			last_name=last_name,
			email=email,
			is_admin=True,
			password=password,
			organization=request.user.organization,
			phone=phone,
			added_by_user_id=request.user.id,
			has_tour_perm=has_tour_perm,
			has_procurement_perm=has_procurement_perm,
			has_training_perm=has_training_perm,
			has_edit_perm=has_edit_perm,
			has_delete_perm=has_delete_perm)




		if(role == 'Officer'):
			User.objects.create_user(first_name=first_name,
			last_name=last_name,
			email=email,
			is_moderator=False,
			is_officer=True,
			is_admin=False,
			password=password,
			organization=request.user.organization,
			phone=phone,
			added_by_user_id=request.user.id,
			has_tour_perm=has_tour_perm,
			has_procurement_perm=has_procurement_perm,
			has_training_perm=has_training_perm,
			has_edit_perm=has_edit_perm,
			has_delete_perm=has_delete_perm)



		if(role == 'Moderator'):
			User.objects.create_user(first_name=first_name,
			last_name=last_name,
			email=email,
			is_officer=False,
			is_moderator=True,
			is_admin=False,
			password=password,
			organization=request.user.organization,
			phone=phone,
			added_by_user_id=request.user.id,
			has_tour_perm=has_tour_perm,
			has_procurement_perm=has_procurement_perm,
			has_training_perm=has_training_perm,
			has_edit_perm=has_edit_perm,
			has_delete_perm=has_delete_perm)

		if(role == 'PO User'):
			User.objects.create_user(first_name=first_name,
			last_name=last_name,
			email=email,
			is_officer=False,
			is_moderator=False,
			is_admin=False,
			is_po_user=True,
			password=password,
			organization=request.user.organization,
			phone=phone,
			added_by_user_id=request.user.id,
			has_tour_perm=has_tour_perm,
			has_procurement_perm=has_procurement_perm,
			has_training_perm=has_training_perm,
			has_edit_perm=has_edit_perm,
			has_delete_perm=has_delete_perm)




		return JsonResponse({'status':'user created'})


def logout(requst):
	auth.logout(requst)
	return redirect('index_page')


def profile(request):
	if request.method == 'GET':
		return render(request,'profile.html')

	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name= request.POST['last_name']
		phone = request.POST['phone_number']
		address = request.POST['address']
		try:
			profile_picture = request.FILES['profile_picture']
		except:
			pass


		user = User.objects.get(id=request.user.id)
		user.first_name = first_name
		user.last_name = last_name
		user.phone = phone
		user.address = address
		try:
			user.profile_picture = profile_picture
		except:
			pass
		user.save()

		messages.success(request,'Profile has been updated !')

		return redirect('profile')

