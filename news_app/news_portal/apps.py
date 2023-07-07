from django.apps import AppConfig
from news_app.news_portal.signals import notify_about_new_post, send_notifications
import redis


class NewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal'

    def ready(self):
        notify_about_new_post, send_notifications


red = redis.Redis(
    host='redis-11624.c293.eu-central-1-1.ec2.cloud.redislabs.com',
    port=11624,
    password='UnhS2QSk8DKfhRU07rx7PkceOllCx5G9'
)

