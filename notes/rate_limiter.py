from django.http import HttpResponseForbidden
from datetime import datetime, timedelta


request_count = {} # stores the request count for each IP address
rate_limit = 5  # Requests allowed per minute
window_size = timedelta(minutes=1)  # Time window for rate limiting

def rate_limiter(view_func):
    def wrapped(request, *args, **kwargs):
        ip_address = get_client_ip(request)
        now = datetime.now()

        # Initialize request count for the IP address if not present
        request_count[ip_address] = request_count.get(ip_address, [])

        # Remove requests outside the time window
        request_count[ip_address] = [req_time for req_time in request_count[ip_address] if now - req_time < window_size]
        if len(request_count[ip_address]) >= rate_limit:
            return HttpResponseForbidden("Rate limit exceeded")

        request_count[ip_address].append(now)

        # Call the original view function
        return view_func(request, *args, **kwargs)

    return wrapped

# Utility function to get the client's IP address
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
