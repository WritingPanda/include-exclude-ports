import unittest
import apply_port_exlusions as ape


class TestApplyPortExclusions(unittest.TestCase):
    def test_first_input(self):
        include_ports = [[80, 80], [22, 23], [8000, 9000]]
        exclude_ports = [8080, 8080]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[22, 23], [80, 80], [8000, 8079], [8081, 9000]], result)

    def test_second_input(self):
        include_ports = [[8000, 9000], [80, 80], [22, 23]]
        exclude_ports = [1024, 1024]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[22, 23], [80, 80], [8000, 9000]], result)

    def test_third_input(self):
        include_ports = [[1,65535]]
        exclude_ports = [1000,2000]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[1, 999], [2001, 65535]], result)

    def test_fourth_input(self):
        include_ports = [[1, 1], [3, 65535], [2, 2]]
        exclude_ports = [500, 2500]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[1, 499], [2501, 65535]], result)

    def test_fifth_input(self):
        include_ports = []
        exclude_ports = [8080, 8080]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([], result)

    def test_low_edge_case(self):
        include_ports = [[1, 1000]]
        exclude_ports = [1, 1]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[2, 1000]], result)

    def test_high_edge_case(self):
        include_ports = [[1, 1000]]
        exclude_ports = [1000, 1000]
        result = ape.apply_port_exclusions(include_ports, exclude_ports)
        self.assertEqual([[1, 999]], result)

    def test_combined_sequential_ports(self):
        result = ape.combine_sequential_ports([[1, 1], [3, 65535], [2, 2]])
        self.assertEqual([[1, 65535]], result)

    def test_combined_sequential_ports_empty_list(self):
        result = ape.combine_sequential_ports([])
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()
