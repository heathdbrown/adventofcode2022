from collections import defaultdict

STACK_WIDTH = 4


def read_input(file="day5-example.txt") -> tuple[str, str]:
    with open(file, "r") as f:
        crates, instructions = f.read().split("\n\n")
    return crates, instructions


def form_crates(crates: str) -> dict[int, list[str]]:
    """
    input:
            [D]
        [N] [C]
        [Z] [M] [P]
        1   2   3
    output:
        {
            1: ['Z', 'N', ' ']
            2: ['M', 'C', D']
            3: ['P', ' ', ' ']
        }
    """
    d: dict[int, list[str]] = defaultdict(list)
    stack_ids = []
    for col in crates.split("\n")[-1]:
        try:
            int(col)
        except:
            continue
        stack_ids.append(int(col))

    for j, row in enumerate(crates.split("\n")[::-1]):
        if j < 1:
            continue
        for stack_id in stack_ids:
            row_index = 1 + (STACK_WIDTH * (stack_id - 1))
            if row[row_index] != " ":
                d[stack_id].append(row[row_index])
    return d


def get_instructions(raw: str) -> tuple[int, int, int]:
    split_up = raw.split(" ")
    crates_to_move = int(split_up[1])
    source_stack = int(split_up[3])
    target_stack = int(split_up[5])
    return crates_to_move, source_stack, target_stack


def do_instruction(
    stacks: dict[int, list[str]], raw_instruction: str
) -> dict[int, list[str]]:
    crates_to_move, source_stack, target_stack = get_instructions(raw_instruction)
    for _ in range(crates_to_move):
        crate = stacks[source_stack].pop()
        print(f"Popped {crate} from {source_stack} and put on {target_stack}")
        stacks[target_stack].append(crate)
    return stacks


def do_instruction_9001(
    stacks: dict[int, list[str]], raw_instruction: str
) -> dict[int, list[str]]:
    crates_to_move, source_stack, target_stack = get_instructions(raw_instruction)
    crates = list(reversed([stacks[source_stack].pop() for _ in range(crates_to_move)]))
    stacks[target_stack].extend(crates)

    return stacks


def answer1(file: str):
    raw_crates, raw_instructions = read_input(file=file)
    # print(raw_instructions.split("\n"))
    stacks = form_crates(raw_crates)
    # print(stacks.values)
    for raw_instruction in raw_instructions.split("\n"):
        # print(raw_instruction)
        stacks = do_instruction(stacks, raw_instruction)
        # print(stacks)

    # print(stacks)
    tops = [v[-1] for v in stacks.values() if len(v) != 0]
    return "".join(tops)


def answer2(file: str):
    raw_crates, raw_instructions = read_input(file=file)
    stacks = form_crates(raw_crates)
    for raw_instruction in raw_instructions.split("\n"):
        stacks = do_instruction_9001(stacks, raw_instruction)

    tops = [v[-1] for v in stacks.values()]
    return "".join(tops)


if __name__ == "__main__":
    print(answer1(file="day5.txt"))
    print(answer2(file="day5.txt"))
