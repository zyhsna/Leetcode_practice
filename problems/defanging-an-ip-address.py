# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/28 17:14
# 文件名：defanging-an-ip-address.py
# 开发工具：PyCharm
def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    address = str(address)
    print(address.replace(".", "[.]"))
    print(address)

defangIPaddr("255.100.50.0")