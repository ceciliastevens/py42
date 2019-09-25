import json

from py42._internal.base_classes import BaseAuthorityClient


class OrgClient(BaseAuthorityClient):
    def create_org(
        self,
        org_name,
        org_ext_ref=None,
        notes=None,
        parent_org_uid=None,
        classification=None,
        **kwargs
    ):
        uri = u"/api/Org/"
        data = {
            u"orgName": org_name,
            u"orgExtRef": org_ext_ref,
            u"notes": notes,
            u"parentOrgUid": parent_org_uid,
            u"classification": classification,
        }
        return self._default_session.post(uri, data=json.dumps(data), **kwargs)

    def get_org_by_uid(self, org_uid, **kwargs):
        uri = u"/api/Org/{0}?idType=orgUid".format(org_uid)
        return self._default_session.get(uri, **kwargs)

    def get_orgs(self, page_num=None, page_size=None, **kwargs):
        uri = u"/api/Org"
        params = {u"pgNum": page_num, u"pgSize": page_size}

        return self._default_session.get(uri, params=params, **kwargs)

    def block_org(self, org_id, **kwargs):
        uri = u"/api/OrgBlock/{0}".format(org_id)
        return self._default_session.put(uri, **kwargs)

    def unblock_org(self, org_id, **kwargs):
        uri = u"/api/OrgBlock/{0}".format(org_id)
        return self._default_session.delete(uri, **kwargs)

    def deactivate_org(self, org_id, **kwargs):
        uri = u"/api/OrgDeactivation/{0}".format(org_id)
        return self._default_session.put(uri, **kwargs)

    def reactivate_org(self, org_id, **kwargs):
        uri = u"/api/OrgDeactivation/{0}".format(org_id)
        return self._default_session.delete(uri, **kwargs)

    def get_current_user_org(self, **kwargs):
        uri = u"/api/Org/my"
        return self._default_session.get(uri, **kwargs)