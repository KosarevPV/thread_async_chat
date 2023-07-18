import subprocess
from ipaddress import ip_address


def host_ping(resource_data: [str]) -> dict:
    result_data = {}
    for i in resource_data:
        try:
            resource = ip_address(i)
        except ValueError:
            resource = i
        response_ping = subprocess.run(['ping', str(resource)])

        if response_ping.returncode == 0:
            print('Узел доступен')
            result_data[str(i)] = True
        else:
            print('Узел недоступен')
            result_data[str(i)] = False
    return result_data


if __name__ == '__main__':
    host_ping(['140.82.121.3', '127.0.0.1', 'youtube.com', 'rwge32r.com'])
