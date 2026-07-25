"""
Project : Invoice Generator
Project ID : 013

Invoice Model
"""

from dataclasses import dataclass, field

from src.models.company_model import CompanyModel
from src.models.customer_model import CustomerModel
from src.models.invoice_item_model import InvoiceItemModel


@dataclass(slots=True)
class InvoiceModel:
    """
    Represents a complete invoice.
    """

    # --------------------------------------------------------------
    # Invoice Information
    # --------------------------------------------------------------

    invoice_number: str = ""

    invoice_date: str = ""

    due_date: str = ""

    purchase_order_number: str = ""

    payment_terms: str = ""

    currency: str = "USD"

    notes: str = ""

    # --------------------------------------------------------------
    # Business Information
    # --------------------------------------------------------------

    company: CompanyModel = field(default_factory=CompanyModel)

    # --------------------------------------------------------------
    # Customer Information
    # --------------------------------------------------------------

    customer: CustomerModel = field(default_factory=CustomerModel)

    # --------------------------------------------------------------
    # Invoice Items
    # --------------------------------------------------------------

    invoice_items: list[InvoiceItemModel] = field(default_factory=list)

    # --------------------------------------------------------------
    # Invoice Totals
    # --------------------------------------------------------------

    subtotal: float = 0.0

    total_discount: float = 0.0

    total_tax: float = 0.0

    grand_total: float = 0.0


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceModel()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# dataclasses
# src.models.company_model
# src.models.customer_model
# src.models.invoice_item_model