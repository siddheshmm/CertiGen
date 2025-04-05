import csv
from fpdf import FPDF
import os
import qrcode

def read_attendees(csv_path="attendees.csv"):
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def generate_qr_code(name):
    qr_data = f"https://example.com/verify?name={name.replace(' ', '_')}"
    qr_img_path = f"qrs/{name.replace(' ', '_')}_qr.png"
    if not os.path.exists("qrs"):
        os.makedirs("qrs")
    qr = qrcode.make(qr_data)
    qr.save(qr_img_path)
    return qr_img_path
                
def generate_certificate(name, event, date, template="certificate.png"):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()

    # Background template
    pdf.image(template, x=0, y=0, w=297, h=210)

    # Event Name
    pdf.set_font('Helvetica', 'B', 20)
    pdf.set_text_color(0, 51, 102)  # Dark blue for event name
    pdf.set_xy(0, 17)
    pdf.cell(w=297, h=10, text=event.upper(), align='C')

    # Name
    pdf.set_font('Times', 'B', 48)
    pdf.set_text_color(81, 114, 119)
    pdf.set_xy(0, 100)
    pdf.cell(w=297, h=10, text=name, align='C')

    # Event + date
    pdf.set_font('Times', '', 18)
    pdf.set_text_color(81, 114, 119)
    pdf.set_xy(0, 115)
    pdf.cell(w=297, h=45, text=f"{event} held on {date}", align='C')

    # Generate QR Code
    qr_data = f"https://example.com/verify?name={name.replace(' ', '_')}"
    qr_img_path = f"qrs/{name.replace(' ', '_')}_qr.png"
    if not os.path.exists("qrs"):
        os.makedirs("qrs")
    qr = qrcode.make(qr_data)
    qr.save(qr_img_path)

    # Add QR code to certificate
    pdf.image(qr_img_path, x=180, y=153, w=35, h=35)

    # Add seal/stamp if available
    if os.path.exists("seal.png"):
        pdf.image("seal.png", x=80, y=150, w=40)

    # Ensure output folder exists
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save PDF
    safe_name = name.replace(" ", "_")
    pdf_path = f"output/{safe_name}.pdf"
    pdf.output(pdf_path)

    # Clean up QR image (optional)
    os.remove(qr_img_path)

    return pdf_path  # Useful for testing

def main():
    data = read_attendees()
    for row in data:
        print('Generating certificate for- ', row["name"], row["event"], row["date"])
        generate_certificate(row["name"], row["event"], row["date"])

if __name__ == "__main__":
    main()