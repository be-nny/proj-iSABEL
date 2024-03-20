# AUTHOR: Ben Abbott, Merve Ipek Bal, Sam Pulsford
from django import template

from ..models import Report

register = template.Library()

# Function to create a new report with the provided message
def report(msg):
    Report.objects.create(message=msg)

# Function to resolve a report by deleting it from the database
@register.simple_tag
def resolve(report):
    id = report.report_id
    Report.objects.get(report_id=id).delete()

# Decorator to register the function as a simple template tag
@register.simple_tag
def save_report(request):
    message = request.GET.get('reportInputField', '')
    if message != '':
        report(message)



