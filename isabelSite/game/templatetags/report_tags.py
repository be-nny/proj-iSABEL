# AUTHOR: Ben Abbott, Ipek Bal, Sam Pulsford
from django import template

from ..models import Report

register = template.Library()


def report(msg):
    Report.objects.create(message=msg)

def resolve(report):
    Report.objects.filter(report_id=report.report_id).delete()

@register.simple_tag
def save_report(request):
    message = request.GET.get('reportInputField', '')
    if message != '':
        report("Test2")

    # if message != "":
    #     new_report = Report.objects.create(message=message)
    #     return JsonResponse({'success': True})
    # else:
    #     return JsonResponse({'success': False, 'error': 'Message is required'})

