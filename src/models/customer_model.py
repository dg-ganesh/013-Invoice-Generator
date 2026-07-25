"""
Project : Invoice Generator
Project ID : 013

Customer Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CustomerModel:
    """
    Represents customer information for an invoice.
    """

    customer_name: str = ""

    address_line_1: str = ""
    address_line_2: str = ""

    city: str = ""
    state: str = ""
    postal_code: str = ""
    country: str = ""

    phone_number: str = ""
    email_address: str = ""

    customer_reference: str = ""


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# CustomerModel()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# dataclasses