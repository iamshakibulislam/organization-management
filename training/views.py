from email import message
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .models import category as cats
from django.db.models import Q
from django.http import Http404
from functools import wraps

def requires_training_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_training_perm != True and request.user.is_admin != True:   
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



@requires_training_perm
def add_training(request):
    if request.method == "GET":
        cat = cats.objects.filter(organization=request.user.organization)
        return render(request, 'training/add_training.html',{'categories':cat})

    if request.method == "POST":
        po_name = request.POST.get('po_name')
        sub_sector = request.POST.get('sub_sector')
        budget_head = request.POST.get('budget_head')
        sub_budget_head1 = request.POST.get('sub_budget_head1')
        training_title = request.POST.get('training_title')
        training_topic = request.POST.get('training_topic')
        try:
            category = cats.objects.get(id=int(request.POST.get('category')))
        except:
            pass
        budget = request.POST.get('budget')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        duration = request.POST.get('duration')
        batch = request.POST.get('batch')
        total_session_conducted = request.POST.get('total_session_conducted')
        no_of_facilitator_official = request.POST.get('no_of_facilitator_official')
        no_of_facilitator_private = request.POST.get('no_of_facilitator_private')
        no_of_facilitator_internal = request.POST.get('no_of_facilitator_internal')

        information_of_facilitator_official_name = request.POST.get('information_of_facilitator_official_name')
        information_of_facilitator_official_designation = request.POST.get('information_of_facilitator_official_designation')
        information_of_facilitator_official_organization = request.POST.get('information_of_facilitator_official_organization')
        information_of_facilitator_official_contact = request.POST.get('information_of_facilitator_official_contact')

        information_of_facilitator_private_name = request.POST.get('information_of_facilitator_private_name')
        information_of_facilitator_private_designation = request.POST.get('information_of_facilitator_private_designation')
        information_of_facilitator_private_organization = request.POST.get('information_of_facilitator_private_organization')
        information_of_facilitator_private_contact = request.POST.get('information_of_facilitator_private_contact')

        information_of_facilitator_internal_name = request.POST.get('information_of_facilitator_internal_name')
        information_of_facilitator_internal_designation = request.POST.get('information_of_facilitator_internal_designation')
        information_of_facilitator_internal_organization = request.POST.get('information_of_facilitator_internal_organization')
        information_of_facilitator_internal_contact = request.POST.get('information_of_facilitator_internal_contact')
        total_number_of_trainer = request.POST.get('total_number_of_trainer')
        
        po_male_perticipent = request.POST.get('po_male_perticipent')
        po_female_perticipent = request.POST.get('po_female_perticipent')

        po_total_perticipent = request.POST.get('po_total_perticipent')

        me_male_perticipent = request.POST.get('me_male_perticipent')
        me_female_perticipent = request.POST.get('me_female_perticipent')
        me_total_perticipent = request.POST.get('me_total_perticipent')

        other_male_perticipent = request.POST.get('other_male_perticipent')
        other_female_perticipent = request.POST.get('other_female_perticipent')
        other_total_perticipent = request.POST.get('other_total_perticipent')

        total_perticipent = request.POST.get('total_perticipent')

        training.objects.create(
            user = request.user,
            organization=request.user.organization,
            po_name = po_name,
            sub_sector = sub_sector,
            budget_head = budget_head,
            sub_budget_head1 = sub_budget_head1,
            training_title = training_title,
            training_topic = training_topic,
            category = category,
            budget = budget,
            cost = cost,
            date = date,
            duration = duration,
            batch = batch,
            total_session_conducted = total_session_conducted,
            no_of_facilitator_official = no_of_facilitator_official,
            no_of_facilitator_private = no_of_facilitator_private,
            no_of_facilitator_internal = no_of_facilitator_internal,
            information_of_facilitator_official_name = information_of_facilitator_official_name,
            information_of_facilitator_official_designation = information_of_facilitator_official_designation,
            information_of_facilitator_official_organization = information_of_facilitator_official_organization,
            information_of_facilitator_official_contact = information_of_facilitator_official_contact,

            information_of_facilitator_private_name = information_of_facilitator_private_name,
            information_of_facilitator_private_designation = information_of_facilitator_private_designation,
            information_of_facilitator_private_organization = information_of_facilitator_private_organization,
            information_of_facilitator_private_contact = information_of_facilitator_private_contact,

            information_of_facilitator_internal_name = information_of_facilitator_internal_name,
            information_of_facilitator_internal_designation = information_of_facilitator_internal_designation,
            information_of_facilitator_internal_organization = information_of_facilitator_internal_organization,
            information_of_facilitator_internal_contact = information_of_facilitator_internal_contact,

            total_number_of_trainer = total_number_of_trainer,
            po_male_perticipent = po_male_perticipent,
            po_female_perticipent = po_female_perticipent,
            po_total_perticipent = po_total_perticipent,
            me_male_perticipent = me_male_perticipent,
            me_female_perticipent = me_female_perticipent,
            me_total_perticipent = me_total_perticipent,
            other_female_perticipent = other_female_perticipent,
            other_male_perticipent = other_male_perticipent,
            other_total_perticipent = other_total_perticipent,
            total_perticipent = total_perticipent
            )


        return redirect('training_list')





