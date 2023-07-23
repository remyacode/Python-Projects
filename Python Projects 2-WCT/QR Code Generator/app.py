import qrcode as qr
url=input('Enter url:   ')
img=qr.make(url)
img.save("QR Code Generator/QR/img.png")
