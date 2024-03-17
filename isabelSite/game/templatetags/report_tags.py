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

