class Patient:
    def __init__(self, name: str):
        self.set_name(name)

    def set_name(self, name: str):
        if name == "":
            raise ValueError("Patient name cannot be empty")
        self.__name = name

    def get_name(self) -> str:
        return self.__name