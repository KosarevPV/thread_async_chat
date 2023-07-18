import subprocess
from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping(start: str, end: str) -> dict:
    start = ip_address(start)
    end = ip_address(end)

    resource_data = []
    while start <= end:
        resource_data.append(start)
        start += 1

    return host_ping(resource_data)


if __name__ == '__main__':
    print(host_range_ping('140.82.121.13', '140.82.121.15'))
