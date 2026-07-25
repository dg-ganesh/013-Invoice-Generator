"""
Project : Invoice Generator
Project ID : 013

Main Application Window
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from src import config
from src.ui.invoice_form import InvoiceForm


class MainWindow:
    """
    Main application window.
    """

    def __init__(self) -> None:

        self.root = tk.Tk()

        self._configure_window()

        self._create_menu()

        self._create_layout()

        self._create_status_bar()

        self.root.bind_all(
            "<MouseWheel>",
            self._on_mousewheel,
        )

    # ---------------------------------------------------------
    # Window Configuration
    # ---------------------------------------------------------

    def _configure_window(self) -> None:
        """
        Configures the application window.
        """

        self.root.title(
            config.WINDOW_TITLE
        )

        self.root.geometry(
            f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}"
        )

        self.root.minsize(
            config.WINDOW_MIN_WIDTH,
            config.WINDOW_MIN_HEIGHT,
        )

        self.root.rowconfigure(
            0,
            weight=1,
        )

        self.root.columnconfigure(
            0,
            weight=1,
        )

    # ---------------------------------------------------------
    # Menu
    # ---------------------------------------------------------

    def _create_menu(self) -> None:
        """
        Creates the application menu.
        """

        self.menu_bar = tk.Menu(
            self.root,
        )

        #
        # File Menu
        #

        self.file_menu = tk.Menu(
            self.menu_bar,
            tearoff=False,
        )

        self.file_menu.add_command(
            label="New Invoice",
            command=self._menu_new_invoice,
        )

        self.file_menu.add_command(
            label="Open Invoice",
            command=self._menu_open_invoice,
        )

        self.file_menu.add_command(
            label="Save Invoice",
            command=self._menu_save_invoice,
        )

        self.file_menu.add_separator()

        self.file_menu.add_command(
            label="Calculate Invoice",
            command=self._menu_calculate_invoice,
        )

        self.file_menu.add_separator()

        self.file_menu.add_command(
            label="Export PDF",
            command=self._menu_export_pdf,
        )

        self.file_menu.add_separator()

        self.file_menu.add_command(
            label="Exit",
            command=self.root.destroy,
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu,
        )

        #
        # Help Menu
        #

        self.help_menu = tk.Menu(
            self.menu_bar,
            tearoff=False,
        )

        self.help_menu.add_command(
            label="About",
            command=self._show_about,
        )

        self.menu_bar.add_cascade(
            label="Help",
            menu=self.help_menu,
        )

        self.root.configure(
            menu=self.menu_bar,
        )
    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _create_layout(self) -> None:
        """
        Creates the main application layout.
        """

        self.main_container = ttk.Frame(
            self.root,
            padding=5,
        )

        self.main_container.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.main_container.rowconfigure(
            0,
            weight=1,
        )

        self.main_container.columnconfigure(
            0,
            weight=1,
        )

        #
        # Scrollable Canvas
        #

        self.canvas = tk.Canvas(
            self.main_container,
            highlightthickness=0,
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.scrollbar = ttk.Scrollbar(
            self.main_container,
            orient="vertical",
            command=self.canvas.yview,
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set,
        )

        self.scrollable_frame = ttk.Frame(
            self.canvas,
        )

        self.canvas_window = self.canvas.create_window(
            (
                0,
                0,
            ),
            window=self.scrollable_frame,
            anchor="nw",
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda event: self._update_scroll_region(),
        )

        self.canvas.bind(
            "<Configure>",
            self._resize_canvas,
        )

        self.invoice_form = InvoiceForm(
            self.scrollable_frame,
        )

        self.invoice_form.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5,
        )

        self._update_scroll_region()

    def _resize_canvas(
        self,
        event,
    ) -> None:
        """
        Keeps the form width equal to the
        canvas width.
        """

        self.canvas.itemconfigure(
            self.canvas_window,
            width=event.width,
        )

    def _update_scroll_region(
        self,
    ) -> None:
        """
        Updates the canvas scroll region.
        """

        self.root.update_idletasks()

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"),
        )

    def _on_mousewheel(
        self,
        event,
    ) -> None:
        """
        Mouse wheel scrolling.
        """

        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units",
        )

    # ---------------------------------------------------------
    # Status Bar
    # ---------------------------------------------------------

    def _create_status_bar(self) -> None:
        """
        Creates the application status bar.
        """

        self.status_text = tk.StringVar(
            value="Ready",
        )

        self.status_bar = ttk.Label(
            self.root,
            textvariable=self.status_text,
            relief=tk.SUNKEN,
            anchor="w",
        )

        self.status_bar.grid(
            row=1,
            column=0,
            sticky="ew",
        )

    # ---------------------------------------------------------
    # Menu Commands
    # ---------------------------------------------------------

    def _menu_new_invoice(self) -> None:

        self.invoice_form._new_invoice()

    def _menu_open_invoice(self) -> None:

        self.invoice_form._load_invoice()

    def _menu_save_invoice(self) -> None:

        self.invoice_form._save_invoice()

    def _menu_calculate_invoice(self) -> None:

        self.invoice_form._calculate_invoice()

    def _menu_export_pdf(self) -> None:

        self.invoice_form._export_pdf()

    def _show_about(self) -> None:
        """
        Displays the About dialog.
        """

        messagebox.showinfo(
            "About",
            (
                f"{config.WINDOW_TITLE}\n\n"
                "Version 1.0.0\n\n"
                "Professional Invoice Generator\n"
                "Developed using Python and Tkinter."
            ),
        )

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def set_status(
        self,
        message: str,
    ) -> None:
        """
        Updates the status bar.
        """

        self.status_text.set(
            message,
        )

    def run(self) -> None:
        """
        Starts the application.
        """

        self.root.mainloop()


# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# MainWindow()
# set_status(message)
# run()

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
#
# src.config
# src.ui.invoice_form