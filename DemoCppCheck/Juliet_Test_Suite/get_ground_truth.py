#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import csv, os

# 1. Chỉnh lại đường dẫn nếu cần
MANIFEST = "manifest.xml"
OUT_CSV  = "ground_truth.csv"

tree = ET.parse(MANIFEST)
root = tree.getroot()

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "line", "id"])

    # 2. Với mỗi testcase, duyệt từng <file>
    for tc in root.findall("testcase"):
        for file_el in tc.findall("file"):
            flaw_el = file_el.find("flaw")
            if flaw_el is None:
                # bỏ qua file không có flaw
                continue

            path_attr = file_el.get("path")     # VD: CWE114_..._52c.c
            line_attr = flaw_el.get("line")     # VD: "53"
            # name="CWE-114: Process Control" -> lấy CWE-114 rồi bỏ dấu '-'
            name_attr = flaw_el.get("name").split(":", 1)[0]
            cwe_id    = name_attr.replace("-", "")  # VD: "CWE114"

            # 3. Ghi vào CSV
            writer.writerow([path_attr, line_attr, cwe_id])

print(f"Đã tạo file {OUT_CSV}")
