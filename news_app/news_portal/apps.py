from django.apps import AppConfig
from news_app.news_portal.signals import notify_about_new_post, send_notifications


class NewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal'

    def ready(self):
        notify_about_new_post, send_notifications
