import os
from certigen import read_attendees, generate_qr_code, generate_certificate

def test_read_attendees():
    data = read_attendees("sample_attendees.csv")  # Create a small sample file
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]

def test_generate_qr_code():
    path = generate_qr_code("Test User")
    assert os.path.exists(path)
    assert path.endswith(".png")

def test_generate_certificate():
    path = generate_certificate("Test User", "Test Event", "2025-04-05", template="certificate.png")
    assert os.path.exists(path)
    assert path.endswith(".pdf")
