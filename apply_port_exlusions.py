def apply_port_exclusions(include_ports: list, exclude_ports: list) -> list:
    """
    Takes two lists and produces one list as output.
    :param include_ports: A list of lists of low, high pairs
    :type include_ports: list

    :param exclude_ports: A list of a low, high pair
    :type exclude_ports: list

    :return: list
    """
    # Combine sequential ports initially
    inc_ports = combine_sequential_ports(include_ports)
    # Isolate ports
    exclude_low, exclude_high = exclude_ports
    # Initialize result list
    result = list()
    # Iterate through the list of inc_ports
    for pair in inc_ports:
        # Isolate pairs in inc_ports
        low, high = pair
        pair_range = range(low, high + 1)

        if high < exclude_low or exclude_high < low:
            # Include this pair
            result.append(pair)
        elif exclude_low <= low and exclude_high >= high:
            # This pair is excluded
            continue
        if exclude_low in pair_range:
            if exclude_low == low:
                # If the low number in the exclude list
                # is lower than the low number in the include list
                # exclude it from the list
                pass
            else:
                # Otherwise, include it in the list
                result.append([low, exclude_low - 1])
        if exclude_high in pair_range:
            if exclude_high == high:
                # If the high number in the exclude list
                # is higher than the high number in the include list
                # exclude it from the final list
                pass
            else:
                # Otherwise, include it in the list
                result.append([exclude_high + 1, high])
    return result


def combine_sequential_ports(ports: list) -> list:
    """
    Takes in a list of ports [low, high] and checks to see
    if the if the adjacent pairs are sequential. If so, then
    go ahead and combine them into one list. For example:
    [[1, 1], [2, 2], [3, 45]] would become [[1, 45]].
    :param ports: A list of lists containing low, high pairs
    :type ports: list

    :return: list
    """
    if ports:
        # Initialize the list
        combined = list()
        # Sort the lists
        sorted_ports = sorted(ports)
        # Pop out the first index and add it to the combined list
        combined.append(sorted_ports.pop(0))
        # Iterate through the remaining lists
        for pair in sorted_ports:
            # Isolate values
            low, high = pair
            # Remove the first indexed list
            previous = combined.pop()
            # Isolate values
            prev_low, prev_high = previous
            # If the adjacent low value is equal
            # to the sum of the previous high # + 1,
            # then the numbers in the adjacent lists
            # are sequential and can be combined.
            if low == prev_high + 1:
                # The pairs are adjacent
                combined.append([prev_low, high])
            else:
                # Otherwise, append the lists to build
                # the fully combined list
                combined.append(previous)
                combined.append(pair)
        return combined
    else:
        return ports
