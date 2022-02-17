from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
# create a django view
def main_page(request):
    all_procurments_for_goods = procurement_plan_for_goods.objects.filter(organization=request.user.organization)
    return render(request, 'dashboard/index.html', {'all_procurments_for_goods': all_procurments_for_goods})

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

        procurement_plan_for_goods_instance=procurement_plan_for_goods(organization=request.user.organization,contract_package_number=contract_package_number,contract_description=contract_description,unit=unit,quantity=quantity,estimated_price=estimated_price,actual_contract_amount=actual_contract_amount,procedure_method=procedure_method,procurement_guidelines=procurement_guidelines,prior_review=prior_review,contract_approving_authority=contract_approving_authority,planned_date_of_ifb_publication=planned_date_of_ifb_publication,actual_date_of_ifb_publication=actual_date_of_ifb_publication,planned_date_of_bid_opening=planned_date_of_bid_opening,actual_date_of_bid_opening=actual_date_of_bid_opening,planned_date_of_contract_singning=planned_date_of_contract_singning,actual_date_of_contract_signing=actual_date_of_contract_signing,planned_date_of_delivery=planned_date_of_delivery,actual_date_of_delivery=actual_date_of_delivery,supplier_name=supplier_name,remarks=remarks)
        procurement_plan_for_goods_instance.save()
        return redirect('main_procurement_page')



def procurement_details(request,pk):
    procurement_plan_for_goods_instance=procurement_plan_for_goods.objects.get(pk=pk)
    return render(request, 'procurements/procurement-details.html', {'procurement_data': procurement_plan_for_goods_instance})



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


def delete_procurements_for_goods(request):
    if request.user.is_admin == True and request.method == "POST":
        getid = request.POST['procurementid']
        procurement_plan_for_goods_instance=procurement_plan_for_goods.objects.get(id=int(getid))
        procurement_plan_for_goods_instance.delete()
        return JsonResponse({'status': 'deleted'})










