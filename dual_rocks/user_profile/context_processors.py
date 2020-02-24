def current_profile(request):
    if hasattr(request, 'current_profile'):
        return {
            'current_profile': request.current_profile
        }
    return {}
