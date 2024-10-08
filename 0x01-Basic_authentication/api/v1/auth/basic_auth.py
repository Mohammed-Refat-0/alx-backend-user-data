#!/usr/bin/env python3
"""Basic Auth module"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    '''Basic Auth class'''

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        '''returns the Base64 part of the Authorization header
        '''
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        '''returns the decoded value of a Base64 string
        base64_authorization_header'''
        if base64_authorization_header is None or \
           not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        '''returns the user email and password from the Base64 decoded value'''

        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        '''returns the User instance based on his email and password.'''
        if user_email is None or not isinstance(user_email, str) or \
           user_pwd is None or not isinstance(user_pwd, str):
            return None
        if not User.search({'email': user_email}):
            return
        if not self.is_valid_password(user_pwd):
            return
        return User.search({'email': user_email})[0]

    def current_user(self, request=None) -> TypeVar('User'):
        '''retrieves the User instance for a request'''
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
