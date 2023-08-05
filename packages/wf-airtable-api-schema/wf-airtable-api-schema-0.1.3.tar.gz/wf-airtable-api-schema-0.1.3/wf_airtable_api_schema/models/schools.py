from datetime import date
from typing import Optional

from pydantic import BaseModel, HttpUrl

from . import response as response_models

MODEL_TYPE = 'school'


class APISchoolFields(BaseModel):
    name: Optional[str] = None
    short_name: Optional[str] = None
    details: Optional[str] = None
    logo_url: Optional[HttpUrl] = None
    domain_name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    ages_served: Optional[list[str]] = []
    school_calendar: Optional[str] = None
    school_schedule: Optional[list[str]] = []
    school_phone: Optional[str] = None
    school_email: Optional[str] = None
    website: Optional[HttpUrl] = None

    status: Optional[str] = None
    ssj_stage: Optional[str] = None
    began_ssj_at: Optional[date] = None
    entered_planning_at: Optional[date] = None
    entered_startup_at: Optional[date] = None
    opened_at: Optional[date] = None
    projected_open: Optional[date] = None
    affiliation_status: Optional[str] = None
    affiliated_at: Optional[date] = None
    affiliation_agreement_url: Optional[HttpUrl] = None
    nonprofit_status: Optional[str] = None
    left_network_reason: Optional[str] = None
    left_network_date: Optional[date] = None


class APISchoolRelationships(BaseModel):
    hub: Optional[response_models.APILinksAndData] = None
    pod: Optional[response_models.APILinksAndData] = None
    guides_and_entrepreneurs: Optional[response_models.APILinksAndData] = None
    educators: Optional[response_models.APILinksAndData] = None
    current_educators: Optional[response_models.APILinksAndData] = None
    primary_contacts: Optional[response_models.APILinksAndData] = None


class APISchoolData(response_models.APIData):
    fields: APISchoolFields


class ListAPISchoolData(BaseModel):
    __root__: list[APISchoolData]
