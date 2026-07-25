"""
Project : Invoice Generator
Project ID : 013

Invoice Items Panel
"""

import tkinter as tk


from tkinter import ttk

from src.models.invoice_item_model import (
    InvoiceItemModel,
)

from src.ui.dialogs.invoice_item_dialog import (
    InvoiceItemDialog,
)


class InvoiceItemsPanel(ttk.LabelFrame):
    """
    Displays and manages invoice items.
    """

    COLUMN_DEFINITIONS = (

        (
            "line_number",
            "#",
            60,
        ),

        (
            "description",
            "Description",
            320,
        ),

        (
            "quantity",
            "Qty",
            80,
        ),

        (
            "unit_price",
            "Unit Price",
            120,
        ),

        (
            "tax_percentage",
            "Tax %",
            80,
        ),

        (
            "line_total",
            "Line Total",
            120,
        ),

    )

    def __init__(
        self,
        parent,
    ) -> None:

        super().__init__(
            parent,
            text="Invoice Items",
            padding=10,
        )

        self.invoice_items: list[
            InvoiceItemModel
        ] = []

        self._create_widgets()

        self._configure_layout()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self.tree = ttk.Treeview(
            self,
            columns=[
                column[0]
                for column
                in self.COLUMN_DEFINITIONS
            ],
            show="headings",
            height=8,
            selectmode="browse",
        )

        for (
            column_name,
            heading,
            width,
        ) in self.COLUMN_DEFINITIONS:

            self.tree.heading(
                column_name,
                text=heading,
            )

            self.tree.column(
                column_name,
                width=width,
                anchor="center",
                stretch=True,
            )

        self.vertical_scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview,
        )

        self.tree.configure(
            yscrollcommand=(
                self.vertical_scrollbar.set
            ),
        )

        self.button_frame = ttk.Frame(
            self,
        )

        self.add_button = ttk.Button(
            self.button_frame,
            text="Add Item",
        )

        self.edit_button = ttk.Button(
            self.button_frame,
            text="Edit Item",
        )

        self.remove_button = ttk.Button(
            self.button_frame,
            text="Remove Item",
        )

        self.clear_button = ttk.Button(
            self.button_frame,
            text="Clear Items",
        )

        #
        # Button Commands
        #

        self.add_button.configure(
            command=self._add_item,
        )

        self.edit_button.configure(
            command=self._edit_item,
        )

        self.remove_button.configure(
            command=self._remove_item,
        )

        self.clear_button.configure(
            command=self.clear_items,
        )

        self.tree.bind(
            "<Double-1>",
            self._double_click,
        )


    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _configure_layout(
        self,
    ) -> None:
        """
        Configures the panel layout.
        """

        self.rowconfigure(
            0,
            weight=1,
            minsize=250,
        )

        self.rowconfigure(
            1,
            weight=0,
        )

        self.columnconfigure(
            0,
            weight=1,
        )

        self.columnconfigure(
            1,
            weight=0,
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 5),
            pady=(0, 5),
        )

        self.vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
            pady=(0, 5),
        )

        self.button_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="e",
            pady=(5, 0),
        )

        self.add_button.pack(
            side="left",
            padx=5,
        )

        self.edit_button.pack(
            side="left",
            padx=5,
        )

        self.remove_button.pack(
            side="left",
            padx=5,
        )

        self.clear_button.pack(
            side="left",
            padx=5,
        )

    # ---------------------------------------------------------
    # Tree Refresh
    # ---------------------------------------------------------

    def _refresh_tree(
        self,
    ) -> None:
        """
        Refreshes the TreeView.
        """

        self.tree.delete(
            *self.tree.get_children()
        )

        for item in self.invoice_items:

            self.tree.insert(
                "",
                "end",
                iid=str(item.line_number),
                values=(
                    item.line_number,
                    item.description,
                    f"{item.quantity:.2f}",
                    f"{item.unit_price:.2f}",
                    f"{item.tax_percentage:.2f}",
                    f"{item.line_total:.2f}",
                ),
            )

    # ---------------------------------------------------------
    # Button Events
    # ---------------------------------------------------------

    def _add_item(
        self,
    ) -> None:
        """
        Adds a new invoice item.
        """

        dialog = InvoiceItemDialog(
            self,
        )

        item = dialog.show()

        if item is None:
            return

        item.line_number = (
            len(self.invoice_items) + 1
        )

        self.add_item(
            item,
        )

    def _edit_item(
        self,
    ) -> None:
        """
        Edits the selected invoice item.
        """

        selection = self.tree.selection()

        if not selection:
            return

        line_number = int(
            selection[0]
        )

        for index, item in enumerate(
            self.invoice_items
        ):

            if (
                item.line_number
                != line_number
            ):
                continue

            dialog = InvoiceItemDialog(
                self,
                item,
            )

            updated_item = dialog.show()

            if updated_item is not None:

                self.update_item(
                    index,
                    updated_item,
                )

            return

    def _remove_item(
        self,
    ) -> None:
        """
        Removes the selected invoice item.
        """

        self.remove_selected_item()

    def _double_click(
        self,
        event,
    ) -> None:
        """
        Double-click edits the selected item.
        """

        self._edit_item()

        
    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def get_items(
        self,
    ) -> list[InvoiceItemModel]:
        """
        Returns all invoice items.
        """

        return list(
            self.invoice_items
        )

    def set_items(
        self,
        items: list[InvoiceItemModel],
    ) -> None:
        """
        Replaces all invoice items.
        """

        self.invoice_items = list(
            items
        )

        self._refresh_tree()

    def add_item(
        self,
        item: InvoiceItemModel,
    ) -> None:
        """
        Adds an invoice item.
        """

        item.line_number = (
            len(self.invoice_items) + 1
        )

        self.invoice_items.append(
            item
        )

        self._refresh_tree()

    def update_item(
        self,
        index: int,
        item: InvoiceItemModel,
    ) -> None:
        """
        Updates an invoice item.
        """

        self.invoice_items[index] = item

        item.line_number = (
            index + 1
        )

        self._refresh_tree()

    def remove_selected_item(
        self,
    ) -> InvoiceItemModel | None:
        """
        Removes the selected invoice item.
        """

        selection = self.tree.selection()

        if not selection:
            return None

        line_number = int(
            selection[0]
        )

        for index, item in enumerate(
            self.invoice_items
        ):

            if (
                item.line_number
                == line_number
            ):

                removed_item = (
                    self.invoice_items.pop(
                        index
                    )
                )

                #
                # Renumber remaining items
                #

                for number, invoice_item in enumerate(
                    self.invoice_items,
                    start=1,
                ):

                    invoice_item.line_number = (
                        number
                    )

                self._refresh_tree()

                return removed_item

        return None

    def clear_items(
        self,
    ) -> None:
        """
        Clears every invoice item.
        """

        self.invoice_items.clear()

        self._refresh_tree()
# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# InvoiceItemsPanel(parent)
# get_items()
# set_items(items)
# add_item(item)
# update_item(index, item)
# remove_selected_item()
# clear_items()

# ---------------------------------------------------------
# Public Signals
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

# tkinter.ttk
# src.models.invoice_item_model
# src.ui.dialogs.invoice_item_dialog