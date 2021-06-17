class CsvAndInstanceError(Exception):
    def __init__(self) -> None:
        self.message = "An instance and a csv file are both provided."
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"
