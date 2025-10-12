class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"
    

    @staticmethod
    def add(a, b):
        """
        Static method: Adds two numbers.
        Does not access class or instance data.
        """
        return a + b


    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Multiplies two numbers.
        Accesses class-level attribute using 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b