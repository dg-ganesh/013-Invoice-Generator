"""
Project : Invoice Generator
Project ID : 013

Invoice Serializer
"""

from dataclasses import asdict

from src.models.invoice_model import InvoiceModel


class InvoiceSerializer:
    """
    Converts InvoiceModel objects into dictionaries that
    can be written to JSON.

    This module performs serialization only.
    It does not perform file operations.
    """

    @staticmethod
    def to_dict(
        invoice: InvoiceModel,
    ) -> dict:
        """
        Converts an InvoiceModel into a dictionary.
        """

        return asdict(invoice)

    @staticmethod
    def to_json_data(
        invoice: InvoiceModel,
    ) -> dict:
        """
        Returns a JSON-ready dictionary.

        This method exists to provide a stable public
        interface should future serialization require
        additional transformations.
        """

        return InvoiceSerializer.to_dict(invoice)


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceSerializer.to_dict(invoice)
# InvoiceSerializer.to_json_data(invoice)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# dataclasses.asdict
# src.models.invoice_model