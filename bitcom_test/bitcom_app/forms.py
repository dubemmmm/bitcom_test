# forms.py

from django import forms
from .models import NewPollingUnitResults

class PollingUnitResultsForm(forms.ModelForm):
    class Meta:
        model = NewPollingUnitResults
        fields = ['polling_unit_name', 'pdp_votes', 'acn_votes', 'dpp_votes', 'ppa_votes', 'cdc_votes', 'anpp_votes', 'jp_votes', 'labour_votes', 'cpp_votes', 'entered_by_user']
