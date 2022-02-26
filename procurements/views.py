from importlib.metadata import requires
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q,Sum,Avg

from datetime import datetime
from .models import *
from django.http import Http404
from functools import wraps



def requires_procurement_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_procurement_perm == False and request.user.is_admin == False:   
            raise Http404
        return view(request, *args, **kwargs)
    return _view


def requires_edit_perm(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.user.has_edit_perm == False and request.user.is_admin == False:  
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

# create a django view

@requires_procurement_perm
def main_page(request):
    all_procurments_for_goods = procurement_plan_for_goods.objects.filter(organization=request.user.organization)

    if request.user.is_officer == True:
        all_procurments_for_goods = procurement_plan_for_goods.objects.filter(Q(user=request.user) & Q(organization=request.user.organization))
    return render(request, 'dashboard/index.html', {'all_procurments_for_goods': all_procurments_for_goods})

@requires_procurement_perm
def add_procurements_for_goods(request):

    if request.method == "GET":
        

        return render(request, 'procurements/add_procurement_for_goods.html')

    if request.method == "POST":
        contract_package_number=request.POST.get('contract_package_number')
        
        contract_description=request.POST.get('contract_description')
        unit=request.POST.get('unit')
        quantity=request.POST.get('quantity')
        estimated_price=request.POST.get('estimated_price')
        actual_contract_amount=request.POST.get('actual_contract_amount')
        procedure_method=request.POST.get('procedure_method')
        procurement_guidelines=request.POST.get('procurement_guidelines')
        prior_review=request.POST.get('prior_review')
        contract_approving_authority=request.POST.get('contract_approving_authority')
        planned_date_of_ifb_publication=request.POST.get('planned_date_of_ifb_publication')
        actual_date_of_ifb_publication=request.POST.get('actual_date_of_ifb_publication')
        planned_date_of_bid_opening=request.POST.get('planned_date_of_bid_opening')
        actual_date_of_bid_opening=request.POST.get('actual_date_of_bid_opening')
        planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        supplier_name=request.POST.get('supplier_name')
        remarks=request.POST.get('remarks')

        procurement_plan_for_goods_instance=procurement_plan_for_goods(user=request.user,organization=request.user.organization,contract_package_number=contract_package_number,contract_description=contract_description,unit=unit,quantity=quantity,estimated_price=estimated_price,actual_contract_amount=actual_contract_amount,procedure_method=procedure_method,procurement_guidelines=procurement_guidelines,prior_review=prior_review,contract_approving_authority=contract_approving_authority,planned_date_of_ifb_publication=planned_date_of_ifb_publication,actual_date_of_ifb_publication=actual_date_of_ifb_publication,planned_date_of_bid_opening=planned_date_of_bid_opening,actual_date_of_bid_opening=actual_date_of_bid_opening,planned_date_of_contract_singning=planned_date_of_contract_singning,actual_date_of_contract_signing=actual_date_of_contract_signing,planned_date_of_delivery=planned_date_of_delivery,actual_date_of_delivery=actual_date_of_delivery,supplier_name=supplier_name,remarks=remarks)
        procurement_plan_for_goods_instance.save()
        return redirect('main_procurement_page')


@requires_procurement_perm
def procurement_details(request,pk):
    procurement_plan_for_goods_instance=procurement_plan_for_goods.objects.get(pk=pk)
    return render(request, 'procurements/procurement-details.html', {'procurement_data': procurement_plan_for_goods_instance})


@requires_procurement_perm
@requires_edit_perm
def update_procurements_for_goods(request,pk):
    if request.method == "GET":
        sel_proc = procurement_plan_for_goods.objects.get(pk=pk)
        return render(request, 'procurements/edit_procurement_for_goods.html', {'procurement_data': sel_proc})

    if request.method == "POST":
        procurement_plan_for_goods_instance=procurement_plan_for_goods.objects.get(pk=pk)
        
        procurement_plan_for_goods_instance.contract_package_number=request.POST.get('contract_package_number')
        procurement_plan_for_goods_instance.contract_description=request.POST.get('contract_description')
        procurement_plan_for_goods_instance.unit=request.POST.get('unit')
        procurement_plan_for_goods_instance.quantity=request.POST.get('quantity')
        procurement_plan_for_goods_instance.estimated_price=request.POST.get('estimated_price')
        procurement_plan_for_goods_instance.actual_contract_amount=request.POST.get('actual_contract_amount')
        procurement_plan_for_goods_instance.procedure_method=request.POST.get('procedure_method')
        procurement_plan_for_goods_instance.procurement_guidelines=request.POST.get('procurement_guidelines')
        procurement_plan_for_goods_instance.prior_review=request.POST.get('prior_review')
        procurement_plan_for_goods_instance.contract_approving_authority=request.POST.get('contract_approving_authority')
        procurement_plan_for_goods_instance.planned_date_of_ifb_publication=request.POST.get('planned_date_of_ifb_publication')
        procurement_plan_for_goods_instance.actual_date_of_ifb_publication=request.POST.get('actual_date_of_ifb_publication')
        procurement_plan_for_goods_instance.planned_date_of_bid_opening=request.POST.get('planned_date_of_bid_opening')
        procurement_plan_for_goods_instance.actual_date_of_bid_opening=request.POST.get('actual_date_of_bid_opening')
        procurement_plan_for_goods_instance.planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        procurement_plan_for_goods_instance.actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        procurement_plan_for_goods_instance.planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        procurement_plan_for_goods_instance.actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        procurement_plan_for_goods_instance.supplier_name=request.POST.get('supplier_name')
        procurement_plan_for_goods_instance.remarks=request.POST.get('remarks')
        procurement_plan_for_goods_instance.save()

        return redirect('main_procurement_page')

@requires_procurement_perm
@requires_delete_perm
def delete_procurements_for_goods(request):
    if request.user.is_admin == True and request.method == "POST":
        getid = request.POST['procurementid']
        procurement_plan_for_goods_instance=procurement_plan_for_goods.objects.get(id=int(getid))
        procurement_plan_for_goods_instance.delete()
        return JsonResponse({'status': 'deleted'})

@requires_procurement_perm
def summery_for_goods(request):
    if request.method == "GET":
        fromdate = request.GET.get('fromdate', datetime.today().strftime("%Y-%m-%d"))
        todate=request.GET.get('todate', datetime.today().strftime("%Y-%m-%d"))

        if fromdate == '':

            fromdate = datetime.today().strftime("%Y-%m-%d")
        
        if todate == '':
            todate = datetime.today().strftime("%Y-%m-%d")
        print('from',fromdate,todate)


        total_package = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)))
        total_otm = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')))
        total_rfq = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')))
        total_estimated_values = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(testimated=Sum('estimated_price'))['testimated']
        total_otm_estimated_values = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')).aggregate(otmtestimated=Sum('estimated_price'))['otmtestimated']
        total_rfq_estimated_values = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')).aggregate(rfqtestimated=Sum('estimated_price'))['rfqtestimated']

        contract_awarded_total = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_otm_total = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM') & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_rfq_total = len(procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ') & ~Q(actual_date_of_contract_signing=None)))

        contract_actual_total_value = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(tvalue=Sum('actual_contract_amount'))['tvalue']
        contract_otm_actual_total_value = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')).aggregate(otmvalue=Sum('actual_contract_amount'))['otmvalue']
        contract_rfq_actual_total_value = procurement_plan_for_goods.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')).aggregate(rfqvalue=Sum('actual_contract_amount'))['rfqvalue']

        datas = {'fromdate':fromdate,'todate':todate,
                'total_package':total_package,
                'total_otm':total_otm,
                'total_rfq':total_rfq,
                'total_estimated_values':total_estimated_values,
                'total_otm_estimated_values':total_otm_estimated_values,
                'total_rfq_estimated_values':total_rfq_estimated_values,
                'contract_awarded_total':contract_awarded_total,
                'contract_awarded_otm_total':contract_awarded_otm_total,
                'contract_awarded_rfq_total':contract_awarded_rfq_total,
                'contract_actual_total_value':contract_actual_total_value,
                'contract_otm_actual_total_value':contract_otm_actual_total_value,
                'contract_rfq_actual_total_value':contract_rfq_actual_total_value,

        }
        return render(request, 'procurements/procurement_for_goods_summery.html', datas)


