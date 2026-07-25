"""
Project : Invoice Generator
Project ID : 013

Action Panel
"""

from collections.abc import Callable
from tkinter import ttk


class ActionPanel(ttk.LabelFrame):
    """
    Hosts the primary application action buttons.

    This panel exposes registration methods so the
    coordinator can attach business logic without the
    panel depending on application services.
    """

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            text="Actions",
            padding=10,
        )

        self._create_widgets()
        self._configure_layout()

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _create_widgets(self) -> None:

        self.new_button = ttk.Button(
            self,
            text="New Invoice",
        )

        self.calculate_button = ttk.Button(
            self,
            text="Calculate",
        )

        self.save_button = ttk.Button(
            self,
            text="Save",
        )

        self.load_button = ttk.Button(
            self,
            text="Load",
        )

        self.export_pdf_button = ttk.Button(
            self,
            text="Export PDF",
        )

        self.clear_button = ttk.Button(
            self,
            text="Clear",
        )

    def _configure_layout(self) -> None:

        self.columnconfigure(6, weight=1)

        self.new_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        self.calculate_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

        self.save_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
        )

        self.load_button.grid(
            row=0,
            column=3,
            padx=5,
            pady=5,
        )

        self.export_pdf_button.grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
        )

        self.clear_button.grid(
            row=0,
            column=5,
            padx=5,
            pady=5,
        )

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def set_new_invoice_command(
        self,
        command: Callable,
    ) -> None:
        self.new_button.configure(command=command)

    def set_calculate_command(
        self,
        command: Callable,
    ) -> None:
        self.calculate_button.configure(command=command)

    def set_save_command(
        self,
        command: Callable,
    ) -> None:
        self.save_button.configure(command=command)

    def set_load_command(
        self,
        command: Callable,
    ) -> None:
        self.load_button.configure(command=command)

    def set_export_pdf_command(
        self,
        command: Callable,
    ) -> None:
        self.export_pdf_button.configure(command=command)

    def set_clear_command(
        self,
        command: Callable,
    ) -> None:
        self.clear_button.configure(command=command)

    def enable_save(
        self,
        enabled: bool,
    ) -> None:
        state = "normal" if enabled else "disabled"
        self.save_button.configure(state=state)

    def enable_load(
        self,
        enabled: bool,
    ) -> None:
        state = "normal" if enabled else "disabled"
        self.load_button.configure(state=state)

    def enable_export_pdf(
        self,
        enabled: bool,
    ) -> None:
        state = "normal" if enabled else "disabled"
        self.export_pdf_button.configure(state=state)


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# ActionPanel(parent)
# set_new_invoice_command(command)
# set_calculate_command(command)
# set_save_command(command)
# set_load_command(command)
# set_export_pdf_command(command)
# set_clear_command(command)
# enable_save(enabled)
# enable_load(enabled)
# enable_export_pdf(enabled)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# tkinter.ttk
# collections.abc.Callable