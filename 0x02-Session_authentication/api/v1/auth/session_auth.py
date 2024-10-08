#!/usr/bin/env python3
"""
session Authentication module for the API
"""
from api.v1.auth.auth import Auth
import uuid
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    '''session-based authentication class'''

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id'''

        if user_id is None or type(user_id) is not str:
            return None

        new_session_id = uuid.uuid4()
        self.user_id_by_session_id[new_session_id] = user_id
        return new_session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on a Session ID'''

        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        ''' returns a User instance based on a cookie value'''
        cookie_name = Auth.session_cookie(request)
        user_id = self.user_id_by_session_id(cookie_name)
        return User.get(user_id)
