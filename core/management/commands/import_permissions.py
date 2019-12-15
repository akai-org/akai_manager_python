from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from cms.models import *
from meetings.models import *
from members.models import *


class Command(BaseCommand):
    help = "Imports permissions into database."

    def handle(self, *args, **options):
        meeting_content_type = ContentType.objects.get_for_model(Meeting)
        profile_content_type = ContentType.objects.get_for_model(Profile)
        article_content_type = ContentType.objects.get_for_model(Article)
        image_content_type = ContentType.objects.get_for_model(Image)
        tag_content_type = ContentType.objects.get_for_model(Tag)

        manage_image, _ = Permission.objects.update_or_create(
            codename='manage_image',
            defaults={
                'name': 'Can manage images',
                'content_type': image_content_type
            }
        )

        manage_tag, _ = Permission.objects.update_or_create(
            codename='manage_tag',
            defaults={
                'name': 'Can manage tags',
                'content_type': tag_content_type
            }
        )

        manage_article, _ = Permission.objects.update_or_create(
            codename='manage_article',
            defaults={
                'name': 'Can manage articles',
                'content_type': article_content_type
            }
        )

        manage_meeting, _ = Permission.objects.update_or_create(
            codename='manage_meeting',
            defaults={
                'name': 'Can manage meetings',
                'content_type': meeting_content_type
            }
        )

        manage_profile, _ = Permission.objects.update_or_create(
            codename='manage_profile',
            defaults={
                'name': 'Can manage profiles',
                'content_type': profile_content_type
            }
        )

        edit_meeting_agenda, _ = Permission.objects.update_or_create(
            codename='edit_meeting_agenda',
            defaults={
                'name': 'Can edit meeting agenda',
                'content_type': article_content_type
            }
        )

        sign_to_meeting, _ = Permission.objects.update_or_create(
            codename='sign_to_meeting',
            defaults={
                'name': 'Can sign into a meeting',
                'content_type': meeting_content_type
            }
        )

        admin, _ = Group.objects.update_or_create(name='admin')
        publisher, _ = Group.objects.update_or_create(name='publisher')
        staff, _ = Group.objects.update_or_create(name='staff')
        member, _ = Group.objects.update_or_create(name='member')

        admin.permissions.set([
            manage_article,
            manage_image,
            manage_meeting,
            manage_profile,
            manage_tag,
            edit_meeting_agenda,
            sign_to_meeting
        ])
        publisher.permissions.set([
            manage_article,
            manage_image,
            manage_tag,
        ])
        staff.permissions.set([
            manage_article,
            manage_image,
            manage_meeting,
            manage_tag,
            edit_meeting_agenda,
            sign_to_meeting
        ])
        member.permissions.set([
            sign_to_meeting
        ])
