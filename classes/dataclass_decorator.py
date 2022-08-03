from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Person:
    """Person

    - there is no data validation
    """

    # object attributes
    name: str
    age: int

    # class attributes
    specie: ClassVar[str] = "Homo Sapiens"


if __name__ == "__main__":
    person1 = Person(name="jose", age=29)
    person2 = Person(name="jose", age=29)

    print(person1, person2)
    print(person1 == person2)
