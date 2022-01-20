# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode

# String which represents the QR code
s = str(input('Enter link: '))


def generate_qr_code(s):
    link = pyqrcode.create(s)  # Generate QR code
    link.svg("myqr.svg", scale = 8)  # Create and save the svg file naming "myqr.svg"
    link.png('myqr.png', scale = 6)  # Create and save the png file naming "myqr.png"


if __name__ == '__main__':
    generate_qr_code(s)