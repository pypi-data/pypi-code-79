"""
Module for Terraform Cloud API Endpoint: Org Memberships.
"""

from .endpoint import TFCEndpoint
from ._constants import MAX_PAGE_SIZE

class TFCOrgMemberships(TFCEndpoint):
    """
    `Org Memberships API Docs \
        <https://www.terraform.io/docs/cloud/api/organization-memberships.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._endpoint_base_url = f"{self._api_v2_base_url}/organization-memberships"
        self._org_base_url = \
            f"{self._api_v2_base_url}/organizations/{org_name}/organization-memberships"

    def required_entitlements(self):
        return []

    def terraform_cloud_only(self):
        return False

    def terraform_enterprise_only(self):
        return False

    def invite(self, payload):
        """
        ``POST /organizations/:organization_name/organization-memberships``

        `Org Memberships Invite API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#invite-a-user-to-an-organization>`_

        `Invite Sample Payload \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#sample-payload>`_
        """
        return self._create(self._org_base_url, payload)

    def list_for_org(self, query=None, filters=None, page=None, page_size=None):
        """
        ``GET /organizations/:organization_name/organization-memberships``

        `Org Memberships List for Org API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#list-memberships-for-an-organization>`_

        Query Parameter(s) (`details \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#query-parameters>`_):
            - ``query`` (Optional)
            - ``filter[status]`` (Optional)
            - ``page`` (Optional)
            - ``page_size`` (Optional)

        Example filter(s):

        .. code-block:: python

            filters = [
                {
                    "keys": ["status"],
                    "value": "foo"
                }
            ]

        """
        return self._list(\
            self._org_base_url, query=query, filters=filters, page=page, page_size=page_size)

    def list_all_for_org(self, query=None, filters=None):
        """
        This function does not correlate to an endpoint in the TFC API Docs specifically,
        but rather is a helper function to wrap the `list` endpoint, which enumerates out
        every page so users do not have to implement the paging logic every time they just
        want to list every org membership for an organization.

        Returns an array of objects.
        """
        current_page_number = 1
        org_memberships_resp = \
            self._list(self._org_base_url, \
                page=current_page_number, page_size=MAX_PAGE_SIZE, query=query, filters=filters)
        total_pages = org_memberships_resp["meta"]["pagination"]["total-pages"]

        org_memberships = []
        while current_page_number <= total_pages:
            org_memberships_resp = \
                self._list(self._org_base_url, \
                    page=current_page_number, page_size=MAX_PAGE_SIZE, query=query, filters=filters)
            org_memberships += org_memberships_resp["data"]
            current_page_number += 1

        return org_memberships

    def list_for_user(self):
        """
        ``GET /organization-memberships``

        `Org Memberships List for User API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#list-user-39-s-own-memberships>`_
        """
        return self._list(self._endpoint_base_url)

    def show(self, org_membership_id):
        """
        ``GET /organization-memberships/:organization_membership_id``

        `Org Memberships Show API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#show-a-membership>`_
        """
        url = f"{self._endpoint_base_url}/{org_membership_id}"
        return self._show(url)

    def remove(self, org_membership_id):
        """
        ``DELETE /organization-memberships/:organization_membership_id``

        `Org Memberships Remove API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/organization-memberships.html#remove-user-from-organization>`_
        """
        url = f"{self._endpoint_base_url}/{org_membership_id}"
        return self._destroy(url)
