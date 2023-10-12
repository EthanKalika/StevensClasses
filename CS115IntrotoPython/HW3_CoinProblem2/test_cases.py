from hw3 import *

class Tests():
    
    def __init__(self):
        self.tests = [
            {
                "func": giveChange,
                "possible_points": 15,
                "cmp": lambda x, y: x[0] == y[0] and set(x[1]) == set(y[1]),
                "tests": [
                    {
                        # "inputs" means that they are separate
                        # "input" (singular) means interpret a list as a single input 
                        "inputs": [400, [1, 9, 50, 392]],
                        "expected": [8, [50, 50, 50, 50, 50, 50, 50, 50]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 5, 10, 25]],
                        "expected": [4, [1, 1, 5, 25]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 7, 24, 42]],
                        "expected": [3, [1, 7, 24]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [1, 5, 10, 25, 50]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [50, 25, 10, 5, 1]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3 
                    }
                ]
            },
            {
                "func": wordsWithScore,
                "possible_points": 15,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [Dictionary, scrabbleScores],
                        "expected": [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]],
                        "points": 5
                    },
                    {
                        "inputs": [Dictionary, list(map(lambda x: [x[0], x[1]*2 + 1], scrabbleScores))],
                        "expected": [['a', 3], ['am', 10], ['at', 6], ['apple', 23], ['bat', 13], ['bar', 13], ['babble', 30], ['can', 13], ['foo', 15], ['spam', 20], ['spammy', 36], ['zzyzva', 84]],
                        "points": 5
                    },
                    {
                        "inputs": [["cats", "are", "cool"], scrabbleScores],
                        "expected": [['cats', 6], ['are', 3], ['cool', 6]],
                        "points": 5
                    }
                ]
            },
            {
                "func": take,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": ["hello"],
                        "points": 5
                    },
                    {
                        "inputs": [3, [1, 2, 3, 4, 5]],
                        "expected": [1, 2, 3],
                        "points": 5
                    },
                    {
                        "inputs": [0, [52, 34]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["a"],
                        "points": 5
                    }
                ]
            },
            {
                "func": drop,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [4, [1, 2, 3, 4, 5]],
                        "expected": [5],
                        "points": 5
                    },
                    {
                        "inputs": [0, ["a", "b", "c", "d"]],
                        "expected": ["a", "b", "c", "d"],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["b", "c"],
                        "points": 5
                    }
                ]
            }

        ]
memory_refresher = (
    "\n\n################ DONT FORGET ############\n"
    "## 5 points: Name, 5 points: Pledge    ##\n"
    "## 20 points: Docstrings  ##\n"
    "#########################################\n"
)

def test_answer(func, _input, expected, cmp, multi_input=False):

    try:
        # TODO: Only works for two inputs
        if multi_input:
            student_answer = func(_input[0], _input[1])
        else:
            student_answer = func(_input)
    except:
        raise RuntimeError("Oof, %s(%s) itself crashed :\\\n" % (func.__name__, _input))

    try:
        assert(cmp(student_answer, expected))
    except:
        print ("EXPECTED ANSWER: %s(%s) == %s" % (func.__name__, _input, expected))
        print ("STUDENT ANSWER:\t %s(%s) == %s" % (func.__name__, _input, student_answer))
        raise AssertionError("Yikes, their output was incorrect :(\n")


def run_all_tests():
    
    # We will sum these up as we go (variable possible points because some
    # assignments may have more or less than 100 points).
    possible_assign_points = 0
    final_assign_points = 0

    tests_ref = Tests()
    for test in tests_ref.tests:

        print("\n----------------------------------------------------------------------")
        print("Testing %s(): %s points" % (test["func"].__name__, test["possible_points"]))
        print("----------------------------------------------------------------------\n")

        for func_test in test["tests"]:
            try:

                # Check if we have "inputs" or "input". 
                # If it's "inputs", then use the different inputs 
                # If it's not, interpret input exactly as-is
                if "inputs" in func_test:
                    test_answer(test["func"], func_test["inputs"], func_test["expected"], test["cmp"], multi_input=True)
                else:
                    test_answer(test["func"], func_test["input"], func_test["expected"], test["cmp"])
                if "final_points" not in test:
                    test["final_points"] = 0
                test["final_points"] += func_test["points"]
            except (AssertionError, RuntimeError) as e:
                print (e)
        
        possible_assign_points += test["possible_points"]
        if "final_points" not in test:
            test["final_points"] = 0
        final_assign_points += test["final_points"]

        print ("%s/%s points" % (test["final_points"], test["possible_points"]))

    print ("\n\n##### TESTING COMPLETE ######")
    print ("## Final Code Score: %s/%s ##" % (final_assign_points, possible_assign_points))
    print ("#############################\n")

run_all_tests()
