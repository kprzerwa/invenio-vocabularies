# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Example service."""

from invenio_records_resources.services import RecordService, \
    RecordServiceConfig
from invenio_records_resources.services.records.schema import RecordSchema
from invenio_records_resources.services.records.search import terms_filter

from .api import Vocabulary
from .permissions import PermissionPolicy


class ServiceConfig(RecordServiceConfig):
    """Mock service configuration."""

    permission_policy_cls = PermissionPolicy
    record_cls = Vocabulary
    schema = RecordSchema
    search_facets_options = {
        "aggs": {
            "type": {
                "terms": {"field": "metadata.type.type"},
            }
        },
        "post_filters": {
            "type": terms_filter("metadata.type.type"),
        },
    }


class Service(RecordService):
    """Mock service."""

    default_config = ServiceConfig
