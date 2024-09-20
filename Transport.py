discount = {
    "Student": 0.10,
    "Regular": 0,
    "Senior": 0.25
}

class Transport:

    def __init__(self):
        # Complete this method

        # Transport class has four attributes
        self.__type = None
        # List of passengers
        # For example: [Student, Student, Regular]
        self.__passengers = list()

        # Fee for each passenger
        self.__fee = None

        # Integer value
        # Each passenger consumes 1 level of gas
        self.__gas_level = None

    # Create getters and setters for all attributes

    # Then complete the following methods

    def add(self) -> None:
        """
            Adds a new passenger.
        :return:
        """
        pass

    def refuel(self) -> None:
        """
            Refuels when gas level is 0.

        :return:
        """
        pass

    def totalFare(self) -> float:
        """
            Fare for all users combined.

        :return:
        """
        pass

    def fare(self, index: int) -> float:
        """
            Fare of a particular passenger. Fare = Transport Fee * Discount

        :param index: Passenger to calculate the fare.
        :return: Fare
        """
        pass

    def __str__(self) -> str:
        """
            Shows a summary of every passenger (how many students, seniors, regulars, etc.), the total fare,
            and how many times it should refuel.

        :return:
        """
        pass