from socket import socket,gethostbyname,gethostname,AF_INET,SOCK_DGRAM

def host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    ip = '0.0.0.0'
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except OSError as ex:
        hostname = gethostname()
        ip = gethostbyname(hostname)
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    print(host_ip())