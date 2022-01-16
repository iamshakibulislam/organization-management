from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import *
from django.db.models import Q
from django.http import JsonResponse
@login_required(login_url = '/users/login/')
def home(request):
	if(request.method == 'GET'):

		all_members =0
		members = User.objects.filter(Q(organization=request.user.organization))
		officers_total = len(members.filter(is_officer=True))
		moderators_total = len(members.filter(is_moderator=True))
		admin_total = len(members.filter(is_admin=True))


		if len(members) != 0:
			all_members=members
		context = {
				'all_members':all_members,
				'total_members':len(members),
				'total_officers':officers_total,
				'total_moderators':moderators_total,
				'administrators_total':admin_total
				}

		return render(request,'dashboard/index.html',context)


def edit_members(request):
	if request.method == 'GET':
		userid = int(request.GET['userid'])



		sel_user = User.objects.get(id=userid)
		role = ''
		if sel_user.is_admin == True:
			role = 'Administrator'

		if sel_user.is_officer == True:
			role = 'Officer'

		if sel_user.is_moderator == True:
			role = 'Moderator'

		user_data={'first_name':sel_user.first_name,'last_name':sel_user.last_name,'email':sel_user.email,'phone':sel_user.phone,'role':role,'id':sel_user.id}
		print('userid',userid)

		return JsonResponse({'userdata':user_data})



	if request.method == 'POST':

		first_name = request.POST['first_name_edit']
		last_name = request.POST['last_name_edit']
		email = request.POST['email_edit']
		phone = request.POST['phone_edit']
		role = request.POST['role_edit']

		userid = request.POST['userid']


		sel_user = User.objects.get(id=int(userid))



		if(sel_user.first_name != first_name):
			sel_user.first_name = first_name


		if(sel_user.last_name != last_name):
			sel_user.last_name = last_name

		if(sel_user.email != email and len(User.objects.filter(email=email)) !=0):
			return JsonResponse({'status':'user exists'})

		if(sel_user.email != email):
			sel_user.email = email


		if(sel_user.phone != phone):
			sel_user.phone = phone


		if(role == "Administrator"):
			sel_user.is_officer = False
			sel_user.is_moderator = False
			sel_user.is_admin = True

		if(role == "Officer"):
			sel_user.is_officer = True
			sel_user.is_moderator = False
			sel_user.is_admin == False


		if(role == "Moderator"):
			sel_user.is_officer = False
			sel_user.is_moderator = True
			sel_user.is_admin == False



		sel_user.save()

		return JsonResponse({'status':'updated members information'})




def delete_members(request):
	if request.method == "POST":
		userid = request.POST['userid']

		sel_user = User.objects.get(id=userid)
		sel_user.delete()

		return JsonResponse({'status':'deleted'})




def tour(request):
	if request.method == "GET":
		sel_org_members = User.objects.filter(organization = request.user.organization)
		return render(request,'dashboard/tour.html',{'members':sel_org_members})


	if request.method == 'POST':

		member_id = request.POST.getlist('member')
		
		last_visited = request.POST['last_visited']
		next_visit_date = request.POST['next_visit_date']
		last_meeting_date = request.POST['last_meeting_date']
		next_meeting_date = request.POST['next_meeting_date']
		tour_from = request.POST['tour_from']
		tour_to = request.POST['tour_to']

		
		creating_tour=TourManagement.objects.create(
			organization = request.user.organization,
			last_visited = last_visited,
			next_visit_date = next_visit_date,
			last_meeting_date = last_meeting_date,
			next_meeting_date = next_meeting_date,
			tour_from = tour_from,
			tour_to = tour_to
			)

		for members in member_id:
			try:
				sel_mem = User.objects.get(id=int(members))
			except:
				return redirect('tour')

			creating_tour.tour_members.add(sel_mem)











		return redirect('tourmanagement')





