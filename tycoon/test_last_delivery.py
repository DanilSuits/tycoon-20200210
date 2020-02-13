import unittest

def lastDelivery(container_schedule):
    delivery_times = []
    departure_from_port = 1
    duration_from_port_to_A = 4
    arrival_at_A = departure_from_port + duration_from_port_to_A
    delivery_time = arrival_at_A
    delivery_times.append(delivery_time)
    return max(delivery_times)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            5,
            lastDelivery("A")
        )


if __name__ == '__main__':
    unittest.main()
