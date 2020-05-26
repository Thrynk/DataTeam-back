from functools import wraps
from django.shortcuts import render, redirect


def logout_required(redirect_url_name):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                #Do something for authenticated users...
                return redirect(redirect_url_name)
            else:
                #Do something for anonymous users...
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator