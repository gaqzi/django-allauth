# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from allauth.socialaccount.providers import registry

from .provider import DropboxProvider


class DropboxTests(create_oauth2_tests(registry.by_id(DropboxProvider.id))):
    def get_mocked_response(self):
        return [MockedResponse(200, """{
            "display_name": "Björn Andersson",
            "name_details": {
                "surname": "Andersson",
                "familiar_name": "Björn",
                "given_name": "Björn"
                },
            "locale": "en",
            "email": "test@example.se",
            "uid": 1234567890,
            "email_verified": true,
            "quota_info": {
                "shared": 3195052017,
                "datastores": 0,
                "quota": 61337501696,
                "normal": 15455059441
                },
            "is_paired": true,
            "team": null,
            "referral_link": "https://db.tt/UzhBTVjU",
            "country": "SE"
        }""")]