def tourmanagement(request):
	if request.method == 'GET':
		get_tour = TourManagement.objects.filter(organization = request.user.organization)
		print(get_tour)

		tourdata =  []

		for data in get_tour:
			tourdata.append({'id':data.id,
				'members':[name.first_name+' '+name.last_name for name in data.tour_members.all()],
				#'memberid':data.member.id,
				'status':data.status,

				'last_visited':data.last_visited,
				'next_visit_date':data.next_visit_date.split(','),
				'last_meeting_date':data.last_meeting_date,
				'next_meeting_date':data.next_meeting_date.split(','),
				'tour_from':data.tour_from,
				'tour_to':data.tour_to

				})

		print('tourdata is ',tourdata)


		return render(request,'dashboard/tourmanagement.html',{'tourdata':tourdata})





def touredit(request,pk):

	if request.method == 'GET':

		tourdata = {}

		data = TourManagement.objects.get(id=int(pk))
		tourdata={'id':data.id,
				'all_members':User.objects.filter(organization=request.user.organization),
				'assigned_members':[x.id for x in data.tour_members.all()],
				'status_list':['pending approval','approved','finished'],
				'curr_status':data.status,
				#'memberid':data.member.id,

				'last_visited':data.last_visited,
				'next_visit_date':data.next_visit_date,
				'last_meeting_date':data.last_meeting_date,
				'next_meeting_date':data.next_meeting_date,
				'tour_from':data.tour_from,
				'tour_to':data.tour_to

				}


		return render(request,'dashboard/edit-tour.html',{'tourdata':tourdata})



def edittoursubmit(request):


	if request.method == "POST":
		member_ids = request.POST.getlist('members')
		identity = request.POST['identity']
		status = request.POST['status']
		last_visited = request.POST['last_visited']
		next_visit_date = request.POST['next_visit_date']
		last_meeting_date = request.POST['last_meeting_date']
		next_meeting_date = request.POST['next_meeting_date']
		tour_from = request.POST['tour_from']
		tour_to = request.POST['tour_to']

		#sel_user = User.objects.get(id=int(member_id))

		sel_tour = TourManagement.objects.get(id=int(identity))

		sel_tour.tour_members.clear()

		sel_tour.status = status

		for ids in member_ids:
			sel_tour.tour_members.add(User.objects.get(id=int(ids)))


		if(sel_tour.last_visited != last_visited):
			sel_tour.last_visited = last_visited


		if(sel_tour.next_visit_date != next_visit_date):
			sel_tour.next_visit_date = next_visit_date

		if(sel_tour.last_meeting_date != last_meeting_date):
			sel_tour.last_meeting_date = last_meeting_date

		if(sel_tour.next_meeting_date != next_meeting_date):
			sel_tour.next_meeting_date = next_meeting_date

		if(sel_tour.tour_from != tour_from):
			sel_tour.tour_from = tour_from

		if(sel_tour.tour_to != tour_to):
			sel_tour.tour_to = tour_to


		sel_tour.save()


		
		return redirect('tourmanagement')







def delete_tour(request):

	tourid = request.POST['tourid']

	sel = TourManagement.objects.get(id=int(tourid))
	sel.delete()

	return JsonResponse({'status':'deleted'})



def upload_files(request,pk):
	if request.method == "GET":
		tour_file_data = []
		sel_tour = TourManagement.objects.get(id=int(pk))

		all_members = sel_tour.tour_members.all()

		for member in all_members:
			sel_mem = User.objects.get(id=int(member.id))
			all_uploaded_files = tour_files.objects.filter(Q(user=sel_mem) & Q(tour=sel_tour))
			tour_file_data.append({'memberid':member.id,'member':member.first_name+' '+member.last_name,'files':all_uploaded_files})



		return render(request,'dashboard/file_upload.html',{'tour_file_data':tour_file_data})


	if request.method == "POST":
		getfiles = request.FILES.getlist('file')
		

		sel_tour = TourManagement.objects.get(id=int(pk))

		for file in getfiles:
			tour_files.objects.create(user=request.user,tour=sel_tour,file=file)


		return redirect('upload_files',pk)





