# -*- coding:utf-8 -*-
from MyQR import myqr


# myqr.run(
#         words='http://www.baidu.com',
#         # picture='2.jpg',
#         # colorized=True,
#         version=5,  # 1-40
#         contrast=1.0,
#         brightness=1.0,
#         level = 'L', #L，M，Q，H
#         save_name='L.png',
#         save_dir=r'C:\Users\dan\Desktop\code'
#         )


def getimage(url,level,image_name,image_url):

    myqr.run(
        words=url,
        # picture='2.jpg',
        # colorized=True,
        version=5,  # 1-40
        contrast=1.0,
        brightness=1.0,
        level =level, #L，M，Q，H
        save_name=image_name,
        save_dir=image_url
        )


def tt():
    myqr.run(
            words='123',
            # picture='2.jpg',
            # colorized=True,
            version=5,  # 1-40
            contrast=1.0,
            brightness=1.0,
            level = 'L', #L，M，Q，H
            save_name='123.png',
            save_dir=r'C:\Users\dan\Desktop\code'
            )

tt()