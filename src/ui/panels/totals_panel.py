"""
Project : Invoice Generator
Project ID : 013

Totals Panel
"""

import tkinter as tk
from tkinter import ttk

from src.models.invoice_model import InvoiceModel


class TotalsPanel(ttk.LabelFrame):
    """
    Displays the calculated invoice totals.

    This panel is display-only.
    Business calculations are performed by InvoiceCalculator.
    """

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            text="Invoice Totals",
            padding=10,
        )

        self._create_variables()
        self._create_widgets()
        self._configure_layout()

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _create_variables(self) -> None:

        self.subtotal_var = tk.StringVar(value="0.00")
        self.discount_var = tk.StringVar(value="0.00")
        self.tax_var = tk.StringVar(value="0.00")
        self.grand_total_var = tk.StringVar(value="0.00")

    def _create_widgets(self) -> None:

        self.subtotal_label = ttk.Label(
            self,
            text="Subtotal"
        )

        self.subtotal_entry = ttk.Entry(
            self,
            textvariable=self.subtotal_var,
            justify="right",
            state="readonly",
            width=18,
        )

        self.discount_label = ttk.Label(
            self,
            text="Discount"
        )

        self.discount_entry = ttk.Entry(
            self,
            textvariable=self.discount_var,
            justify="right",
            state="readonly",
            width=18,
        )

        self.tax_label = ttk.Label(
            self,
            text="Tax"
        )

        self.tax_entry = ttk.Entry(
            self,
            textvariable=self.tax_var,
            justify="right",
            state="readonly",
            width=18,
        )

        self.grand_total_label = ttk.Label(
            self,
            text="Grand Total"
        )

        self.grand_total_entry = ttk.Entry(
            self,
            textvariable=self.grand_total_var,
            justify="right",
            state="readonly",
            width=18,
        )

    def _configure_layout(self) -> None:

        self.columnconfigure(1, weight=1)

        self.subtotal_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )

        self.subtotal_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=4,
            sticky="e",
        )

        self.discount_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )

        self.discount_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=4,
            sticky="e",
        )

        self.tax_label.grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )

        self.tax_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=4,
            sticky="e",
        )

        self.grand_total_label.grid(
            row=3,
            column=0,
            padx=5,
            pady=6,
            sticky="w",
        )

        self.grand_total_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=6,
            sticky="e",
        )

    @staticmethod
    def _format_amount(value: float) -> str:
        """
        Formats monetary values.
        """

        return f"{value:,.2f}"

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def clear(self) -> None:
        """
        Clears all displayed totals.
        """

        self.subtotal_var.set("0.00")
        self.discount_var.set("0.00")
        self.tax_var.set("0.00")
        self.grand_total_var.set("0.00")

    def set_totals(
        self,
        invoice: InvoiceModel,
    ) -> None:
        """
        Displays totals from an InvoiceModel.
        """

        self.subtotal_var.set(
            self._format_amount(invoice.subtotal)
        )

        self.discount_var.set(
            self._format_amount(invoice.total_discount)
        )

        self.tax_var.set(
            self._format_amount(invoice.total_tax)
        )

        self.grand_total_var.set(
            self._format_amount(invoice.grand_total)
        )

    def get_totals(self) -> dict:
        """
        Returns the currently displayed totals.
        """

        return {
            "subtotal": self.subtotal_var.get(),
            "discount": self.discount_var.get(),
            "tax": self.tax_var.get(),
            "grand_total": self.grand_total_var.get(),
        }


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# TotalsPanel(parent)
# clear()
# set_totals(invoice)
# get_totals()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# tkinter
# tkinter.ttk
# src.models.invoice_model