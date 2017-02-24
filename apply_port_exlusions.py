
def apply_port_exclusions(include_ports=None, exclude_ports=None):
    """
    Takes two lists and produces one list as output.
    :param include_ports:
    :param exclude_ports:
    :return:
    """
    if include_ports:
        for x in range(len(include_ports)):
            print(include_ports[x])
    else:
        print("Nothing here.")

include = [[80, 80], [22, 23], [8000, 9000]]
exclude = [8080, 8080]

apply_port_exclusions(include_ports=include, exclude_ports=exclude)
