"""
Project : Invoice Generator
Project ID : 013

Invoice Validator
"""

from src.models.company_model import CompanyModel
from src.models.customer_model import CustomerModel
from src.models.invoice_item_model import InvoiceItemModel
from src.models.invoice_model import InvoiceModel


class InvoiceValidator:
    """
    Validates invoice data before business processing.

    This module contains validation rules only.
    It performs no calculations and has no UI dependencies.
    """

    @staticmethod
    def validate_invoice(invoice: InvoiceModel) -> list[str]:
        """
        Validates an entire invoice.

        Returns
        -------
        list[str]
            Collection of validation error messages.
        """

        errors: list[str] = []

        errors.extend(
            InvoiceValidator.validate_company(
                invoice.company
            )
        )

        errors.extend(
            InvoiceValidator.validate_customer(
                invoice.customer
            )
        )

        errors.extend(
            InvoiceValidator.validate_invoice_information(
                invoice
            )
        )

        errors.extend(
            InvoiceValidator.validate_invoice_items(
                invoice.invoice_items
            )
        )

        return errors

    @staticmethod
    def validate_company(
        company: CompanyModel,
    ) -> list[str]:
        """
        Validates company information.
        """

        errors: list[str] = []

        if not company.company_name.strip():
            errors.append("Company name is required.")

        return errors

    @staticmethod
    def validate_customer(
        customer: CustomerModel,
    ) -> list[str]:
        """
        Validates customer information.
        """

        errors: list[str] = []

        if not customer.customer_name.strip():
            errors.append("Customer name is required.")

        return errors

    @staticmethod
    def validate_invoice_information(
        invoice: InvoiceModel,
    ) -> list[str]:
        """
        Validates invoice header information.
        """

        errors: list[str] = []

        if not invoice.invoice_number.strip():
            errors.append("Invoice number is required.")

        if not invoice.invoice_date.strip():
            errors.append("Invoice date is required.")

        return errors

    @staticmethod
    def validate_invoice_items(
        items: list[InvoiceItemModel],
    ) -> list[str]:
        """
        Validates all invoice items.
        """

        errors: list[str] = []

        if not items:
            errors.append(
                "At least one invoice item is required."
            )
            return errors

        for index, item in enumerate(items, start=1):
            errors.extend(
                InvoiceValidator.validate_invoice_item(
                    item,
                    index,
                )
            )

        return errors

    @staticmethod
    def validate_invoice_item(
        item: InvoiceItemModel,
        item_number: int,
    ) -> list[str]:
        """
        Validates a single invoice item.
        """

        errors: list[str] = []

        prefix = f"Item {item_number}"

        if not item.description.strip():
            errors.append(
                f"{prefix}: Description is required."
            )

        if item.quantity <= 0:
            errors.append(
                f"{prefix}: Quantity must be greater than zero."
            )

        if item.unit_price < 0:
            errors.append(
                f"{prefix}: Unit price cannot be negative."
            )

        if item.tax_percentage < 0:
            errors.append(
                f"{prefix}: Tax percentage cannot be negative."
            )

        if item.discount_percentage < 0:
            errors.append(
                f"{prefix}: Discount percentage cannot be negative."
            )

        return errors


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoiceValidator.validate_invoice(invoice)
# InvoiceValidator.validate_company(company)
# InvoiceValidator.validate_customer(customer)
# InvoiceValidator.validate_invoice_information(invoice)
# InvoiceValidator.validate_invoice_items(items)
# InvoiceValidator.validate_invoice_item(item, item_number)

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