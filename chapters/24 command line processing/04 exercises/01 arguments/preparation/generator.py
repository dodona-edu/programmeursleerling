import random
import string

import yaml

# Met een vaste seed krijgen we deterministische resultaten.
random.seed(123456789)


class FlowList(list):
    pass


class QuotedStr(str):
    pass


yaml.add_representer(
    FlowList,
    lambda dumper, data: dumper.represent_sequence(
        'tag:yaml.org,2002:seq', data, flow_style=True
    ),
)
yaml.add_representer(
    QuotedStr,
    lambda dumper, data: dumper.represent_scalar(
        'tag:yaml.org,2002:str', data, style="'"
    ),
)


def generate_data():
    data = []
    for _ in range(45):
        number_of_numbers = random.randint(0, 10)
        data.append(random.sample(range(-100, 100), number_of_numbers))
    other_data = [*string.ascii_letters, "Hello World", "twintig", "26.93", "5", "2"]
    for _ in range(5):
        number_of_numbers = random.randint(0, 10)
        data.append(random.sample(other_data, number_of_numbers))
    random.shuffle(data)
    return data


def is_all_int(data):
    for x in data:
        try:
            int(x)
        except ValueError:
            return False
    return True


if __name__ == '__main__':
    testcases = []
    numbers = generate_data()
    for inputs in numbers:
        testcase = {
            "arguments": FlowList(QuotedStr(str(x)) for x in inputs),
        }
        if is_all_int(inputs):
            testcase["stdout"] = QuotedStr(str(sum(inputs)))
        else:
            testcase["stderr"] = {
                "data": "",
                "oracle": "custom_check",
                "file": "stderr_check.py",
                "name": "evaluate",
            }
            testcase["exit_code"] = 1
        testcases.append(testcase)

    suite = [
        {
            "tab": "Feedback",
            "testcases": testcases,
        }
    ]

    with open("../evaluation/suite.yaml", "w") as f:
        yaml.dump(suite, f, default_flow_style=False, sort_keys=False)
