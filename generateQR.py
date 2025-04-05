import qrcode

data = "https://example.com/verify?name=Ananya_Joshi"  # Replace dynamically later
qr = qrcode.make(data)
qr.save("qrs/Ananya_Joshi_qr.png")
