"""
Project : Invoice Generator
Project ID : 013

PDF Styles
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import TableStyle


class PdfStyles:
    """
    Centralized PDF styles.

    This module contains all styles used by the
    PDF Export Service.
    """

    _styles = getSampleStyleSheet()

    # ---------------------------------------------------------
    # Page Constants
    # ---------------------------------------------------------

    PAGE_MARGIN = 40

    TITLE_FONT_SIZE = 20

    HEADING_FONT_SIZE = 12

    BODY_FONT_SIZE = 10

    SMALL_FONT_SIZE = 8

    # ---------------------------------------------------------
    # Paragraph Styles
    # ---------------------------------------------------------

    TITLE = ParagraphStyle(
        "InvoiceTitle",
        parent=_styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=TITLE_FONT_SIZE,
        leading=24,
        spaceAfter=18,
    )

    SECTION_HEADING = ParagraphStyle(
        "SectionHeading",
        parent=_styles["Heading2"],
        alignment=TA_LEFT,
        fontSize=HEADING_FONT_SIZE,
        spaceAfter=8,
        spaceBefore=8,
    )

    NORMAL = ParagraphStyle(
        "NormalText",
        parent=_styles["BodyText"],
        alignment=TA_LEFT,
        fontSize=BODY_FONT_SIZE,
        leading=14,
    )

    FOOTER = ParagraphStyle(
        "Footer",
        parent=_styles["BodyText"],
        alignment=TA_CENTER,
        fontSize=SMALL_FONT_SIZE,
        textColor=colors.grey,
    )

    # ---------------------------------------------------------
    # Table Styles
    # ---------------------------------------------------------

    ITEM_TABLE = TableStyle(

        [

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey,
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.black,
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.black,
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold",
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, 0),
                "CENTER",
            ),

            (
                "ALIGN",
                (1, 1),
                (-1, -1),
                "RIGHT",
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, 0),
                8,
            ),

            (
                "TOPPADDING",
                (0, 1),
                (-1, -1),
                6,
            ),

            (
                "BOTTOMPADDING",
                (0, 1),
                (-1, -1),
                6,
            ),

        ]

    )

    INFO_TABLE = TableStyle(

        [

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey,
            ),

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.whitesmoke,
            ),

            (
                "FONTNAME",
                (0, 0),
                (0, -1),
                "Helvetica-Bold",
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6,
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                6,
            ),

            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "LEFT",
            ),

            (
                "ALIGN",
                (1, 0),
                (1, -1),
                "LEFT",
            ),

        ]

    )

    TOTALS_TABLE = TableStyle(

        [

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "RIGHT",
            ),

            (
                "LINEABOVE",
                (0, 0),
                (-1, 0),
                1,
                colors.black,
            ),

            (
                "LINEBELOW",
                (0, -1),
                (-1, -1),
                1,
                colors.black,
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6,
            ),

        ]

    )


# ---------------------------------------------------------
# Public Methods
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Public Signals
# ---------------------------------------------------------

# None

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

# reportlab.lib.colors
# reportlab.lib.styles
# reportlab.lib.enums
# reportlab.platypus.TableStyle