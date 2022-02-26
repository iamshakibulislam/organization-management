from importlib.metadata import requires
import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib import messages
from users.models import User
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.http import Http404
from functools import wraps




def requires_tour_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_tour_perm != True and request.user.is_admin != True:   
            raise Http404
        return view(request, *args, **kwargs)
    return _view


def requires_edit_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_edit_perm != True and request.user.is_admin != True:  
            raise Http404
        return view(request, *args, **kwargs)
    return _view


def requires_delete_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_delete_perm != True and request.user.is_admin != True:  
            raise Http404
        return view(request, *args, **kwargs)
    return _view


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
		member_data = []

		for mem in members:

			role = ""

			if mem.is_admin == 1:
				role = "Administrator"
			elif mem.is_officer == 1:
				role = "Officer"

			elif mem.is_moderator == 1:
				role = "Moderator"

			
			three_months_status = False
			check_tour = len(TourManagement.objects.filter(Q(date__gte=datetime.now()-timedelta(days=92)) & Q(tour_members=mem)))

			if check_tour > 0:
				three_months_status = True


			member_data.append({'id':mem.id,'email':mem.email,
				'first_name':mem.first_name,'last_name':mem.last_name,
				'join_date':mem.join_date,'role':role,'tour_in_three_months':three_months_status,'profile_picture':mem.profile_picture.url})

		context = {
				'all_members':member_data,
				'total_members':len(members),
				'total_officers':officers_total,
				'total_moderators':moderators_total,
				'administrators_total':admin_total
				}

		return render(request,'dashboard/index.html',context)


def edit_members(request):
	if request.method == 'GET' and request.user.is_admin == True:
		userid = int(request.GET['userid'])



		sel_user = User.objects.get(id=userid)
		
		role = ''
		if sel_user.is_admin == True:
			role = 'Administrator'

		if sel_user.is_officer == True:
			role = 'Officer'

		if sel_user.is_moderator == True:
			role = 'Moderator'

		user_data={'first_name':sel_user.first_name,
		'last_name':sel_user.last_name,
		'email':sel_user.email,
		'phone':sel_user.phone,
		'role':role,
		'id':sel_user.id,
		'has_tour_perm':sel_user.has_tour_perm,
		'has_procurement_perm':sel_user.has_procurement_perm,
		'has_training_perm':sel_user.has_training_perm,
		'has_edit_perm':sel_user.has_edit_perm,
		'has_delete_perm':sel_user.has_delete_perm,
		
		}
		

		return JsonResponse({'userdata':user_data})



	if request.method == 'POST':

		first_name = request.POST['first_name_edit']
		last_name = request.POST['last_name_edit']
		email = request.POST['email_edit']
		phone = request.POST['phone_edit']
		role = request.POST['role_edit']

		userid = request.POST['userid']


		sel_user = User.objects.get(id=int(userid))


		has_tour_perm_edit = int(request.POST['has_tour_perm_edit'])
		has_procurement_perm_edit = int(request.POST['has_procurement_perm_edit'])
		has_training_perm_edit = int(request.POST['has_training_perm_edit'])
		has_edit_perm_edit = int(request.POST['has_edit_perm_edit'])
		has_delete_perm_edit = int(request.POST['has_delete_perm_edit'])


		sel_user.has_tour_perm = has_tour_perm_edit
		sel_user.has_procurement_perm = has_procurement_perm_edit
		sel_user.has_training_perm = has_training_perm_edit
		sel_user.has_edit_perm = has_edit_perm_edit
		sel_user.has_delete_perm = has_delete_perm_edit

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
			sel_user.is_admin = False


		if(role == "Moderator"):
			sel_user.is_officer = False
			sel_user.is_moderator = True
			sel_user.is_admin = False



		sel_user.save()

		return JsonResponse({'status':'updated members information'})




def delete_members(request):
	if request.method == "POST" and request.user.is_admin == True:
		userid = request.POST['userid']

		sel_user = User.objects.get(id=userid)
		sel_user.delete()

		return JsonResponse({'status':'deleted'})



@requires_tour_perm
def tour(request):
	if request.method == "GET":
		sel_org_members = User.objects.filter(organization = request.user.organization)
		all_places = tour_places.objects.filter(organization=request.user.organization)
		all_sub_sectors = sub_sectors.objects.filter(organization=request.user.organization)
		return render(request,'dashboard/tour.html',{'members':sel_org_members,'all_places':all_places,'all_sub_sectors':all_sub_sectors})


	if request.method == 'POST' :

		member_id = request.POST.getlist('member')
		
		last_visited = request.POST['last_visited']
		next_visit_date = request.POST['next_visit_date']

		try:
			last_meeting_date = request.POST['last_meeting_date']
			next_meeting_date = request.POST['next_meeting_date']
		except:
			pass

		#tour_from = request.POST['tour_from']
		tour_to = request.POST['tour_to']

		#comment = request.GET.get('comment','No Comment')
		sub_sector = request.POST.get('sub_sector',' No Sub Sector')
		#actual_visit_date = request.POST['actual_visit_date']
		#report_submission_date=request.POST['report_submission_date']

		
		creating_tour=TourManagement.objects.create(
			organization = request.user.organization,
			last_visited = last_visited,
			next_visit_date = next_visit_date,
			#actual_visit_date = actual_visit_date,
			#report_submission_date = report_submission_date,
			
			
			#comment = comment,
			sub_sector = sub_sector,
			tour_to = tour_to
			)

		for members in member_id:
			try:
				sel_mem = User.objects.get(id=int(members))
			except:
				return redirect('tour')

			creating_tour.tour_members.add(sel_mem)











		return redirect('tourmanagement')




