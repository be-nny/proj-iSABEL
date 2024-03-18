# AUTHOR: Ben Abbott
from django import template

from ..models import Report

register = template.Library()

@register.simple_tag
def report(msg):
    new_report = Report(message=msg)
    new_report.save()

@register.simple_tag
def resolve(report):
    Report.objects.filter(report_id=report.report_id).delete()

@register.simple_tag
def save_report(request):
    message = request.GET.get('reportInputField')
    if message != "":
        new_report = Report.objects.create(message=message)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Message is required'})

