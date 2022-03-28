import importlib
import os
import sys


def import_module(filename: str):
    name, extension = os.path.splitext(filename)

    module = importlib.import_module(f"tests.{name}")
    return module


def main():
    failed_tests = []

    for root, dirs, files in os.walk("."):
        if root == ".":
            print(f"Performing {len([file for file in files if file.startswith('test')])} tests...")

            for file in files:
                if file.startswith("test"):
                    module = import_module(file)
                    
                    try:
                        module.test()
                    except Exception as e:
                        failed_tests.append({"filename": file, "exception": e})

    if len(failed_tests) != 0:
        print("An error occurred in the following test files:")

        for test in failed_tests:
            print(f"- {test['filename']}, {test['exception']}")
    else:
        print("0 errors occurred while running tests.")


if __name__ == "__main__":
    # Change the system path for the imports to work
    sys.path.append("../")

    main()
