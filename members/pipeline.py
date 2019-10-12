def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = response['picture']
    if url:
        user.profile.avatar_url = url
        user.save()
