from django.contrib import messages


def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = response['picture']
    if url:
        user.profile.avatar_url = url
    else:
        user.profile.avatar_url = "https://akai.org.pl/img/logo.svg"
    user.save()


def get_name(backend, strategy, details, response, user=None, *args, **kwargs):
    name = response['name'].split()
    if name[0]:
        user.first_name = name[0]
    if name[1:]:
        user.last_name = ' '.join(name[1:])
    user.save()

