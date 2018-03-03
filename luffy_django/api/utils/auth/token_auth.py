#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from django.utils.translation import ugettext_lazy as _

from rest_framework import HTTP_HEADER_ENCODING, exceptions


class LuffyTokenAuthentication(BaseAuthentication):
<<<<<<< HEAD
    keyword = 'Token'
=======
    keyword = 'token'
>>>>>>> d88e5362166088677c2fecc32ab1afc71f0a8611

    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        token = request.query_params.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('验证失败')

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        from api.models import UserAuthToken
        try:
            token_obj = UserAuthToken.objects.select_related('user').get(token=token)
<<<<<<< HEAD
=======
            print(token_obj,'99999999999999999999999')
>>>>>>> d88e5362166088677c2fecc32ab1afc71f0a8611
        except Exception as e:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return (token_obj.user, token_obj)
<<<<<<< HEAD
=======


>>>>>>> d88e5362166088677c2fecc32ab1afc71f0a8611
