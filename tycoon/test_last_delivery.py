import unittest

def lastDelivery(container_schedule):
    DURATION_FROM_FACTORY_TO_PORT = 1
    DURATION_FROM_PORT_TO_A = 4

    delivery_times = []

    # Leg: factory to port
    departure_from_factory = 0
    arrival_at_port = departure_from_factory + DURATION_FROM_FACTORY_TO_PORT

    # Leg: port to A
    departure_from_port = arrival_at_port
    arrival_at_A = departure_from_port + DURATION_FROM_PORT_TO_A

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