@requires_procurement_perm
def add_procurements_for_services(request):
    if request.method == "GET":
        

        return render(request, 'procurements/add_procurement_for_services.html')

    if request.method == "POST":
        contract_package_number=request.POST.get('contract_package_number')
        
        contract_description=request.POST.get('contract_description')
        unit=request.POST.get('unit')
        quantity=request.POST.get('quantity')
        estimated_price=request.POST.get('estimated_price')
        actual_contract_amount=request.POST.get('actual_contract_amount')
        procedure_method=request.POST.get('procedure_method')
        procurement_guidelines=request.POST.get('procurement_guidelines')
        prior_review=request.POST.get('prior_review')
        contract_approving_authority=request.POST.get('contract_approving_authority')
        planned_date_of_eoi_publication=request.POST.get('planned_date_of_eoi_publication')
        actual_date_of_eoi_publication=request.POST.get('actual_date_of_eoi_publication')
        planned_date_of_eoi_opening=request.POST.get('planned_date_of_eoi_opening')
        actual_date_of_eoi_opening=request.POST.get('actual_date_of_eoi_opening')
        planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        consultant_name=request.POST.get('consultant_name')
        remarks=request.POST.get('remarks')

        procurement_plan_for_services_instance=procurement_plan_for_services(user=request.user,organization=request.user.organization,contract_package_number=contract_package_number,contract_description=contract_description,unit=unit,quantity=quantity,estimated_price=estimated_price,actual_contract_amount=actual_contract_amount,procedure_method=procedure_method,procurement_guidelines=procurement_guidelines,prior_review=prior_review,contract_approving_authority=contract_approving_authority,planned_date_of_eoi_publication=planned_date_of_eoi_publication,actual_date_of_eoi_publication=actual_date_of_eoi_publication,planned_date_of_eoi_opening=planned_date_of_eoi_opening,actual_date_of_eoi_opening=actual_date_of_eoi_opening,planned_date_of_contract_singning=planned_date_of_contract_singning,actual_date_of_contract_signing=actual_date_of_contract_signing,planned_date_of_delivery=planned_date_of_delivery,actual_date_of_delivery=actual_date_of_delivery,consultant_name=consultant_name,remarks=remarks)
        procurement_plan_for_services_instance.save()
        return redirect('procurement_list_for_services')

    


