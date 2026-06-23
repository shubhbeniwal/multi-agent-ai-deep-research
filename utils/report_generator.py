from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    topic,
    report
):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Multi-Agent Research Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>Topic:</b> {topic}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    report = report.replace(
        "\n",
        "<br/>"
    )

    content.append(
        Paragraph(
            report,
            styles["BodyText"]
        )
    )

    pdf.build(content)