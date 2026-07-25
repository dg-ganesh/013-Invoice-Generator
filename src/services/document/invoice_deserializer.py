"""
Project : Invoice Generator
Project ID : 013

Invoice Deserializer
"""

from src.models.company_model import CompanyModel
from src.models.customer_model import CustomerModel
from src.models.invoice_item_model import InvoiceItemModel
from src.models.invoice_model import InvoiceModel


class InvoiceDeserializer:
    """
    Reconstructs InvoiceModel objects from dictionaries.

    This module performs deserialization only.
    It performs no file operations.
    """

    @staticmethod
    def deserialize(
        data: dict,
    ) -> InvoiceModel:
        """
        Creates an InvoiceModel from a dictionary.
        """

        invoice = InvoiceModel()

        InvoiceDeserializer._load_invoice_information(
            invoice,
            data,
        )

        InvoiceDeserializer._load_company(
            invoice,
            data.get("company", {}),
        )

        InvoiceDeserializer._load_customer(
            invoice,
            data.get("customer", {}),
        )

        InvoiceDeserializer._load_invoice_items(
            invoice,
            data.get("invoice_items", []),
        )

        InvoiceDeserializer._load_totals(
            invoice,
            data,
        )

        return invoice

    # ----------------------------------------------------------
    # Private Methods
    # ----------------------------------------------------------

    @staticmethod
    def _load_invoice_information(
        invoice: InvoiceModel,
        data: dict,
    ) -> None:

        invoice.invoice_number = data.get(
            "invoice_number",
            "",
        )

        invoice.invoice_date = data.get(
            "invoice_date",
            "",
        )

        invoice.due_date = data.get(
            "due_date",
            "",
        )

        invoice.purchase_order_number = data.get(
            "purchase_order_number",
            "",
        )

        invoice.payment_terms = data.get(
            "payment_terms",
            "",
        )

        invoice.currency = data.get(
            "currency",
            "USD",
        )

        invoice.notes = data.get(
            "notes",
            "",
        )

    @staticmethod
    def _load_company(
        invoice: InvoiceModel,
        data: dict,
    ) -> None:

        invoice.company = CompanyModel(**data)

    @staticmethod
    def _load_customer(
        invoice: InvoiceModel,
        data: dict,
    ) -> None:

        invoice.customer = CustomerModel(**data)

    @staticmethod
    def _load_invoice_items(
        invoice: InvoiceModel,
        items: list[dict],
    ) -> None:

        invoice.invoice_items.clear()

        for item_data in items:

            invoice.invoice_items.append(
                InvoiceItemModel(**item_data)
            )

    @staticmethod
    def _load_totals(
        invoice: InvoiceModel,
        data: dict,
    ) -> None:

        invoice.subtotal = data.get(
            "subtotal",
            0.0,
        )

        invoice.total_discount = data.get(
            "total_discount",
            0.0,
        )

        invoice.total_tax = data.get(
            "total_tax",
            0.0,
        )

        invoice.grand_total = data.get(
            "grand_total",
            0.0,
        )


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceDeserializer.deserialize(data)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# src.models.company_model
# src.models.customer_model
# src.models.invoice_item_model
# src.models.invoice_model