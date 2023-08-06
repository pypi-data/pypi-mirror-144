"""API Client
"""
from relevanceai.package_utils.base import _Base
from relevanceai.api.endpoints.admin.admin import AdminClient
from relevanceai.api.endpoints.datasets.datasets import DatasetsClient
from relevanceai.api.endpoints.services.services import ServicesClient
from relevanceai.api.endpoints.reports.reports import ReportsClient
from relevanceai.api.endpoints.deployables.deployables import DeployableClient
from relevanceai.package_utils.datasets import ExampleDatasets


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


class APIClient(_Base):
    """API Client"""

    def __init__(self, project: str, api_key: str, firebase_uid: str):
        self.datasets = DatasetsClient(
            project=project, api_key=api_key, firebase_uid=firebase_uid
        )
        self.services = ServicesClient(
            project=project, api_key=api_key, firebase_uid=firebase_uid
        )
        self.example_datasets = ExampleDatasets()
        self.admin = AdminClient(
            project=project, api_key=api_key, firebase_uid=firebase_uid
        )
        self.reports = ReportsClient(
            project=project, api_key=api_key, firebase_uid=firebase_uid
        )
        self.deployables = DeployableClient(
            project=project, api_key=api_key, firebase_uid=firebase_uid
        )
        super().__init__(project=project, api_key=api_key, firebase_uid=firebase_uid)
