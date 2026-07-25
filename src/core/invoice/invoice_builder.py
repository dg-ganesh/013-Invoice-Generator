"""
Project : Invoice Generator
Project ID : 013

Invoice Builder
"""

from src.models.company_model import CompanyModel
from src.models.customer_model import CustomerModel
from src.models.invoice_item_model import InvoiceItemModel
from src.models.invoice_model import InvoiceModel


class InvoiceBuilder:
    """
    Creates InvoiceModel instances from application data.

    This module assembles the invoice model but performs
    no validation or calculations.
    """

    @staticmethod
    def create_invoice(
        company: CompanyModel,
        customer: CustomerModel,
        invoice_number: str,
        invoice_date: str,
        due_date: str,
        purchase_order_number: str = "",
        payment_terms: str = "",
        currency: str = "USD",
        notes: str = "",
    ) -> InvoiceModel:
        """
        Creates a new invoice.
        """

        invoice = InvoiceModel()

        invoice.company = company
        invoice.customer = customer

        invoice.invoice_number = invoice_number.strip()
        invoice.invoice_date = invoice_date.strip()
        invoice.due_date = due_date.strip()

        invoice.purchase_order_number = (
            purchase_order_number.strip()
        )

        invoice.payment_terms = payment_terms.strip()

        invoice.currency = currency.strip().upper()

        invoice.notes = notes.strip()

        return invoice

    @staticmethod
    def add_invoice_item(
        invoice: InvoiceModel,
        item: InvoiceItemModel,
    ) -> None:
        """
        Adds an invoice item.
        """

        item.line_number = len(invoice.invoice_items) + 1

        invoice.invoice_items.append(item)

    @staticmethod
    def remove_invoice_item(
        invoice: InvoiceModel,
        line_number: int,
    ) -> bool:
        """
        Removes an invoice item.

        Returns True if removed.
        """

        for index, item in enumerate(invoice.invoice_items):

            if item.line_number == line_number:

                del invoice.invoice_items[index]

                InvoiceBuilder.renumber_invoice_items(
                    invoice
                )

                return True

        return False

    @staticmethod
    def clear_invoice_items(
        invoice: InvoiceModel,
    ) -> None:
        """
        Removes all invoice items.
        """

        invoice.invoice_items.clear()

    @staticmethod
    def renumber_invoice_items(
        invoice: InvoiceModel,
    ) -> None:
        """
        Ensures sequential line numbers.
        """

        for index, item in enumerate(
            invoice.invoice_items,
            start=1,
        ):
            item.line_number = index

    @staticmethod
    def get_invoice_item(
        invoice: InvoiceModel,
        line_number: int,
    ) -> InvoiceItemModel | None:
        """
        Returns an invoice item by line number.
        """

        for item in invoice.invoice_items:

            if item.line_number == line_number:
                return item

        return None


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceBuilder.create_invoice(...)
# InvoiceBuilder.add_invoice_item(invoice, item)
# InvoiceBuilder.remove_invoice_item(invoice, line_number)
# InvoiceBuilder.clear_invoice_items(invoice)
# InvoiceBuilder.renumber_invoice_items(invoice)
# InvoiceBuilder.get_invoice_item(invoice, line_number)

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