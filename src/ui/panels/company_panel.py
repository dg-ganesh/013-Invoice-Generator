"""
Project : Invoice Generator
Project ID : 013

Company Panel
"""

from tkinter import ttk

from src.models.company_model import CompanyModel


class CompanyPanel(ttk.LabelFrame):
    """
    Company information entry panel.
    """

    def __init__(self, parent) -> None:
        super().__init__(
            parent,
            text="Business Information",
            padding=10,
        )

        self._create_widgets()
        self._configure_layout()

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _create_widgets(self) -> None:

        self.company_name_label = ttk.Label(
            self,
            text="Company Name"
        )
        self.company_name_entry = ttk.Entry(
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

        self.website_label = ttk.Label(
            self,
            text="Website"
        )
        self.website_entry = ttk.Entry(
            self,
            width=35,
        )

        self.tax_registration_label = ttk.Label(
            self,
            text="GST / VAT Number"
        )
        self.tax_registration_entry = ttk.Entry(
            self,
            width=30,
        )

    def _configure_layout(self) -> None:

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

        self.company_name_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.company_name_entry.grid(
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

        self.website_label.grid(
            row=6,
            column=0,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.website_entry.grid(
            row=6,
            column=1,
            padx=5,
            pady=4,
            sticky="ew",
        )

        self.tax_registration_label.grid(
            row=6,
            column=2,
            padx=5,
            pady=4,
            sticky="w",
        )
        self.tax_registration_entry.grid(
            row=6,
            column=3,
            padx=5,
            pady=4,
            sticky="ew",
        )

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def get_data(self) -> CompanyModel:
        """
        Returns the entered company information.
        """

        return CompanyModel(
            company_name=self.company_name_entry.get().strip(),
            address_line_1=self.address_line_1_entry.get().strip(),
            address_line_2=self.address_line_2_entry.get().strip(),
            city=self.city_entry.get().strip(),
            state=self.state_entry.get().strip(),
            postal_code=self.postal_code_entry.get().strip(),
            country=self.country_entry.get().strip(),
            phone_number=self.phone_entry.get().strip(),
            email_address=self.email_entry.get().strip(),
            website=self.website_entry.get().strip(),
            tax_registration_number=self.tax_registration_entry.get().strip(),
        )

    def set_data(
        self,
        company: CompanyModel,
    ) -> None:
        """
        Populates the panel using a CompanyModel.
        """

        entries = [
            (self.company_name_entry, company.company_name),
            (self.address_line_1_entry, company.address_line_1),
            (self.address_line_2_entry, company.address_line_2),
            (self.city_entry, company.city),
            (self.state_entry, company.state),
            (self.postal_code_entry, company.postal_code),
            (self.country_entry, company.country),
            (self.phone_entry, company.phone_number),
            (self.email_entry, company.email_address),
            (self.website_entry, company.website),
            (
                self.tax_registration_entry,
                company.tax_registration_number,
            ),
        ]

        for entry, value in entries:
            entry.delete(0, "end")
            entry.insert(0, value)


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# CompanyPanel(parent)
# get_data()
# set_data(company)

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# tkinter.ttk
# src.models.company_model