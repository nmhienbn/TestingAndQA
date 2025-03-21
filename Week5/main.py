import pandas as pd

def Pow(a, b, mod):
    ans = 1
    while b > 0:
        if b % 2:
            ans = ans * a % mod
        a = a * a % mod
        b //= 2
    return ans


test_cases = pd.read_csv("testcases.csv", delimiter=",")
print(test_cases)


for (test_id, a, b, mod, EO) in test_cases.itertuples(index=False):
    if Pow(a, b, mod) == EO:
        print(f"Test case {test_id} - Passed")
    else:
        print(f"Test case {test_id} - Failed")
        print(f"Expected output: {EO}")
        print(f"Real output: {Pow(a, b)}")