@requires_procurement_perm
def procurement_list_for_services(request):
    if request.method == "GET":
        all_procurments_for_services = procurement_plan_for_services.objects.filter(organization=request.user.organization)
        if request.user.is_officer == True:
            all_procurments_for_services = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(user=request.user))
        return render(request, 'procurements/procurement_list_for_services.html',{'all_procurments_for_services':all_procurments_for_services})



@requires_procurement_perm
@requires_edit_perm
def update_procurements_for_services(request,pk):
    if request.method == "GET":
        procurement_id = int(pk)
        procurement_instance = procurement_plan_for_services.objects.get(id=procurement_id)
        return render(request, 'procurements/edit_procurement_for_service.html',{'procurement_data':procurement_instance})
    
    if request.method == "POST":

        procurement_plan_for_goods_instance=procurement_plan_for_services.objects.get(pk=pk)
        
        procurement_plan_for_goods_instance.contract_package_number=request.POST.get('contract_package_number')
        procurement_plan_for_goods_instance.contract_description=request.POST.get('contract_description')
        procurement_plan_for_goods_instance.unit=request.POST.get('unit')
        procurement_plan_for_goods_instance.quantity=request.POST.get('quantity')
        procurement_plan_for_goods_instance.estimated_price=request.POST.get('estimated_price')
        procurement_plan_for_goods_instance.actual_contract_amount=request.POST.get('actual_contract_amount')
        procurement_plan_for_goods_instance.procedure_method=request.POST.get('procedure_method')
        procurement_plan_for_goods_instance.procurement_guidelines=request.POST.get('procurement_guidelines')
        procurement_plan_for_goods_instance.prior_review=request.POST.get('prior_review')
        procurement_plan_for_goods_instance.contract_approving_authority=request.POST.get('contract_approving_authority')
        procurement_plan_for_goods_instance.planned_date_of_ifb_publication=request.POST.get('planned_date_of_eoi_publication')
        procurement_plan_for_goods_instance.actual_date_of_ifb_publication=request.POST.get('actual_date_of_eoi_publication')
        procurement_plan_for_goods_instance.planned_date_of_bid_opening=request.POST.get('planned_date_of_eoi_opening')
        procurement_plan_for_goods_instance.actual_date_of_bid_opening=request.POST.get('actual_date_of_eoi_opening')
        procurement_plan_for_goods_instance.planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        procurement_plan_for_goods_instance.actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        procurement_plan_for_goods_instance.planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        procurement_plan_for_goods_instance.actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        procurement_plan_for_goods_instance.supplier_name=request.POST.get('consultant_name')
        procurement_plan_for_goods_instance.remarks=request.POST.get('remarks')
        procurement_plan_for_goods_instance.save()


        return redirect('procurement_list_for_services')


