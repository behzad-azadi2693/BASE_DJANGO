from drf_spectacular.extensions import OpenApiAuthenticationExtension

class OauthAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'oauth2_provider.contrib.rest_framework.OAuth2Authentication'  # full import path to your authentication class
    name = 'OauthToken'  # name used in the 'SECURITY' setting

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }