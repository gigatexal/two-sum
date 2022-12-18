from pathlib import Path
from dataclasses import dataclass

DATA_FILE = "../data/data.txt"

@dataclass(frozen=True)
class InputAndTarget:
    candidates: list[int]
    target: int

@dataclass(frozen=True)
class Result:
    indexes: set[tuple[int, int]]
    found: bool


def get_list_of_nums_and_target(file: str)-> InputAndTarget:
    p = Path(DATA_FILE)
    with p.open() as data:
            nums: str = data.readline()
            list_of_nums: list[str] = nums.strip(' \n').split(' ') # text file has a trailing space before the new line, TODO: fix this?
            list_of_integers: list[int] = [int(x) for x in list_of_nums]
            target: int = int(data.readline().strip('\n'))
            result: InputAndTarget = InputAndTarget(candidates=list_of_integers, target=target)
            return result

def find_indexes_if_any(request: InputAndTarget)->Result:
    for index, value in enumerate(request.candidates):
        lookup_values = set(request.candidates)
        if (compliment:= request.target - value) in lookup_values:
            indexes=set([tuple([index, value]), tuple([request.candidates.index(compliment), compliment])])
            return Result(indexes=indexes, found=True)
    return Result(indexes=set(), found=False)



if __name__ == '__main__':
    input_and_target = get_list_of_nums_and_target(file=DATA_FILE)
    print(input_and_target)
    print(find_indexes_if_any(input_and_target))


