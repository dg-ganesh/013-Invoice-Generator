"""
Project : Invoice Generator
Project ID : 013

Company Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CompanyModel:
    """
    Represents the seller/business information.
    """

    company_name: str = ""
    address_line_1: str = ""
    address_line_2: str = ""
    city: str = ""
    state: str = ""
    postal_code: str = ""
    country: str = ""

    phone_number: str = ""
    email_address: str = ""
    website: str = ""

    tax_registration_number: str = ""

    logo_path: str = ""


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# CompanyModel()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# dataclasses