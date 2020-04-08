# Django Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Localfolder Library
from ..models.lead import PyLead


@login_required(login_url="base:login")
def DashboardCrmView(request):
    leads = PyLead.objects.all()
    return render(request, 'crm/dashboard-crm.html', {
        'leads': leads,
        'total_leads': leads,
        'new_leads': leads.filter(stage_id__name__iexact='nuevo'),
        'gained_leads': leads.filter(stage_id__name__iexact='ganado'),
        'lost_leads': leads.filter(stage_id__name__iexact='perdidos')
    })
