from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserToken(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):

        return str(user.pk) + str(timestamp)

token_generator = UserToken()