@requires_procurement_perm
def procurement_details_for_services(request,pk):
    procurement_plan_for_services_instance=procurement_plan_for_services.objects.get(pk=pk)
    return render(request, 'procurements/procurement_details_for_services.html', {'procurement_data': procurement_plan_for_services_instance})



@requires_procurement_perm
@requires_delete_perm
def delete_procurements_for_service(request):
    if request.user.is_admin == True and request.method == "POST":
        getid = request.POST['procurementid']
        procurement_plan_for_service_instance=procurement_plan_for_services.objects.get(id=int(getid))
        procurement_plan_for_service_instance.delete()
        return JsonResponse({'status': 'deleted'})

@requires_procurement_perm
def summery_for_services(request):
    if request.method == "GET":
        fromdate = request.GET.get('fromdate', datetime.today().strftime("%Y-%m-%d"))
        todate=request.GET.get('todate', datetime.today().strftime("%Y-%m-%d"))

        if fromdate == '':

            fromdate = datetime.today().strftime("%Y-%m-%d")
        
        if todate == '':
            todate = datetime.today().strftime("%Y-%m-%d")

        


        total_package = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)))
        total_ics = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='ICS')))
        total_cqs = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='CQS')))
        total_estimated_values = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(testimated=Sum('estimated_price'))['testimated']
        total_ics_estimated_values = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='ICS')).aggregate(otmtestimated=Sum('estimated_price'))['otmtestimated']
        total_cqs_estimated_values = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='CQS')).aggregate(rfqtestimated=Sum('estimated_price'))['rfqtestimated']

        contract_awarded_total = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_ics_total = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='ICS') & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_cqs_total = len(procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='CQS') & ~Q(actual_date_of_contract_signing=None)))

        contract_actual_total_value = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(tvalue=Sum('actual_contract_amount'))['tvalue']
        contract_ics_actual_total_value = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='ICS')).aggregate(otmvalue=Sum('actual_contract_amount'))['otmvalue']
        contract_cqs_actual_total_value = procurement_plan_for_services.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='CQS')).aggregate(rfqvalue=Sum('actual_contract_amount'))['rfqvalue']

        datas = {'fromdate':fromdate,'todate':todate,
                'total_package':total_package,
                'total_ics':total_ics,
                'total_cqs':total_cqs,
                'total_estimated_values':total_estimated_values,
                'total_ics_estimated_values':total_ics_estimated_values,
                'total_cqs_estimated_values':total_cqs_estimated_values,
                'contract_awarded_total':contract_awarded_total,
                'contract_awarded_ics_total':contract_awarded_ics_total,
                'contract_awarded_cqs_total':contract_awarded_cqs_total,
                'contract_actual_total_value':contract_actual_total_value,
                'contract_ics_actual_total_value':contract_ics_actual_total_value,
                'contract_cqs_actual_total_value':contract_cqs_actual_total_value,

        }
        return render(request, 'procurements/procurement_for_services_summery.html', datas)



