def int32_to_ip(number: int):
    ip_list = list()

    for i in range (3, -1, -1):
        ip_number = number // (256 ** i) % 256
        ip_list.append(str(ip_number))

    return '.'.join(ip_list)

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"



