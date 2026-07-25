"""
Project : Invoice Generator
Project ID : 013

Invoice Item Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InvoiceItemModel:
    """
    Represents a single invoice line item.
    """

    line_number: int = 0

    description: str = ""

    quantity: float = 0.0

    unit_price: float = 0.0

    tax_percentage: float = 0.0

    discount_percentage: float = 0.0

    line_subtotal: float = 0.0

    tax_amount: float = 0.0

    discount_amount: float = 0.0

    line_total: float = 0.0


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceItemModel()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# dataclasses