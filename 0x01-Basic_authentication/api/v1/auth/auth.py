#!/usr/bin/env python3
"""Authentication module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Basic Authentification class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''checks if a given path require Auth'''
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        '''Return Authorization Header'''
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return Current User'''
        return None
