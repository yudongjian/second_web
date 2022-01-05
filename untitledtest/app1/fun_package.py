import hashlib
from captcha.image import ImageCaptcha
from random import randint
import io


def get_self_md5(str2, salt):
    # 传入密码和盐
    # 加密的函数
    # 如果传入盐的参数，则加盐
    s = str(str2)  # 类型转换，转成字符串
    if salt:
        s = s + salt
    m = hashlib.md5(s.encode())  # md5加密
    return m.hexdigest()  # 返回密文


def get_verify_code():
    code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    code_str = ''
    for i in range(4):
        code_str += code_list[randint(0, 62)]
    image = ImageCaptcha().generate_image(code_str)

    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    image.save(buf, 'png')
    return buf.getvalue(), 'image/png'

