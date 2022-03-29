
# pip install pillow

from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO


def random_color():
    return (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))


str_all = string.digits + string.ascii_letters


def random_code(size=(200,40), length=4, point_num=100, line_num=15):
    # 生成一个200*40的白色背景图片
    width, height = size
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    # 新建一个和图片大小一样的画布
    draw = ImageDraw.Draw(img)
    #生成字体对象
    font = ImageFont.truetype(font='static/font/逐浪萌芽字.ttf', size=32)
    #书写文字

    valid_code=''
    for i in range(length):
        random_char = random.choice(str_all)
        draw.text((40*i+20, 10), random_char, (0, 0, 0), font=font)
        valid_code += random_char
    
    # 随机生成点
    for i in range(point_num):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x,y), random_color())

    # 随机画线
    for i in range(line_num):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line((x1,y1,x2,y2), fill=random_color())

    f = BytesIO()
    img.save(f, 'PNG')

    data = f.getvalue()
    
    return (data, valid_code)

if __name__ == '__main__':
    random_code()