def add_procurements_for_work(request):

    if request.method == "GET":
        

        return render(request, 'procurements/add_procurement_for_work.html')

    if request.method == "POST":
        contract_package_number=request.POST.get('contract_package_number')
        
        contract_description=request.POST.get('contract_description')
        unit=request.POST.get('unit')
        quantity=request.POST.get('quantity')
        estimated_price=request.POST.get('estimated_price')
        actual_contract_amount=request.POST.get('actual_contract_amount')
        procedure_method=request.POST.get('procedure_method')
        procurement_guidelines=request.POST.get('procurement_guidelines')
        prior_review=request.POST.get('prior_review')
        contract_approving_authority=request.POST.get('contract_approving_authority')
        planned_date_of_ifb_publication=request.POST.get('planned_date_of_ifb_publication')
        actual_date_of_ifb_publication=request.POST.get('actual_date_of_ifb_publication')
        planned_date_of_bid_opening=request.POST.get('planned_date_of_bid_opening')
        actual_date_of_bid_opening=request.POST.get('actual_date_of_bid_opening')
        planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        supplier_name=request.POST.get('supplier_name')
        remarks=request.POST.get('remarks')

        procurement_plan_for_work_instance=procurement_plan_for_work(user=request.user,organization=request.user.organization,contract_package_number=contract_package_number,contract_description=contract_description,unit=unit,quantity=quantity,estimated_price=estimated_price,actual_contract_amount=actual_contract_amount,procedure_method=procedure_method,procurement_guidelines=procurement_guidelines,prior_review=prior_review,contract_approving_authority=contract_approving_authority,planned_date_of_ifb_publication=planned_date_of_ifb_publication,actual_date_of_ifb_publication=actual_date_of_ifb_publication,planned_date_of_bid_opening=planned_date_of_bid_opening,actual_date_of_bid_opening=actual_date_of_bid_opening,planned_date_of_contract_singning=planned_date_of_contract_singning,actual_date_of_contract_signing=actual_date_of_contract_signing,planned_date_of_delivery=planned_date_of_delivery,actual_date_of_delivery=actual_date_of_delivery,supplier_name=supplier_name,remarks=remarks)
        procurement_plan_for_work_instance.save()
        return redirect('procurement_list_for_work')

@requires_procurement_perm
def procurement_list_for_work(request):
     if request.method == "GET":
        all_procurments_for_work = procurement_plan_for_work.objects.filter(organization=request.user.organization)
        if request.user.is_officer == True:
            all_procurments_for_work = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(user=request.user))
        return render(request, 'procurements/procurement_list_for_work.html',{'all_procurments_for_work':all_procurments_for_work})



@requires_procurement_perm
@requires_edit_perm
def update_procurements_for_work(request,pk):
    if request.method == "GET":
        sel_proc = procurement_plan_for_work.objects.get(pk=int(pk))
        return render(request, 'procurements/edit_procurement_for_work.html', {'procurement_data': sel_proc})

    if request.method == "POST":
        procurement_plan_for_work_instance=procurement_plan_for_work.objects.get(pk=pk)
        
        procurement_plan_for_work_instance.contract_package_number=request.POST.get('contract_package_number')
        procurement_plan_for_work_instance.contract_description=request.POST.get('contract_description')
        procurement_plan_for_work_instance.unit=request.POST.get('unit')
        procurement_plan_for_work_instance.quantity=request.POST.get('quantity')
        procurement_plan_for_work_instance.estimated_price=request.POST.get('estimated_price')
        procurement_plan_for_work_instance.actual_contract_amount=request.POST.get('actual_contract_amount')
        procurement_plan_for_work_instance.procedure_method=request.POST.get('procedure_method')
        procurement_plan_for_work_instance.procurement_guidelines=request.POST.get('procurement_guidelines')
        procurement_plan_for_work_instance.prior_review=request.POST.get('prior_review')
        procurement_plan_for_work_instance.contract_approving_authority=request.POST.get('contract_approving_authority')
        procurement_plan_for_work_instance.planned_date_of_ifb_publication=request.POST.get('planned_date_of_ifb_publication')
        procurement_plan_for_work_instance.actual_date_of_ifb_publication=request.POST.get('actual_date_of_ifb_publication')
        procurement_plan_for_work_instance.planned_date_of_bid_opening=request.POST.get('planned_date_of_bid_opening')
        procurement_plan_for_work_instance.actual_date_of_bid_opening=request.POST.get('actual_date_of_bid_opening')
        procurement_plan_for_work_instance.planned_date_of_contract_singning=request.POST.get('planned_date_of_contract_singning')
        procurement_plan_for_work_instance.actual_date_of_contract_signing=request.POST.get('actual_date_of_contract_signing')
        procurement_plan_for_work_instance.planned_date_of_delivery=request.POST.get('planned_date_of_delivery')
        procurement_plan_for_work_instance.actual_date_of_delivery=request.POST.get('actual_date_of_delivery')
        procurement_plan_for_work_instance.supplier_name=request.POST.get('supplier_name')
        procurement_plan_for_work_instance.remarks=request.POST.get('remarks')
        procurement_plan_for_work_instance.save()

        return redirect('procurement_list_for_work')


