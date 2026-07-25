"""
Project : Invoice Generator
Project ID : 013

Invoice Calculator
"""

from src.models.invoice_model import InvoiceModel
from src.models.invoice_item_model import InvoiceItemModel


class InvoiceCalculator:
    """
    Performs all invoice calculations.

    This module contains the business rules for calculating
    invoice totals. It does not interact with the UI.
    """

    @staticmethod
    def calculate_invoice(invoice: InvoiceModel) -> InvoiceModel:
        """
        Calculates all invoice totals.

        Parameters
        ----------
        invoice : InvoiceModel

        Returns
        -------
        InvoiceModel
        """

        subtotal = 0.0
        total_discount = 0.0
        total_tax = 0.0

        for item in invoice.invoice_items:
            InvoiceCalculator.calculate_invoice_item(item)

            subtotal += item.line_subtotal
            total_discount += item.discount_amount
            total_tax += item.tax_amount

        invoice.subtotal = InvoiceCalculator._round(subtotal)
        invoice.total_discount = InvoiceCalculator._round(total_discount)
        invoice.total_tax = InvoiceCalculator._round(total_tax)

        invoice.grand_total = InvoiceCalculator._round(
            invoice.subtotal
            - invoice.total_discount
            + invoice.total_tax
        )

        return invoice

    @staticmethod
    def calculate_invoice_item(item: InvoiceItemModel) -> InvoiceItemModel:
        """
        Calculates all values for a single invoice item.
        """

        item.line_subtotal = InvoiceCalculator._round(
            item.quantity * item.unit_price
        )

        item.discount_amount = InvoiceCalculator._round(
            item.line_subtotal
            * (item.discount_percentage / 100.0)
        )

        taxable_amount = (
            item.line_subtotal
            - item.discount_amount
        )

        item.tax_amount = InvoiceCalculator._round(
            taxable_amount
            * (item.tax_percentage / 100.0)
        )

        item.line_total = InvoiceCalculator._round(
            taxable_amount
            + item.tax_amount
        )

        return item

    @staticmethod
    def calculate_subtotal(
        invoice_items: list[InvoiceItemModel],
    ) -> float:
        """
        Calculates the subtotal.
        """

        subtotal = sum(
            item.line_subtotal
            for item in invoice_items
        )

        return InvoiceCalculator._round(subtotal)

    @staticmethod
    def calculate_total_discount(
        invoice_items: list[InvoiceItemModel],
    ) -> float:
        """
        Calculates the total discount.
        """

        total = sum(
            item.discount_amount
            for item in invoice_items
        )

        return InvoiceCalculator._round(total)

    @staticmethod
    def calculate_total_tax(
        invoice_items: list[InvoiceItemModel],
    ) -> float:
        """
        Calculates the total tax.
        """

        total = sum(
            item.tax_amount
            for item in invoice_items
        )

        return InvoiceCalculator._round(total)

    @staticmethod
    def calculate_grand_total(
        subtotal: float,
        total_discount: float,
        total_tax: float,
    ) -> float:
        """
        Calculates the invoice grand total.
        """

        return InvoiceCalculator._round(
            subtotal
            - total_discount
            + total_tax
        )

    @staticmethod
    def _round(value: float) -> float:
        """
        Standard rounding for monetary values.
        """

        return round(value, 2)


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceCalculator.calculate_invoice(invoice)
# InvoiceCalculator.calculate_invoice_item(item)
# InvoiceCalculator.calculate_subtotal(invoice_items)
# InvoiceCalculator.calculate_total_discount(invoice_items)
# InvoiceCalculator.calculate_total_tax(invoice_items)
# InvoiceCalculator.calculate_grand_total(
#     subtotal,
#     total_discount,
#     total_tax
# )

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# src.models.invoice_model
# src.models.invoice_item_model