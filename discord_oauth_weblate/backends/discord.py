"""Melhor que o teu, *muito* melhor que o teu"""

from social_core.backends.oauth import BaseOAuth2


class DiscordOAuth2(BaseOAuth2):
    name = "discord"
    HOSTNAME = "discord.com"
    AUTHORIZATION_URL = "https://%s/api/oauth2/authorize" % HOSTNAME
    ACCESS_TOKEN_URL = "https://%s/api/oauth2/token" % HOSTNAME
    ACCESS_TOKEN_METHOD = "POST"
    REVOKE_TOKEN_URL = "https://%s/api/oauth2/token/revoke" % HOSTNAME
    REVOKE_TOKEN_METHOD = "GET"
    DEFAULT_SCOPE = ["identify", "email", "guilds.members.read"]
    SCOPE_SEPARATOR = "+"
    REDIRECT_STATE = False
    EXTRA_DATA = [("expires_in", "expires"), ("refresh_token", "refresh_token")]

    def get_user_details(self, response):
        return {
            "username": response.get("username"),
            "email": response.get("email"),
        }

    def user_data(self, access_token, *args, **kwargs):
        url = "https://%s/api/users/@me" % self.HOSTNAME
        auth_header = {"Authorization": "Bearer %s" % access_token}
        return self.get_json(url, headers=auth_header)

    def has_joined_guild(self, access_token, guild_id, *args, **kwargs):
        url = "https://%s/api/users/@me/guilds/%s/member" % (self.HOSTNAME, guild_id)
        auth_header = {"Authorization": "Bearer %s" % access_token}
        return self.get_json(url, headers=auth_header)

    def auth_allowed(self, response, details):
        print(response)
        raise NotImplementedError()



