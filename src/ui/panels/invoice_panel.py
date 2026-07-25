"""
Project : Invoice Generator
Project ID : 013

Invoice Panel
"""

from tkinter import ttk

from src.models.invoice_model import InvoiceModel


class InvoicePanel(ttk.LabelFrame):
    """
    Invoice header information panel.
    """

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            text="Invoice Information",
            padding=10,
        )

        self._create_widgets()
        self._configure_layout()

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _create_widgets(self) -> None:

        self.invoice_number_label = ttk.Label(
            self,
            text="Invoice Number"
        )
        self.invoice_number_entry = ttk.Entry(
            self,
            width=20,
        )

        self.invoice_date_label = ttk.Label(
            self,
            text="Invoice Date"
        )
        self.invoice_date_entry = ttk.Entry(
            self,
            width=20,
        )

        self.due_date_label = ttk.Label(
            self,
            text="Due Date"
        )
        self.due_date_entry = ttk.Entry(
            self,
            width=20,
        )

        self.purchase_order_label = ttk.Label(
            self,
            text="PO Number"
        )
        self.purchase_order_entry = ttk.Entry(
            self,
            width=25,
        )

        self.payment_terms_label = ttk.Label(
            self,
            text="Payment Terms"
        )
        self.payment_terms_entry = ttk.Entry(
            self,
            width=25,
        )

        self.currency_label = ttk.Label(
            self,
            text="Currency"
        )

        self.currency_combobox = ttk.Combobox(
            self,
            width=12,
            state="readonly",
            values=(
                "USD",
                "EUR",
                "GBP",
                "INR",
                "AUD",
                "CAD",
            ),
        )

        self.currency_combobox.set("USD")

        self.notes_label = ttk.Label(
            self,
            text="Notes"
        )

        self.notes_text = ttk.Entry(
            self,
            width=70,
        )

    def _configure_layout(self) -> None:

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.invoice_number_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.invoice_number_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.invoice_date_label.grid(
            row=0,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.invoice_date_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.due_date_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.due_date_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.purchase_order_label.grid(
            row=1,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.purchase_order_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.payment_terms_label.grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.payment_terms_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.currency_label.grid(
            row=2,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.currency_combobox.grid(
            row=2,
            column=3,
            padx=5,
            pady=4,
            sticky="w",
        )

        self.notes_label.grid(
            row=3,
            column=0,
            padx=5,
            pady=4,
            sticky="nw",
        )
        self.notes_text.grid(
            row=3,
            column=1,
            columnspan=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def get_data(self) -> dict:
        """
        Returns the invoice header information.
        """

        return {
            "invoice_number": self.invoice_number_entry.get().strip(),
            "invoice_date": self.invoice_date_entry.get().strip(),
            "due_date": self.due_date_entry.get().strip(),
            "purchase_order_number":
                self.purchase_order_entry.get().strip(),
            "payment_terms":
                self.payment_terms_entry.get().strip(),
            "currency":
                self.currency_combobox.get().strip(),
            "notes":
                self.notes_text.get().strip(),
        }

    def set_data(
        self,
        invoice: InvoiceModel,
    ) -> None:
        """
        Populates the panel from an InvoiceModel.
        """

        self.invoice_number_entry.delete(0, "end")
        self.invoice_number_entry.insert(
            0,
            invoice.invoice_number,
        )

        self.invoice_date_entry.delete(0, "end")
        self.invoice_date_entry.insert(
            0,
            invoice.invoice_date,
        )

        self.due_date_entry.delete(0, "end")
        self.due_date_entry.insert(
            0,
            invoice.due_date,
        )

        self.purchase_order_entry.delete(0, "end")
        self.purchase_order_entry.insert(
            0,
            invoice.purchase_order_number,
        )

        self.payment_terms_entry.delete(0, "end")
        self.payment_terms_entry.insert(
            0,
            invoice.payment_terms,
        )

        self.currency_combobox.set(
            invoice.currency
        )

        self.notes_text.delete(0, "end")
        self.notes_text.insert(
            0,
            invoice.notes,
        )


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# InvoicePanel(parent)
# get_data()
# set_data(invoice)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# tkinter.ttk
# src.models.invoice_model