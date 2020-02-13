import unittest

def lastDelivery(container_schedule):
    delivery_times = []
    arrival_at_A = 5
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
