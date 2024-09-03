#!/usr/bin/env python3
"""Basic Auth module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Basic Authentification class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Require Auth'''
        return False

    def authorization_header(self, request=None) -> str:
        '''Return Authorization Header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return Current User'''
        return None
