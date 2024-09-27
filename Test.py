import unittest
from Transport import Transport


class TransportTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        # Complete the initialization of the Transport object
        super(TransportTest, self).__init__(*args, **kwargs)
        self.transport = Transport("Bus", 100, 3)

    def test_Fare(self):
        # Complete this test of the Fare method from the Transport class
        # Add a few more assertEquals
        self.transport.add("Student")
        self.assertEqual(self.transport.fare(0), 90.0)
        
        self.transport.add("Senior")
        self.assertEqual(self.transport.fare(1), 75.0)
        
        self.transport.add("Regular")
        self.assertEqual(self.transport.fare(2), 100.0)

    def test_refuel(self):
        # Complete this test of how many refuels a transport will have based on the refuel method from the Transport
        # class
        #
        # Add a few more assertEquals
        self.transport.add("Student")
        self.transport.add("Regular")
        self.transport.add("Senior")
        self.transport.refuel()
        self.assertEqual(self.transport.get_gas_level(), 3)

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
