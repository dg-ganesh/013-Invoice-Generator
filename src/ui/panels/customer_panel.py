"""
Project : Invoice Generator
Project ID : 013

Customer Panel
"""

from tkinter import ttk

from src.models.customer_model import CustomerModel


class CustomerPanel(ttk.LabelFrame):
    """
    Customer information entry panel.
    """

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            text="Customer Information",
            padding=10,
        )

        self._create_widgets()
        self._configure_layout()

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _create_widgets(self) -> None:

        self.customer_name_label = ttk.Label(
            self,
            text="Customer Name"
        )
        self.customer_name_entry = ttk.Entry(
            self,
            width=50,
        )

        self.address_line_1_label = ttk.Label(
            self,
            text="Address Line 1"
        )
        self.address_line_1_entry = ttk.Entry(
            self,
            width=50,
        )

        self.address_line_2_label = ttk.Label(
            self,
            text="Address Line 2"
        )
        self.address_line_2_entry = ttk.Entry(
            self,
            width=50,
        )

        self.city_label = ttk.Label(
            self,
            text="City"
        )
        self.city_entry = ttk.Entry(
            self,
            width=25,
        )

        self.state_label = ttk.Label(
            self,
            text="State"
        )
        self.state_entry = ttk.Entry(
            self,
            width=25,
        )

        self.postal_code_label = ttk.Label(
            self,
            text="Postal Code"
        )
        self.postal_code_entry = ttk.Entry(
            self,
            width=15,
        )

        self.country_label = ttk.Label(
            self,
            text="Country"
        )
        self.country_entry = ttk.Entry(
            self,
            width=20,
        )

        self.phone_label = ttk.Label(
            self,
            text="Phone"
        )
        self.phone_entry = ttk.Entry(
            self,
            width=25,
        )

        self.email_label = ttk.Label(
            self,
            text="Email"
        )
        self.email_entry = ttk.Entry(
            self,
            width=35,
        )

        self.reference_label = ttk.Label(
            self,
            text="Customer Reference"
        )
        self.reference_entry = ttk.Entry(
            self,
            width=35,
        )

    def _configure_layout(self) -> None:

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.customer_name_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.customer_name_entry.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.address_line_1_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.address_line_1_entry.grid(
            row=1,
            column=1,
            columnspan=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.address_line_2_label.grid(
            row=2,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.address_line_2_entry.grid(
            row=2,
            column=1,
            columnspan=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.city_label.grid(
            row=3,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.city_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.state_label.grid(
            row=3,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.state_entry.grid(
            row=3,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.postal_code_label.grid(
            row=4,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.postal_code_entry.grid(
            row=4,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.country_label.grid(
            row=4,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.country_entry.grid(
            row=4,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.phone_label.grid(
            row=5,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.phone_entry.grid(
            row=5,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.email_label.grid(
            row=5,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.email_entry.grid(
            row=5,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.reference_label.grid(
            row=6,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.reference_entry.grid(
            row=6,
            column=1,
            columnspan=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def get_data(self) -> CustomerModel:
        """
        Returns the entered customer information.
        """

        return CustomerModel(
            customer_name=self.customer_name_entry.get().strip(),
            address_line_1=self.address_line_1_entry.get().strip(),
            address_line_2=self.address_line_2_entry.get().strip(),
            city=self.city_entry.get().strip(),
            state=self.state_entry.get().strip(),
            postal_code=self.postal_code_entry.get().strip(),
            country=self.country_entry.get().strip(),
            phone_number=self.phone_entry.get().strip(),
            email_address=self.email_entry.get().strip(),
            customer_reference=self.reference_entry.get().strip(),
        )

    def set_data(
        self,
        customer: CustomerModel,
    ) -> None:
        """
        Populates the panel using a CustomerModel.
        """

        entries = [
            (self.customer_name_entry, customer.customer_name),
            (self.address_line_1_entry, customer.address_line_1),
            (self.address_line_2_entry, customer.address_line_2),
            (self.city_entry, customer.city),
            (self.state_entry, customer.state),
            (self.postal_code_entry, customer.postal_code),
            (self.country_entry, customer.country),
            (self.phone_entry, customer.phone_number),
            (self.email_entry, customer.email_address),
            (self.reference_entry, customer.customer_reference),
        ]

        for entry, value in entries:
            entry.delete(0, "end")
            entry.insert(0, value)


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# CustomerPanel(parent)
# get_data()
# set_data(customer)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# tkinter.ttk
# src.models.customer_model