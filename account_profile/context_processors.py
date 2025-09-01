
from .models import Profile


def profile_processor(request):
    profile = None
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)

    return {'profile': profile}
