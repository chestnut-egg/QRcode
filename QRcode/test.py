import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance

# a = 'C:\\Users\\dan\\Desktop\\code'
#
# c = r'\\'.join(a.split("\\"))
#
# d = a.replace('\\', '\\').strip()
# e = '/save' + d[2:]
# print(a)





image = "H.png"

img = Image.open(image)

#img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

#img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

#img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

#img = img.convert('L')#灰度化

# img.show()

barcodes = pyzbar.decode(img)

for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)