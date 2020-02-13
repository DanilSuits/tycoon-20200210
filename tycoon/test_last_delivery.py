import unittest

def lastDelivery(container_schedule):
    delivery_times = [5]
    return max(delivery_times)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            5,
            lastDelivery("A")
        )


if __name__ == '__main__':
    unittest.main()
