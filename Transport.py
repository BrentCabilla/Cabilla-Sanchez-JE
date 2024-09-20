discount = {
    "Student": 0.10,
    "Regular": 0,
    "Senior": 0.25
}

class Transport:

    def __init__(self, transport: str, fare: float, gas: int):
        # Complete this method
        
        # Transport class has four attributes
        self.__type = transport
        # List of passengers
        # For example: [Student, Student, Regular]
        self.__passengers = list()

        # Fee for each passenger
        self.__fee = fare

        # Integer value
        # Each passenger consumes 1 level of gas
        self.__gas_level = gas

    # Create getters and setters for all attributes
    # vehicle type
    def get_type(self):
        return self.__type
    def set_type(self, transport: str):
        self.__type = transport

    #passenger
    def get_passengers(self):
        return self.__passengers
    def set_passengers(self, passengers: list):
        self.__passengers = passengers
    
    #gas level
    def get_gas_level(self):
        return self.__gas_level
    def set_gas_level(self, gas_level: int):
        self.__gas_level = gas_level

    
    # Then complete the following methods
    def add(self, passenger_type: str) -> None:
        """
            Adds a new passenger.
        :return:
        """
        if passenger_type in discount:
            self.__passengers.append(passenger_type)
            self.__gas_level -= 1
        else:
            raise ValueError

    def refuel(self) -> None:
        """
            Refuels when gas level is 0.

        :return:
        """
        if self.__gas_level == 0:
            self.__gas_level = len(self.__passengers)

    def totalFare(self) -> float:
        """
            Fare for all users combined.

        :return:
        """
        

    def fare(self, index: int) -> float:
        """
            Fare of a particular passenger. Fare = Transport Fee * Discount

        :param index: Passenger to calculate the fare.
        :return: Fare
        """

    def __str__(self) -> str:
        """
            Shows a summary of every passenger (how many students, seniors, regulars, etc.), the total fare,
            and how many times it should refuel.

        :return:
        """
