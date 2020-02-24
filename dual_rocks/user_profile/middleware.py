from dual_rocks.user_profile.models import Profile


class CurrentProfileMiddleware:
    CURRENT_PROFILE_ID_FIELD = 'current_profile_id'

    def __init__(self, get_response):
        self.get_response = get_response

    @classmethod
    def set_current_profile(cls, request, profile):
        request.session[
            CurrentProfileMiddleware.CURRENT_PROFILE_ID_FIELD] = profile.id
        request.current_profile = profile

    @classmethod
    def unset_current_profile(cls, request):
        del request.session[
            CurrentProfileMiddleware.CURRENT_PROFILE_ID_FIELD]

    def __call__(self, request):
        request.current_profile = None
        current_profile_id = request.session.get(
            CurrentProfileMiddleware.CURRENT_PROFILE_ID_FIELD
        )
        if request.user.is_authenticated and current_profile_id:
            try:
                request.current_profile = \
                    request.user.profiles.get(id=current_profile_id)
            except Profile.DoesNotExist:
                del request.session[
                    CurrentProfileMiddleware.CURRENT_PROFILE_ID_FIELD]
        response = self.get_response(request)
        return response
