"""
Project : Invoice Generator
Project ID : 013

PDF Export Service
"""

from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
)

from src.models.invoice_model import (
    InvoiceModel,
)

from src.services.document.pdf_styles import (
    PdfStyles,
)


class PdfExportService:
    """
    Generates professional PDF invoices.
    """

    # ---------------------------------------------------------
    # Public Export
    # ---------------------------------------------------------

    @staticmethod
    def export(
        invoice: InvoiceModel,
        file_path: str,
    ) -> None:
        """
        Exports an invoice to PDF.
        """

        document = SimpleDocTemplate(
            file_path,
            pagesize=A4,
            leftMargin=PdfStyles.PAGE_MARGIN,
            rightMargin=PdfStyles.PAGE_MARGIN,
            topMargin=PdfStyles.PAGE_MARGIN,
            bottomMargin=PdfStyles.PAGE_MARGIN,
        )

        elements = []

        PdfExportService._add_company_section(
            elements,
            invoice,
        )

        PdfExportService._add_invoice_heading(
            elements,
        )

        PdfExportService._add_customer_section(
            elements,
            invoice,
        )

        PdfExportService._add_invoice_information(
            elements,
            invoice,
        )

        PdfExportService._add_items_table(
            elements,
            invoice,
        )

        PdfExportService._add_totals(
            elements,
            invoice,
        )

        PdfExportService._add_notes(
            elements,
            invoice,
        )

        PdfExportService._add_footer(
            elements,
        )

        document.build(
            elements,
        )

    # ---------------------------------------------------------
    # Company Information
    # ---------------------------------------------------------

    @staticmethod
    def _add_company_section(
        elements,
        invoice,
    ) -> None:
        """
        Adds company information.
        """

        company = invoice.company

        elements.append(

            Paragraph(
                company.company_name,
                PdfStyles.TITLE,
            )

        )

        if company.address_line_1:

            elements.append(

                Paragraph(
                    company.address_line_1,
                    PdfStyles.NORMAL,
                )

            )

        if company.address_line_2:

            elements.append(

                Paragraph(
                    company.address_line_2,
                    PdfStyles.NORMAL,
                )

            )

        city_line = ", ".join(

            value

            for value in [

                company.city,
                company.state,

            ]

            if value

        )

        if company.postal_code:

            city_line += (
                f" - {company.postal_code}"
            )

        if city_line:

            elements.append(

                Paragraph(
                    city_line,
                    PdfStyles.NORMAL,
                )

            )

        if company.country:

            elements.append(

                Paragraph(
                    company.country,
                    PdfStyles.NORMAL,
                )

            )

        if company.phone_number:

            elements.append(

                Paragraph(
                    f"Phone : {company.phone_number}",
                    PdfStyles.NORMAL,
                )

            )

        if company.email_address:

            elements.append(

                Paragraph(
                    f"Email : {company.email_address}",
                    PdfStyles.NORMAL,
                )

            )

        if company.website:

            elements.append(

                Paragraph(
                    company.website,
                    PdfStyles.NORMAL,
                )

            )

        if company.tax_registration_number:

            elements.append(

                Paragraph(
                    f"GST / VAT : {company.tax_registration_number}",
                    PdfStyles.NORMAL,
                )

            )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Invoice Heading
    # ---------------------------------------------------------

    @staticmethod
    def _add_invoice_heading(
        elements,
    ) -> None:
        """
        Adds invoice heading.
        """

        elements.append(

            Paragraph(
                "TAX INVOICE",
                PdfStyles.TITLE,
            )

        )

        elements.append(

            Spacer(
                1,
                15,
            )

        )

    # ---------------------------------------------------------
    # Customer Information
    # ---------------------------------------------------------

    @staticmethod
    def _add_customer_section(
        elements,
        invoice,
    ) -> None:
        """
        Adds customer information.
        """

        customer = invoice.customer

        elements.append(

            Paragraph(
                "<b>Bill To</b>",
                PdfStyles.SECTION_HEADING,
            )

        )

        elements.append(

            Paragraph(
                customer.customer_name,
                PdfStyles.NORMAL,
            )

        )

        if customer.address_line_1:

            elements.append(

                Paragraph(
                    customer.address_line_1,
                    PdfStyles.NORMAL,
                )

            )

        if customer.address_line_2:

            elements.append(

                Paragraph(
                    customer.address_line_2,
                    PdfStyles.NORMAL,
                )

            )

        city_line = ", ".join(

            value

            for value in [

                customer.city,
                customer.state,

            ]

            if value

        )

        if customer.postal_code:

            city_line += (
                f" - {customer.postal_code}"
            )

        if city_line:

            elements.append(

                Paragraph(
                    city_line,
                    PdfStyles.NORMAL,
                )

            )

        if customer.country:

            elements.append(

                Paragraph(
                    customer.country,
                    PdfStyles.NORMAL,
                )

            )

        if customer.phone_number:

            elements.append(

                Paragraph(
                    f"Phone : {customer.phone_number}",
                    PdfStyles.NORMAL,
                )

            )

        if customer.email_address:

            elements.append(

                Paragraph(
                    f"Email : {customer.email_address}",
                    PdfStyles.NORMAL,
                )

            )

        if customer.customer_reference:

            elements.append(

                Paragraph(
                    f"Customer Ref : {customer.customer_reference}",
                    PdfStyles.NORMAL,
                )

            )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Invoice Information
    # ---------------------------------------------------------

    @staticmethod
    def _add_invoice_information(
        elements,
        invoice,
    ) -> None:
        """
        Adds invoice information.
        """

        data = [

            [
                "Invoice Number",
                invoice.invoice_number,
            ],

            [
                "Invoice Date",
                str(invoice.invoice_date),
            ],

            [
                "Due Date",
                str(invoice.due_date),
            ],

            [
                "Payment Terms",
                invoice.payment_terms,
            ],

            [
                "Currency",
                invoice.currency,
            ],

        ]

        table = Table(
            data,
            colWidths=[
                160,
                320,
            ],
        )

        table.setStyle(
            PdfStyles.INFO_TABLE
        )

        elements.append(
            table,
        )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Invoice Items
    # ---------------------------------------------------------

    @staticmethod
    def _add_items_table(
        elements,
        invoice,
    ) -> None:
        """
        Adds invoice items table.
        """

        table_data = [

            [
                "#",
                "Description",
                "Qty",
                "Rate",
                "Tax",
                "Amount",
            ]

        ]

        for item in invoice.invoice_items:

            table_data.append(

                [

                    str(
                        item.line_number
                    ),

                    item.description,

                    f"{item.quantity:.2f}",

                    f"{item.unit_price:.2f}",

                    f"{item.tax_amount:.2f}",

                    f"{item.line_total:.2f}",

                ]

            )

        table = Table(

            table_data,

            colWidths=[
                35,
                220,
                55,
                70,
                70,
                80,
            ],

        )

        table.setStyle(
            PdfStyles.ITEM_TABLE,
        )

        elements.append(
            table,
        )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Invoice Totals
    # ---------------------------------------------------------

    @staticmethod
    def _add_totals(
        elements,
        invoice,
    ) -> None:
        """
        Adds invoice totals.
        """

        totals = [

            [

                "Subtotal",

                f"{invoice.subtotal:.2f}",

            ],

            [

                "Discount",

                f"{invoice.total_discount:.2f}",

            ],

            [

                "Tax",

                f"{invoice.total_tax:.2f}",

            ],

            [

                "Grand Total",

                f"{invoice.grand_total:.2f}",

            ],

        ]

        table = Table(

            totals,

            colWidths=[
                360,
                120,
            ],

        )

        table.setStyle(
            PdfStyles.TOTALS_TABLE,
        )

        elements.append(
            table,
        )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Notes
    # ---------------------------------------------------------

    @staticmethod
    def _add_notes(
        elements,
        invoice,
    ) -> None:
        """
        Adds invoice notes.
        """

        if not invoice.notes:
            return

        elements.append(

            Paragraph(
                "<b>Notes</b>",
                PdfStyles.SECTION_HEADING,
            )

        )

        elements.append(

            Paragraph(
                invoice.notes,
                PdfStyles.NORMAL,
            )

        )

        elements.append(

            Spacer(
                1,
                20,
            )

        )

    # ---------------------------------------------------------
    # Footer
    # ---------------------------------------------------------

    @staticmethod
    def _add_footer(
        elements,
    ) -> None:
        """
        Adds footer.
        """

        elements.append(

            Paragraph(
                "Thank you for your business.",
                PdfStyles.FOOTER,
            )

        )


# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# PdfExportService.export(
#     invoice,
#     file_path,
# )

# ---------------------------------------------------------
# Public Signals
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

# reportlab
# reportlab.platypus
# reportlab.lib.pagesizes
#
# src.models.invoice_model
# src.services.document.pdf_styles