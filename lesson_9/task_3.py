import tabulate


from task_2 import host_range_ping


def host_range_ping_tab():
    result = []
    for k, v in host_range_ping('140.82.121.13', '140.82.121.15').items():
        if v:
            result.append(({'Узел доступен': k}))
        else:
            result.append(({'Узел недоступен': k}))
    return tabulate.tabulate(result, headers='keys')


if __name__ == '__main__':
    print(host_range_ping_tab())
