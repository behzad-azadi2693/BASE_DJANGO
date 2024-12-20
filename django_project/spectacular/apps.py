from django.apps import AppConfig

class Spectacular(AppConfig):
    name = 'spectacular'

    def ready(self):
        from .spectacular_extensions import OauthAuthenticationScheme  # Ensure the extensions are loaded
