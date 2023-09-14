from django.template import Library
import json
import datetime
register = Library()
def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
@register.filter
def to_json(queryset):
    return json.dumps(
  queryset,
  sort_keys=True,
  indent=1,
  default=default
)

# def to_json(queryset):
#     return queryset