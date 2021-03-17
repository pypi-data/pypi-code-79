# Copyright (C) 2020  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

from datetime import datetime
from typing import Optional, Set

from django.contrib.auth.models import User
from django.db import models


class OIDCUser(User):
    """
    Custom User proxy model for remote users storing OpenID Connect
    related data: profile containing authentication tokens.

    The model is also not saved to database as all users are already stored
    in the Keycloak one.
    """

    # OIDC subject identifier
    sub: str = ""

    # OIDC tokens and session related data, only relevant when a user
    # authenticates from a web browser
    access_token: Optional[str] = None
    expires_at: Optional[datetime] = None
    id_token: Optional[str] = None
    refresh_token: Optional[str] = None
    refresh_expires_at: Optional[datetime] = None
    scope: Optional[str] = None
    session_state: Optional[str] = None

    # User permissions
    permissions: Set[str]

    class Meta:
        app_label = "swh_web_auth"
        proxy = True

    def save(self, **kwargs):
        """
        Override django.db.models.Model.save to avoid saving the remote
        users to web application database.
        """
        pass

    def get_group_permissions(self, obj=None) -> Set[str]:
        """
        Override django.contrib.auth.models.PermissionsMixin.get_group_permissions
        to get permissions from OIDC
        """
        return self.get_all_permissions(obj)

    def get_all_permissions(self, obj=None) -> Set[str]:
        """
        Override django.contrib.auth.models.PermissionsMixin.get_all_permissions
        to get permissions from OIDC
        """
        return self.permissions

    def has_perm(self, perm, obj=None) -> bool:
        """
        Override django.contrib.auth.models.PermissionsMixin.has_perm
        to check permission from OIDC
        """
        if self.is_active and self.is_superuser:
            return True

        return perm in self.permissions

    def has_module_perms(self, app_label) -> bool:
        """
        Override django.contrib.auth.models.PermissionsMixin.has_module_perms
        to check permissions from OIDC.
        """
        if self.is_active and self.is_superuser:
            return True

        return any(perm.startswith(app_label) for perm in self.permissions)


class OIDCUserOfflineTokens(models.Model):
    """
    Model storing encrypted bearer tokens generated by users.
    """

    user_id = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    offline_token = models.BinaryField()

    class Meta:
        app_label = "swh_web_auth"
        db_table = "oidc_user_offline_tokens"
