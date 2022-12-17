from pathlib import Path
from dataclasses import dataclass

DATA_FILE = "../data/data.txt"

@dataclass(frozen=True)
class InputAndTarget:
    candidates: list[int]
    target: int

@dataclass(frozen=True)
class Result:
    indexes: set[int]
    found: bool


def get_list_of_nums_and_target(file: str)-> (InputAndTarget | None):
    with Path(DATA_FILE).open() as data:
        nums: str = data.readline()
        list_of_nums: list[str] = nums.strip(' \n').split(' ')
        list_of_integers: list[int] = [int(x) for x in list_of_nums]
        target: int = int(data.readline().strip('\n'))
        result: InputAndTarget = InputAndTarget(candidates=list_of_integers, target=target)
        return result
    return None



    



if __name__ == '__main__':
    list_of_numbers: list[int] = []
    target: int = -1
    print(get_list_of_nums_and_target(file=DATA_FILE))
    


