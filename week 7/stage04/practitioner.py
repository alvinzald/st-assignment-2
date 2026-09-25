class Practitioner:
    def __init__(self, identifier: str, name: str, specialty:str):
        self.set_id(identifier)
        self.set_name(name)
        self.availability = []

    def set_id(self, identifier: str):
        if identifier == "":
            raise ValueError("Practitioner identifier cannot be empty")
        self.__identifier = identifier

    def set_name(self, name: str):
        if name == "":
            raise ValueError("Practitioner name cannot be empty")
        self.__name = name

    def set_specialty(self, specialty: str):
        if specialty == "":
            raise ValueError("Practitioner specialty cannot be empty")
        self.__specialty = specialty

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_specialty(self) -> str:
        return self.__specialty