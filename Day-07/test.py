import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, this will incurr charge for you 2$/day")

elif type == "t2.medium":
    print("ok, this will incurr charge for you 4$/day")

elif type == "t2.xlarge":
    print("ok, this will incurr charge for you 6$/day")

else:
    print("Please provide a valid instance type")