@requires_tour_perm
def tourmanagement(request):
	if request.method == 'GET':

		from_date = ''
		to_date = ''
		userid = 0
		singleMode = False
		name =''

		
		userid = request.GET.get('user',0)
		if userid != 0:
			singleMode = True
			name = User.objects.get(id=int(userid)).first_name+' '+User.objects.get(id=int(userid)).last_name
		
		try:
			from_date = request.GET['from']
			to_date = request.GET['to']

			

		except:
			pass
		get_tour = TourManagement.objects.filter(organization = request.user.organization)

		if(request.user.is_officer == True and from_date != '' and to_date != ''):
			get_tour = TourManagement.objects.filter(Q(tour_members = request.user) & Q(date__gte=from_date) & Q(date__lte=to_date))

		elif request.user.is_officer == True and from_date=='' and to_date=='':
			get_tour = TourManagement.objects.filter(Q(tour_members = request.user))

		else:
			pass


		if request.user.is_officer != True:

			if len(from_date) != 0 and len(to_date) != 0:
				get_tour = TourManagement.objects.filter(Q(organization = request.user.organization) & Q(date__gte=from_date) & Q(date__lte=to_date) )

			if int(userid) > 0 and from_date != '' and to_date != '':
				get_tour = TourManagement.objects.filter(Q(organization = request.user.organization) & Q(date__gte=from_date) & Q(date__lte=to_date)  & Q(tour_members = User.objects.get(id=int(userid))))

			if (int(userid) > 0 and from_date =='' and to_date==''):
				get_tour = TourManagement.objects.filter(Q(organization = request.user.organization)   & Q(tour_members = User.objects.get(id=int(userid))))

		

		tourdata =  []

		for data in get_tour:
			tourdata.append({'id':data.id,
				'members':[name.first_name+' '+name.last_name for name in data.tour_members.all()],
				#'memberid':data.member.id,
				'status':data.status,

				'last_visited':data.last_visited,
				'next_visit_date':data.next_visit_date.split(','),
				'actual_visit_date':data.actual_visit_date,
				'report_submission_date':data.report_submission_date,
				
				'tour_from':data.tour_from,
				'tour_to':data.tour_to,
				'sub_sector':data.sub_sector,
				'comment':data.comment

				})

		all_places = tour_places.objects.all()
		all_sub_sectors = sub_sectors.objects.all()

		


		return render(request,'dashboard/tourmanagement.html',{'tourdata':tourdata,'singleMode':singleMode,'name':name,'identity':userid,'all_places':all_places,'all_sub_sectors':all_sub_sectors})




@requires_tour_perm
@requires_edit_perm
def touredit(request,pk):

	if request.method == 'GET':

		tourdata = {}

		all_places = tour_places.objects.filter(organization=request.user.organization)
		all_sub_sectors = sub_sectors.objects.filter(organization=request.user.organization)

		data = TourManagement.objects.get(id=int(pk))
		tourdata={'id':data.id,
				'all_members':User.objects.filter(organization=request.user.organization),
				'assigned_members':[x.id for x in data.tour_members.all()],
				'status_list':['pending approval','approved','finished'],
				'curr_status':data.status,
				'actual_visit_date':data.actual_visit_date,
				'report_submission_date':data.report_submission_date,
				#'memberid':data.member.id,

				'last_visited':data.last_visited,
				'next_visit_date':data.next_visit_date,
				
				'tour_from':data.tour_from,
				'tour_to':data.tour_to,
				'sub_sector':data.sub_sector,
				'comment':data.comment

				}

		

		return render(request,'dashboard/edit-tour.html',{'tourdata':tourdata,'all_places':all_places,'all_sub_sectors':all_sub_sectors})


