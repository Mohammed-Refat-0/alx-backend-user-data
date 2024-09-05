#!/usr/bin/env python3
"""
session Authentication module for the API
"""
from api.v1.auth.auth import Auth
import uuid


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