@requires_training_perm
def training_list(request):
    if request.method == 'GET':
        training_list = training.objects.filter(organization=request.user.organization) 

        if request.user.is_officer == True:
            training_list = training.objects.filter(Q(organization=request.user.organization) & Q(user=request.user))
       
        return render(request, 'training/training_list.html', {'training_list':training_list})

@requires_training_perm
@requires_edit_perm
def training_edit(request,pk):
    if request.method == 'GET':
        sel_cat = cats.objects.filter(organization=request.user.organization)
        training_details = training.objects.get(id=pk)
        return render(request, 'training/training_edit.html', {'cont':training_details,'categories':sel_cat})

    if request.method == 'POST':
        po_name = request.POST.get('po_name')
        sub_sector = request.POST.get('sub_sector')
        budget_head = request.POST.get('budget_head')
        sub_budget_head1 = request.POST.get('sub_budget_head1')
        training_title = request.POST.get('training_title')
        training_topic = request.POST.get('training_topic')
        
        category = request.POST.get('category')
        print('category is ',category)
        cat_inst = cats.objects.get(id=int(category))

        print('instance ',cat_inst)
        
        budget = request.POST.get('budget')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        duration = request.POST.get('duration')
        batch = request.POST.get('batch')
        total_session_conducted = request.POST.get('total_session_conducted')
        no_of_facilitator_official = request.POST.get('no_of_facilitator_official')
        no_of_facilitator_private = request.POST.get('no_of_facilitator_private')
        no_of_facilitator_internal = request.POST.get('no_of_facilitator_internal')

        information_of_facilitator_official_name = request.POST.get('information_of_facilitator_official_name')
        information_of_facilitator_official_designation = request.POST.get('information_of_facilitator_official_designation')
        information_of_facilitator_official_organization = request.POST.get('information_of_facilitator_official_organization')
        information_of_facilitator_official_contact = request.POST.get('information_of_facilitator_official_contact')

        information_of_facilitator_private_name = request.POST.get('information_of_facilitator_private_name')
        information_of_facilitator_private_designation = request.POST.get('information_of_facilitator_private_designation')
        information_of_facilitator_private_organization = request.POST.get('information_of_facilitator_private_organization')
        information_of_facilitator_private_contact = request.POST.get('information_of_facilitator_private_contact')

        information_of_facilitator_internal_name = request.POST.get('information_of_facilitator_internal_name')
        information_of_facilitator_internal_designation = request.POST.get('information_of_facilitator_internal_designation')
        information_of_facilitator_internal_organization = request.POST.get('information_of_facilitator_internal_organization')
        information_of_facilitator_internal_contact = request.POST.get('information_of_facilitator_internal_contact')
        total_number_of_trainer = request.POST.get('total_number_of_trainer')
        
        po_male_perticipent = request.POST.get('po_male_perticipent')
        po_female_perticipent = request.POST.get('po_female_perticipent')

        po_total_perticipent = request.POST.get('po_total_perticipent')

        me_male_perticipent = request.POST.get('me_male_perticipent')
        me_female_perticipent = request.POST.get('me_female_perticipent')
        me_total_perticipent = request.POST.get('me_total_perticipent')

        other_male_perticipent = request.POST.get('other_male_perticipent')
        other_female_perticipent = request.POST.get('other_female_perticipent')
        other_total_perticipent = request.POST.get('other_total_perticipent')

        total_perticipent = request.POST.get('total_perticipent')

        sel_training = training.objects.get(id=int(pk))
        
        
        
        sel_training.po_name=po_name
        sel_training.sub_sector=sub_sector
        sel_training.budget_head=budget_head
        sel_training.sub_budget_head1=sub_budget_head1
        sel_training.training_title=training_title
        sel_training.training_topic=training_topic
        sel_training.category=cat_inst
        sel_training.budget=budget
        sel_training.cost=cost
        sel_training.date=date
        sel_training.duration=duration
        sel_training.batch=batch
        sel_training.total_session_conducted=total_session_conducted
        sel_training.no_of_facilitator_official=no_of_facilitator_official
        sel_training.no_of_facilitator_private=no_of_facilitator_private
        sel_training.no_of_facilitator_internal=no_of_facilitator_internal
        sel_training.information_of_facilitator_official_name=information_of_facilitator_official_name
        sel_training.information_of_facilitator_official_designation=information_of_facilitator_official_designation
        sel_training.information_of_facilitator_official_organization=information_of_facilitator_official_organization
        sel_training.information_of_facilitator_official_contact=information_of_facilitator_official_contact
       
        sel_training.information_of_facilitator_private_name=information_of_facilitator_private_name
        sel_training.information_of_facilitator_private_designation=information_of_facilitator_private_designation
        sel_training.information_of_facilitator_private_organization=information_of_facilitator_private_organization
        sel_training.information_of_facilitator_private_contact=information_of_facilitator_private_contact
       
        sel_training.information_of_facilitator_internal_name=information_of_facilitator_internal_name
        sel_training.information_of_facilitator_internal_designation=information_of_facilitator_internal_designation
        sel_training.information_of_facilitator_internal_organization=information_of_facilitator_internal_organization
        sel_training.information_of_facilitator_internal_contact=information_of_facilitator_internal_contact
        
        sel_training.total_number_of_trainer=total_number_of_trainer
        sel_training.po_male_perticipent=po_male_perticipent
        sel_training.po_female_perticipent=po_female_perticipent
        sel_training.po_total_perticipent=po_total_perticipent
        sel_training.me_male_perticipent=me_male_perticipent
        sel_training.me_female_perticipent=me_female_perticipent
        sel_training.me_total_perticipent=me_total_perticipent
        sel_training.other_female_perticipent=other_female_perticipent
        sel_training.other_male_perticipent=other_male_perticipent
        sel_training.other_total_perticipent=other_total_perticipent
        sel_training.total_perticipent=total_perticipent

        sel_training.save()
            

        
        return redirect(training_list)






def add_training_category(request):
    if request.method == 'GET':
        return render(request, 'training/add_training_category.html')
    if request.method == "POST":
        get_cat = request.POST.get('category')

        category.objects.create(name=get_cat,organization=request.user.organization)
        messages.success(request, 'Category Added Successfully')
        return redirect('add_training_category')

@requires_training_perm
def training_details(request,pk):
    if request.method == 'GET':
        sel_training = training.objects.get(id=int(pk))
        return render(request, 'training/training_details.html',{'procurement_data':sel_training})

@requires_training_perm
@requires_delete_perm
def training_delete(request):
    if request.method == "POST":
        get_id = request.POST.get('procurement_id')
        sel_training = training.objects.get(id=int(get_id))
        sel_training.delete()
        return JsonResponse({'status':'deleted'})