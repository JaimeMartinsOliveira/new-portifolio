from .models import VisitorCount

def visitor_count(request):
    count_obj, created = VisitorCount.objects.get_or_create(pk=1)
    return {'total_visitors': count_obj.count}