@requires_tour_perm
@requires_edit_perm
def edittoursubmit(request):


	if request.method == "POST":
		member_ids = request.POST.getlist('members')
		identity = request.POST['identity']
		status = request.POST['status']
		last_visited = request.POST['last_visited']
		next_visit_date = request.POST['next_visit_date']

		sub_sector = request.POST['sub_sector']
		comment = request.POST['comment']
		
		#tour_from = request.POST['tour_from']
		tour_to = request.POST['tour_to']

		actual_visit_date = request.POST['actual_visit_date']
		report_submission_date = request.POST['report_submission_date']

		#sel_user = User.objects.get(id=int(member_id))

		logs_data = ""

		sel_tour = TourManagement.objects.get(id=int(identity))

		sel_tour.tour_members.clear()

		if sel_tour.status != status:
			logs_data=logs_data + ','+'Status changed from '+sel_tour.status+' to '+status
			sel_tour.status = status

		for ids in member_ids:
			sel_tour.tour_members.add(User.objects.get(id=int(ids)))

		if sel_tour.actual_visit_date != actual_visit_date:
			logs_data = logs_data + ','+'Changed Actual visit date from '+str(sel_tour.actual_visit_date)+' to '+actual_visit_date

			sel_tour.actual_visit_date = actual_visit_date

		if sel_tour.report_submission_date != report_submission_date:
			logs_data = logs_data + ','+'Changed report submission date from '+str(sel_tour.report_submission_date)+' to '+report_submission_date
			sel_tour.report_submission_date = report_submission_date

		if(sel_tour.last_visited != last_visited):
			logs_data = logs_data + ','+'Changed Last visit date from '+str(sel_tour.last_visited)+' to '+last_visited
			sel_tour.last_visited = last_visited


		if(sel_tour.next_visit_date != next_visit_date):
			logs_data = logs_data + ','+'Changed Proposed visit date from '+sel_tour.next_visit_date+' to '+next_visit_date
			sel_tour.next_visit_date = next_visit_date

		

		#if(sel_tour.tour_from != tour_from):
			#sel_tour.tour_from = tour_from

		if(sel_tour.tour_to != tour_to):
			logs_data = logs_data + ','+'Changed tour destination from '+sel_tour.tour_to+' to '+tour_to
			sel_tour.tour_to = tour_to


		if(sel_tour.sub_sector != sub_sector):
			logs_data = logs_data + ','+'Changed Sub-Sector from '+sel_tour.sub_sector+' to '+sub_sector
			sel_tour.sub_sector = sub_sector

		if(sel_tour.comment != comment):
			logs_data = logs_data + ','+'Changed tour comment from '+str(sel_tour.comment)+' to '+comment
			sel_tour.comment = comment


		sel_tour.save()

		if logs_data != "":
			logs.objects.create(user=request.user,tour=sel_tour,action=logs_data[1:])


		
		return redirect('tourmanagement')






@requires_tour_perm
@requires_delete_perm
def delete_tour(request):

	tourid = request.POST['tourid']

	sel = TourManagement.objects.get(id=int(tourid))
	sel.delete()

	return JsonResponse({'status':'deleted'})


@requires_tour_perm
@requires_edit_perm
def upload_files(request,pk):
	if request.method == "GET":
		


		return render(request,'dashboard/file_upload.html',{'tourid':int(pk)})


	if request.method == "POST":
		getfiles = request.FILES.getlist('file')
		

		sel_tour = TourManagement.objects.get(id=int(pk))

		for file in getfiles:
			tour_files.objects.create(user=request.user,tour=sel_tour,file=file)

		total_member_for_this_tour = len(sel_tour.tour_members.all())

		unique_files_per_user = len(list(set([userid.user.id for userid in tour_files.objects.filter(tour=sel_tour)])))

		if total_member_for_this_tour == unique_files_per_user:
			sel_tour.status = "finished"

			sel_tour.save()


		return redirect('show_files',pk)




@requires_tour_perm
def show_files(request,pk):
	if request.method == "GET":
		tour_file_data = []
		sel_tour = TourManagement.objects.get(id=int(pk))

		all_members = sel_tour.tour_members.all()

		for member in all_members:
			sel_mem = User.objects.get(id=int(member.id))
			all_uploaded_files = tour_files.objects.filter(Q(user=sel_mem) & Q(tour=sel_tour))
			tour_file_data.append({'memberid':member.id,'member':member.first_name+' '+member.last_name,'files':all_uploaded_files})



		return render(request,'dashboard/file_show.html',{'tour_file_data':tour_file_data})



@login_required(login_url = '/users/login/')
def add_tour_place(request):
	if request.method == "GET":
		return render(request,'dashboard/add_tour_places.html')


	if request.method == "POST":
		place_name = request.POST['place']
		

		tour_places.objects.create(place_name=place_name,organization=request.user.organization)

		messages.info(request,'Tour place added successfully')

		return redirect('add_tour_place')



@login_required(login_url = '/users/login/')
def add_sub_sector(request):
	if request.method == "GET":
		return render(request,'dashboard/add-sub-sector.html')


	if request.method == "POST":
		sector_name = request.POST['sector_name']
		

		sub_sectors.objects.create(sector_name=sector_name,organization=request.user.organization)

		messages.info(request,'Sub Sector added successfully')

		return redirect('add_sub_sector')


@login_required(login_url = '/users/login/')
def get_logs(request,pk):
	if request.method == "GET":
		sel_tour = TourManagement.objects.get(id=int(pk))
		sel_log = logs.objects.filter(tour=sel_tour)

		log_data = []

		for data in sel_log:
			action = []
			act = data.action.split(',')
			for change in act:
				action.append(change)
			log_data.append({'user':data.user.first_name+' '+data.user.last_name,'date':data.date,'action':action})
			

		return render(request,'dashboard/logs.html',{'logdata':log_data})



