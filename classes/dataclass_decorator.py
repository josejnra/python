from dataclasses import dataclass, astuple, asdict, field
from typing import ClassVar


@dataclass
class Person:
    """Person

    why to use dataclass:
    - write less code
    - there is no data validation
    - easy conversion to tuple, dict
    """

    # class attributes
    specie: ClassVar[str] = "Homo Sapiens"

    # object attributes
    name: str
    surname: str
    age: int
    full_name: str = field(init=False, repr=False)

    def __post_init__(self):
        self.full_name = f"{self.name} {self.surname}"


if __name__ == "__main__":
    person1 = Person(name="jose", surname="nunes", age=29)
    person2 = Person(name="jose", surname="nunes", age=29)

    print(person1, person2)
    print(person1 == person2)

    print(astuple(person1))
    print(asdict(person2))
