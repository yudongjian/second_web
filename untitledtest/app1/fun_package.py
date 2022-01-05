import hashlib


def get_self_md5(str2, salt):
    # 传入密码和盐
    # 加密的函数
    # 如果传入盐的参数，则加盐
    s = str(str2)  # 类型转换，转成字符串
    if salt:
        s = s + salt
    m = hashlib.md5(s.encode())  # md5加密
    return m.hexdigest()  # 返回密文


