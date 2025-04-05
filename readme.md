 # CertiGen
    #### Video Demo:  https://youtu.be/q_0YBFkE6RE

    #### Description: To automatically generate customized certificates for event attendees (webinars, workshops, competitions, etc.) with their names and details, exporting each as a PDF.
    
Hi, I’m Siddhesh, and this is my final project for CS50P — a Certificate Generator for Events, built in Python.

This program automates the generation of event certificates using participant data from a CSV file. Each certificate is personalized with the participant’s name, event name, date, and even includes a unique QR code for verification.

The project is structured into two main files:
certigen.py contains the main logic, including a generate_certificate function that creates and exports a styled PDF for each participant.
test_project.py includes unit tests written with pytest to verify key parts of the code, such as PDF path creation and data handling.

So here's how it works:
I start with a certificate template image — like this one — and overlay text fields like the participant’s name and the event name. I also generate a QR code that links to a sample verification page. This QR code is embedded into the certificate to ensure authenticity.

When you run the program, it reads a list of participants from a CSV file, generates a certificate for each one, and saves it to an output folder.
Optionally, the QR images are cleaned up after PDF generation to keep things tidy.

I’ve also used error handling to ensure folders like output/ and qrs/ are created automatically, and the program gracefully handles missing resources like the seal image.

Finally, all project dependencies like fpdf2 and qrcode are listed in requirements.txt, making the setup straightforward.

That’s my Certificate Generator project — practical, modular, and testable. Thank you!