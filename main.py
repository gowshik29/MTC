from numpy import product
import qnot
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def collect_size_keys(data):
    size_keys = set()

    for sub_array in data:
        for dictionary in sub_array:
            data_dict = list(dictionary["size"].keys())
            for i in data_dict:
                size_keys.add(i)

    return list(size_keys)


def generate_final_report(pdf_path, data):
    output_pdf_path = "final_report.pdf"

    size_keys = collect_size_keys(data)

    with canvas.Canvas(output_pdf_path, pagesize=letter) as c:
        c.setFont("Helvetica", 12)
        c.drawString(100, 800, "Final Report")

        # Add content to the PDF
        for product in data:
            c.drawString(100, 780, f"Course completion Date: {product['date']}")
            c.drawString(100, 760, f"Name of the Person: {product['name']}")
            c.drawString(100, 740, f"Course Title: {', '.join(product['course_name'])}")
            c.drawString(100, 720, f"Professor Name: {product['professor_name']}")
            c.drawString(100, 700, f"Certificate Link: {product['link']}")

            for key in size_keys:
                c.drawString(
                    120,
                    580 - size_keys.index(key) * 20,
                    f"{key}: {product['size'].get(key, 0)}",
                )

            c.drawString(100, 560, "=" * 50)  # Separator between products

            # Move to the next page if there are more products
            c.showPage()

    print(f"Final report generated and saved to {output_pdf_path}")


pdf_path = "Coursera Introduction of ML.pdf"
p = qnot.annotate_blocks_with_rectangles("modified.pdf")


# Generate the final report in PDF format
generate_final_report(pdf_path, data=product)
