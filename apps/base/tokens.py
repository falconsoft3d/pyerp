"""Generador del tokens para el registro de usuarios
"""
# Django Library
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    """Esta clase genera un token que se envía en correo para validadar el
    registro del usuario
    """
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) +
            str(user.is_active)
        )

ACCOUNT_ACTIVATION_TOKEN = TokenGenerator()

PASSWORD_RECOVERY_TOKEN = TokenGenerator()
