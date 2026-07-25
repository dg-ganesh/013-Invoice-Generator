"""
Project : Invoice Generator
Project ID : 013

Invoice Form Coordinator
"""

from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from src.core.calculation.invoice_calculator import InvoiceCalculator
from src.core.invoice.invoice_builder import InvoiceBuilder
from src.core.validation.invoice_validator import InvoiceValidator

from src.models.invoice_model import InvoiceModel

from src.services.document.invoice_deserializer import (
    InvoiceDeserializer,
)
from src.services.document.invoice_serializer import (
    InvoiceSerializer,
)
from src.services.file.json_file_service import (
    JsonFileService,
)

from src.ui.panels.action_panel import ActionPanel
from src.ui.panels.company_panel import CompanyPanel
from src.ui.panels.customer_panel import CustomerPanel
from src.ui.panels.invoice_items_panel import (
    InvoiceItemsPanel,
)
from src.ui.panels.invoice_panel import InvoicePanel
from src.ui.panels.totals_panel import TotalsPanel
from src.services.document.pdf_export_service import (
    PdfExportService,
)

class InvoiceForm(ttk.Frame):
    """
    Main coordinator for the Invoice Generator.

    Responsible only for coordinating UI and
    business services.

    No business rules are implemented here.
    """

    def __init__(
        self,
        parent,
    ) -> None:

        super().__init__(parent)

        self.invoice = InvoiceModel()

        self._create_panels()

        self._layout_panels()

        self._register_callbacks()

        self._initialize_ui()

    # ---------------------------------------------------------
    # Initialization
    # ---------------------------------------------------------

    def _initialize_ui(self) -> None:
        """
        Initializes the application state.
        """

        self._clear_invoice()

    # ---------------------------------------------------------
    # Panel Creation
    # ---------------------------------------------------------

    def _create_panels(self) -> None:

        self.company_panel = CompanyPanel(self)

        self.customer_panel = CustomerPanel(self)

        self.invoice_panel = InvoicePanel(self)

        self.invoice_items_panel = InvoiceItemsPanel(
            self
        )
        print(">>> ITEMS PANEL CREATED <<<")

        self.totals_panel = TotalsPanel(self)

        self.action_panel = ActionPanel(self)
        print(">>> ACTION PANEL CREATED <<<")

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _layout_panels(self) -> None:

        self.columnconfigure(
            0,
            weight=1,
        )

        self.rowconfigure(
            0,
            weight=0,
        )

        self.rowconfigure(
            1,
            weight=0,
        )

        self.rowconfigure(
            2,
            weight=0,
        )

        self.rowconfigure(
            3,
            weight=1,
            minsize=300,
        )

        self.rowconfigure(
            4,
            weight=0,
        )

        self.rowconfigure(
            5,
            weight=0,
        )

        self.company_panel.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=(10, 5),
        )

        self.customer_panel.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10,
            pady=5,
        )

        self.invoice_panel.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=10,
            pady=5,
        )

        self.invoice_items_panel.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=10,
            pady=5,
        )

        self.totals_panel.grid(
            row=4,
            column=0,
            sticky="e",
            padx=10,
            pady=5,
        )

        self.action_panel.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=10,
            pady=10,
        )
        print(">>> ACTION PANEL GRIDDED <<<")
        self.after(
            1000,
            lambda: print(
                "Invoice Items Height:",
                self.invoice_items_panel.winfo_height(),
                "Action Height:",
                self.action_panel.winfo_height(),
            ),
        )

    # ---------------------------------------------------------
    # Callback Registration
    # ---------------------------------------------------------

    def _register_callbacks(self) -> None:

        self.action_panel.set_new_invoice_command(
            self._new_invoice
        )

        self.action_panel.set_calculate_command(
            self._calculate_invoice
        )

        self.action_panel.set_save_command(
            self._save_invoice
        )

        self.action_panel.set_load_command(
            self._load_invoice
        )

        self.action_panel.set_clear_command(
            self._clear_invoice
        )

        self.action_panel.set_export_pdf_command(
            self._export_pdf
        )

    # ---------------------------------------------------------
    # Invoice Operations
    # ---------------------------------------------------------

    def _new_invoice(self) -> None:

        if messagebox.askyesno(
            "New Invoice",
            "Discard current invoice?",
        ):
            self._clear_invoice()

    def _clear_invoice(self) -> None:

        self.invoice = InvoiceModel()

        self.company_panel.set_data(
            self.invoice.company
        )

        self.customer_panel.set_data(
            self.invoice.customer
        )

        self.invoice_panel.set_data(
            self.invoice
        )

        self.invoice_items_panel.clear_items()

        self.totals_panel.clear()

    def _build_invoice(self) -> InvoiceModel:

        company = self.company_panel.get_data()

        customer = self.customer_panel.get_data()

        invoice_information = (
            self.invoice_panel.get_data()
        )

        invoice = InvoiceBuilder.create_invoice(
            company=company,
            customer=customer,
            invoice_number=invoice_information[
                "invoice_number"
            ],
            invoice_date=invoice_information[
                "invoice_date"
            ],
            due_date=invoice_information[
                "due_date"
            ],
            purchase_order_number=invoice_information[
                "purchase_order_number"
            ],
            payment_terms=invoice_information[
                "payment_terms"
            ],
            currency=invoice_information[
                "currency"
            ],
            notes=invoice_information[
                "notes"
            ],
        )

        invoice.invoice_items = (
            self.invoice_items_panel.get_items()
        )

        return invoice

    def _prepare_invoice(self) -> bool:
        """
        Builds, validates and calculates
        the invoice.
        """

        self.invoice = self._build_invoice()

        validation_errors = (
            InvoiceValidator.validate_invoice(
                self.invoice
            )
        )

        if validation_errors:

            messagebox.showerror(
                "Validation Error",
                "\n".join(validation_errors),
            )

            return False

        InvoiceCalculator.calculate_invoice(
            self.invoice
        )

        self.invoice_items_panel.set_items(
            self.invoice.invoice_items
        )

        self.totals_panel.set_totals(
            self.invoice
        )

        return True
    def _calculate_invoice(self) -> None:
        """
        Calculates the invoice totals.
        """

        if not self._prepare_invoice():
            return

        messagebox.showinfo(
            "Calculation Complete",
            "Invoice totals have been calculated.",
        )

    # ---------------------------------------------------------
    # Persistence Helpers
    # ---------------------------------------------------------

    def _get_save_file_name(self) -> str:
        """
        Displays the Save dialog.
        """

        return filedialog.asksaveasfilename(
            title="Save Invoice",
            defaultextension=".json",
            filetypes=[
                (
                    "Invoice Files",
                    "*.json",
                ),
                (
                    "JSON Files",
                    "*.json",
                ),
            ],
        )

    def _get_open_file_name(self) -> str:
        """
        Displays the Open dialog.
        """

        return filedialog.askopenfilename(
            title="Open Invoice",
            filetypes=[
                (
                    "Invoice Files",
                    "*.json",
                ),
                (
                    "JSON Files",
                    "*.json",
                ),
            ],
        )

    def _populate_ui(
        self,
        invoice: InvoiceModel,
    ) -> None:
        """
        Updates every panel from the invoice model.
        """

        self.company_panel.set_data(
            invoice.company
        )

        self.customer_panel.set_data(
            invoice.customer
        )

        self.invoice_panel.set_data(
            invoice
        )

        self.invoice_items_panel.set_items(
            invoice.invoice_items
        )

        self.totals_panel.set_totals(
            invoice
        )

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def _save_invoice(self) -> None:
        """
        Saves the invoice to disk.
        """

        if not self._prepare_invoice():
            return

        file_name = self._get_save_file_name()

        if not file_name:
            return

        try:

            invoice_data = (
                InvoiceSerializer.to_json_data(
                    self.invoice
                )
            )

            JsonFileService.save_json(
                file_name,
                invoice_data,
            )

            messagebox.showinfo(
                "Invoice Saved",
                "Invoice saved successfully.",
            )

        except Exception as error:

            messagebox.showerror(
                "Save Error",
                str(error),
            )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def _load_invoice(self) -> None:
        """
        Loads an invoice from disk.
        """

        file_name = self._get_open_file_name()

        if not file_name:
            return

        try:

            invoice_data = (
                JsonFileService.load_json(
                    file_name
                )
            )

            self.invoice = (
                InvoiceDeserializer.deserialize(
                    invoice_data
                )
            )

            self._populate_ui(
                self.invoice
            )

            messagebox.showinfo(
                "Invoice Loaded",
                "Invoice loaded successfully.",
            )

        except Exception as error:

            messagebox.showerror(
                "Load Error",
                str(error),
            )
    # ---------------------------------------------------------
    # PDF Export
    # ---------------------------------------------------------

    def _export_pdf(self) -> None:
        """
        Exports the invoice as a PDF.
        """

        if not self._prepare_invoice():
            return

        file_name = filedialog.asksaveasfilename(
            title="Export PDF",
            defaultextension=".pdf",
            filetypes=[
                (
                    "PDF Files",
                    "*.pdf",
                ),
            ],
        )

        if not file_name:
            return

        try:



            PdfExportService.export(
                self.invoice,
                file_name,
            )

            messagebox.showinfo(
                "PDF Export",
                "Invoice exported successfully.",
            )

        except Exception as error:

            messagebox.showerror(
                "PDF Export Error",
                str(error),
            )


# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# InvoiceForm(parent)

# ---------------------------------------------------------
# Public Signals
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

# tkinter.ttk
# tkinter.messagebox
# tkinter.filedialog
#
# src.core.calculation.invoice_calculator
# src.core.invoice.invoice_builder
# src.core.validation.invoice_validator
#
# src.models.invoice_model
#
# src.services.document.invoice_serializer
# src.services.document.invoice_deserializer
# src.services.file.json_file_service
#
# src.ui.panels.company_panel
# src.ui.panels.customer_panel
# src.ui.panels.invoice_panel
# src.ui.panels.invoice_items_panel
# src.ui.panels.totals_panel
# src.ui.panels.action_panel
