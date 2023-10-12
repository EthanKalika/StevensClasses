import hw4
import sys

sys.setrecursionlimit(10000)

class Tests():
    
    def __init__(self):
        self.tests = [
            {
                "func": hw4.pascal_row,
                "possible_points": 32,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": 0,
                        "expected": [1],
                        "points": 4
                    },
                    {
                        "input": 1,
                        "expected": [1,1],
                        "points": 4
                    },
                    {
                        "input": 5,
                        "expected": [1,5,10,10,5,1],
                        "points": 4
                    },
                    {
                        "input": 7,
                        "expected": [1,7,21,35,35,21,7,1],
                        "points": 4
                    },
                    {
                        "input": 10,
                        "expected": [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
                        "points": 4
                    },
                                        {
                        "input": 2,
                        "expected": [1,2,1],
                        "points": 4
                    },
                                        {
                        "input": 50,
                        "expected": [1, 50, 1225, 19600, 230300, 2118760, 15890700, 99884400, 536878650, 2505433700, 10272278170, 37353738800, 121399651100, 354860518600, 937845656300, 2250829575120, 4923689695575, 9847379391150, 18053528883775, 30405943383200, 47129212243960, 67327446062800, 88749815264600, 108043253365600, 121548660036300, 126410606437752, 121548660036300, 108043253365600, 88749815264600, 67327446062800, 47129212243960, 30405943383200, 18053528883775, 9847379391150, 4923689695575, 2250829575120, 937845656300, 354860518600, 121399651100, 37353738800, 10272278170, 2505433700, 536878650, 99884400, 15890700, 2118760, 230300, 19600, 1225, 50, 1],
                        "points": 4
                    },
                    {
                        "input": 15,
                        "expected": [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1],
                        "points": 4
                    }
                ]
            },
            {
                "func": hw4.pascal_triangle,
                "possible_points": 16,
                "cmp": lambda x, y: x == y,
                "tests": [
                    {
                        "input": 0,
                        "expected": [[1]],
                        "points": 4
                    },
                    {
                        "input": 1,
                        "expected": [[1],[1,1]],
                        "points": 4
                    },
                    {
                        "input": 5,
                        "expected": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]],
                        "points": 4
                    },
                    {
                        "input": 7,
                        "expected": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]],
                        "points": 4
                    }
                ]
            }
        ]
memory_refresher = (
    "\n\n################ DONT FORGET ############\n"
    "## 5 points: Name, 5 points: Pledge    ##\n"
    "## 5 points: Docstrings (per function) ##\n"
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

    print ("\nRunning test cases: 16 points for test_pascal_row...")
    hw4.test_pascal_row()
    print("Success!")
    print("\nRunning test cases: 16 points for test_pascal_triangle...")
    hw4.test_pascal_triangle()
    print("Success!")

    print ("\n\n##### TESTING COMPLETE ######")
    print ("## Final Code Score: %s/%s ##" % (final_assign_points+32, possible_assign_points+32))
    print ("#############################\n")
    

if __name__ == '__main__':
    print (memory_refresher)
    run_all_tests()
