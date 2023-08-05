from typing import Optional

from pydantic import BaseModel

from . import response as response_models

MODEL_TYPE = 'hub'


class APIHubFields(BaseModel):
    name: Optional[str] = None


class APIHubRelationships(BaseModel):
    regional_site_entrepreneurs: Optional[response_models.APILinksAndData] = None
    pods: Optional[response_models.APILinksAndData] = None
    schools: Optional[response_models.APILinksAndData] = None


class APIHubData(response_models.APIData):
    fields: APIHubFields


class ListAPIHubData(BaseModel):
    __root__: list[APIHubData]