@requires_procurement_perm
def procurement_details_for_work(request,pk):
    procurement_plan_for_goods_instance=procurement_plan_for_work.objects.get(pk=pk)
    return render(request, 'procurements/procurement_details_for_work.html', {'procurement_data': procurement_plan_for_goods_instance})



@requires_procurement_perm
@requires_delete_perm
def delete_procurements_for_work(request):
    if request.user.is_admin == True and request.method == "POST":
        getid = request.POST['procurementid']
        procurement_plan_for_work_instance=procurement_plan_for_work.objects.get(id=int(getid))
        procurement_plan_for_work_instance.delete()
        return JsonResponse({'status': 'deleted'})




@requires_procurement_perm
def summery_for_work(request):
    if request.method == "GET":
        fromdate = request.GET.get('fromdate', datetime.today().strftime("%Y-%m-%d"))
        todate=request.GET.get('todate', datetime.today().strftime("%Y-%m-%d"))

        if fromdate == '':

            fromdate = datetime.today().strftime("%Y-%m-%d")
        
        if todate == '':
            todate = datetime.today().strftime("%Y-%m-%d")
        


        total_package = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)))
        total_otm = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')))
        total_rfq = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')))
        total_estimated_values = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(testimated=Sum('estimated_price'))['testimated']
        total_otm_estimated_values = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')).aggregate(otmtestimated=Sum('estimated_price'))['otmtestimated']
        total_rfq_estimated_values = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')).aggregate(rfqtestimated=Sum('estimated_price'))['rfqtestimated']

        contract_awarded_total = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_otm_total = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM') & ~Q(actual_date_of_contract_signing=None)))
        contract_awarded_rfq_total = len(procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ') & ~Q(actual_date_of_contract_signing=None)))

        contract_actual_total_value = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate)).aggregate(tvalue=Sum('actual_contract_amount'))['tvalue']
        contract_otm_actual_total_value = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='OTM')).aggregate(otmvalue=Sum('actual_contract_amount'))['otmvalue']
        contract_rfq_actual_total_value = procurement_plan_for_work.objects.filter(Q(organization=request.user.organization) & Q(date__gte=fromdate) & Q(date__lte=todate) & Q(procedure_method='RFQ')).aggregate(rfqvalue=Sum('actual_contract_amount'))['rfqvalue']

        datas = {'fromdate':fromdate,'todate':todate,
                'total_package':total_package,
                'total_otm':total_otm,
                'total_rfq':total_rfq,
                'total_estimated_values':total_estimated_values,
                'total_otm_estimated_values':total_otm_estimated_values,
                'total_rfq_estimated_values':total_rfq_estimated_values,
                'contract_awarded_total':contract_awarded_total,
                'contract_awarded_otm_total':contract_awarded_otm_total,
                'contract_awarded_rfq_total':contract_awarded_rfq_total,
                'contract_actual_total_value':contract_actual_total_value,
                'contract_otm_actual_total_value':contract_otm_actual_total_value,
                'contract_rfq_actual_total_value':contract_rfq_actual_total_value,

        }
        return render(request, 'procurements/procurement_for_work_summery.html', datas)