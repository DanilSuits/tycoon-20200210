import unittest
from parameterized import parameterized

def lastDelivery(container_schedule):
    DURATION_FROM_FACTORY_TO_PORT = 1
    DURATION_FROM_PORT_TO_A = 4
    DURATION_FROM_FACTORY_TO_B = 5

    delivery_times = []

    departure_from_factory = 0

    if "B" == container_schedule:
        # Leg: factory to B
        arrival_at_b = departure_from_factory + DURATION_FROM_FACTORY_TO_B
        delivery_time = arrival_at_b
        delivery_times.append(delivery_time)
    else:
        # Leg: factory to port
        arrival_at_port = departure_from_factory + DURATION_FROM_FACTORY_TO_PORT

        # Leg: port to A
        departure_from_port = arrival_at_port
        arrival_at_A = departure_from_port + DURATION_FROM_PORT_TO_A

        delivery_time = arrival_at_A

        delivery_times.append(delivery_time)

    return max(delivery_times)

class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ["B", 5],
        ["A", 5]
    ])
    def test_something(self, container_schedule, last_delivery):
        self.assertEqual(
            last_delivery,
            lastDelivery(container_schedule)
        )


if __name__ == '__main__':
    unittest.main()
