import pandas as pd


def kha_nang_cho_vay(a, b, c):
    if a < 150 or a > 750 or b < 0.01 or b > 1000.00 or c < 0.00 or c > 100.00:
        return "Đầu vào không hợp lệ"
    if a < 430 and b >= 600 and c <= 70.00:
        return "Không phê duyệt vay"
    if a >= 570 and b <= 50 and c >= 90.00:
        return "Cho vay với lãi thấp"
    return "Cho vay với lãi cao"

test_cases = pd.read_csv("kha_nang_cho_vay_testcases.csv", delimiter=",")
print(test_cases)


for (test_id, a, b, c, EO) in test_cases.itertuples(index=False):
    if kha_nang_cho_vay(a, b, c) == EO:
        print(f"Test case {test_id} - Passed")
    else:
        print(f"Test case {test_id} - Failed")
        print(f"Expected output: {EO}")
        print(f"Real output: {kha_nang_cho_vay(a, b, c)}")
