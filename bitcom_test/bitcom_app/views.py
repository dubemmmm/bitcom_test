from django.shortcuts import redirect, render, get_object_or_404
from .models import PollingUnit, AnnouncedPuResults, Lga
from django.db.models import Sum

# View for the landing page
def landing_page(request):
    return render(request, 'bitcom_app/landing.html')

# View to display the polling units individual results
def view_polling_units(request):
    all_objects = PollingUnit.objects.filter(uniqueid__lte=109)
    return render(request, 'bitcom_app/template.html', {'all_objects': all_objects})

# View to display the details of each polling unit
def polling_unit_results(request, uniqueid):
    # To Retrieve the PollingUnit object using uniqueid
    polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)

    # Retrieve the AnnouncedPuResults based on polling_unit_uniqueid
    announced_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=uniqueid)
    #Context dictionary so that content can be injected into the template
    context = {
        'polling_unit': polling_unit,
        'announced_results': announced_results,
    }
    return render(request, 'bitcom_app/polling_unit_results.html', context)

# View to display the List Local Governments
def lga_list(request):
    lgas = Lga.objects.all()
    return render(request, 'bitcom_app/lga_lists.html', {'lgas': lgas})

# View 
def lga_results(request, pk):
    selected_lga = get_object_or_404(Lga, uniqueid=pk)

    # To Fetch polling units under the selected local government
    polling_units = PollingUnit.objects.filter(lga_id=selected_lga.lga_id)

    # To Calculate the summed total result
    summed_results = AnnouncedPuResults.objects.filter(
        polling_unit_uniqueid__in=polling_units.values_list('uniqueid', flat=True)
    ).aggregate(total_score=Sum('party_score'))

    return render(request, 'bitcom_app/lga_results.html', {
        'selected_lga': selected_lga,
        'polling_units': polling_units,
        'summed_results': summed_results['total_score'] if summed_results['total_score'] else 0,
    })
    

from .models import NewPollingUnitResults
from .forms import PollingUnitResultsForm

def new_polling_unit_results(request):
    if request.method == 'POST':
        form = PollingUnitResultsForm(request.POST)
        if form.is_valid():
            new_results = form.save()
            return redirect('success_page', pk=new_results.result_id)
    else:
        form = PollingUnitResultsForm()

    return render(request, 'bitcom_app/new_polling_unit_results.html', {'form': form})

def success_page(request, pk):
    new_results = get_object_or_404(NewPollingUnitResults, result_id=pk)
    context = {'new_results': new_results}
    return render(request, 'bitcom_app/success_page.html', context)


