"""
Project : Invoice Generator
Project ID : 013

Invoice Item Dialog
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from src.models.invoice_item_model import InvoiceItemModel


class InvoiceItemDialog(tk.Toplevel):
    """
    Dialog used for creating and editing
    invoice items.
    """

    def __init__(
        self,
        parent,
        item: InvoiceItemModel | None = None,
    ) -> None:

        super().__init__(parent)

        self.title("Invoice Item")

        self.resizable(
            False,
            False,
        )

        self.transient(parent)

        self.grab_set()

        self.result = None

        self.item = (
            item
            if item is not None
            else InvoiceItemModel()
        )

        self._create_variables()

        self._create_widgets()

        self._layout_widgets()

        self._load_item()

        self.protocol(
            "WM_DELETE_WINDOW",
            self._cancel,
        )

    # ---------------------------------------------------------
    # Variables
    # ---------------------------------------------------------

    def _create_variables(self) -> None:

        self.description_var = tk.StringVar()

        self.quantity_var = tk.StringVar()

        self.unit_price_var = tk.StringVar()

        self.tax_percentage_var = tk.StringVar()

        self.discount_var = tk.StringVar()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self.main_frame = ttk.Frame(
            self,
            padding=15,
        )

        self.description_label = ttk.Label(
            self.main_frame,
            text="Description",
        )

        self.description_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.description_var,
            width=45,
        )

        self.quantity_label = ttk.Label(
            self.main_frame,
            text="Quantity",
        )

        self.quantity_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.quantity_var,
        )

        self.unit_price_label = ttk.Label(
            self.main_frame,
            text="Unit Price",
        )

        self.unit_price_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.unit_price_var,
        )

        self.tax_label = ttk.Label(
            self.main_frame,
            text="Tax %",
        )

        self.tax_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.tax_percentage_var,
        )

        self.discount_label = ttk.Label(
            self.main_frame,
            text="Discount",
        )

        self.discount_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.discount_var,
        )

        self.button_frame = ttk.Frame(
            self.main_frame,
        )

        self.ok_button = ttk.Button(
            self.button_frame,
            text="OK",
            command=self._ok,
            width=12,
        )

        self.cancel_button = ttk.Button(
            self.button_frame,
            text="Cancel",
            command=self._cancel,
            width=12,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _layout_widgets(self) -> None:

        self.main_frame.pack(
            fill="both",
            expand=True,
        )

        row = 0

        for label, widget in [

            (
                self.description_label,
                self.description_entry,
            ),

            (
                self.quantity_label,
                self.quantity_entry,
            ),

            (
                self.unit_price_label,
                self.unit_price_entry,
            ),

            (
                self.tax_label,
                self.tax_entry,
            ),

            (
                self.discount_label,
                self.discount_entry,
            ),

        ]:

            label.grid(
                row=row,
                column=0,
                sticky="w",
                pady=5,
            )

            widget.grid(
                row=row,
                column=1,
                sticky="ew",
                padx=(10, 0),
                pady=5,
            )

            row += 1

        self.main_frame.columnconfigure(
            1,
            weight=1,
        )

        self.button_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            pady=(15, 0),
        )

        self.ok_button.pack(
            side="left",
            padx=5,
        )

        self.cancel_button.pack(
            side="left",
            padx=5,
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def _load_item(self) -> None:

        self.description_var.set(
            self.item.description
        )

        self.quantity_var.set(
            str(self.item.quantity)
        )

        self.unit_price_var.set(
            str(self.item.unit_price)
        )

        self.tax_percentage_var.set(
            str(self.item.tax_percentage)
        )

        self.discount_var.set(
            str(self.item.discount_percentage)
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def _validate(self) -> bool:

        if not self.description_var.get().strip():

            messagebox.showerror(
                "Validation Error",
                "Description is required.",
            )

            return False

        try:

            float(self.quantity_var.get())

            float(self.unit_price_var.get())

            float(self.tax_percentage_var.get())

            float(self.discount_var.get())

        except ValueError:

            messagebox.showerror(
                "Validation Error",
                "Numeric values are invalid.",
            )

            return False

        return True

    # ---------------------------------------------------------
    # Buttons
    # ---------------------------------------------------------

    def _ok(self) -> None:

        if not self._validate():
            return

        self.item.description = (
            self.description_var.get().strip()
        )

        self.item.quantity = float(
            self.quantity_var.get()
        )

        self.item.unit_price = float(
            self.unit_price_var.get()
        )

        self.item.tax_percentage = float(
            self.tax_percentage_var.get()
        )

        self.item.discount_percentage = float(
            self.discount_var.get()
        )

        self.result = self.item

        self.destroy()

    def _cancel(self) -> None:

        self.result = None

        self.destroy()

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def show(
        self,
    ) -> InvoiceItemModel | None:
        """
        Displays the dialog.
        """

        self.wait_window()

        return self.result


# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# InvoiceItemDialog(parent)
# show()

# ---------------------------------------------------------
# Public Signals
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

# tkinter
# tkinter.ttk
# tkinter.messagebox
# src.models.invoice_item_model