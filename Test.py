import unittest
from Transport import Transport


class TransportTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        # Complete the initialization of the Transport object
        super(TransportTest, self).__init__(*args, **kwargs)
        self.transport = Transport()

    def test_Fare(self):
        # Complete this test of the Fare method from the Transport class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_refuel(self):
        # Complete this test of how many refuels a transport will have based on the refuel method from the Transport
        # class
        #
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_totalfare(self):
        # Complete this test of the total fare method from the Transport class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass

    def test_print(self):
        # Complete this test of the __str__ method from the Transport class
        # Add a few more assertEquals
        self.assertEqual(1, 1)
        pass


if __name__ == "__main__":
    unittest.main()
