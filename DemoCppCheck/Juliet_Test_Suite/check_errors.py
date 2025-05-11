import xml.etree.ElementTree as ET
import csv, argparse, os, sys

def parse_ground_truth(manifest_path):
    """
    Đọc manifest.xml, trả về set của tuples (basename, line)
    """
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    truth = set()
    for tc in root.findall("testcase"):
        for file_el in tc.findall("file"):
            flaw_el = file_el.find("flaw")
            if flaw_el is None:
                continue
            path = file_el.get("path")
            fn   = os.path.basename(path)
            line = flaw_el.get("line")
            truth.add((fn, line))
    return truth

def parse_cppcheck(xml_path):
    """
    Đọc cppcheck.xml, trả về set của tuples (basename, line)
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    detected = set()
    for error in root.findall('errors/error'):
        loc = error.find('location')
        if loc is None: continue
        path = loc.get('file')
        fn   = os.path.basename(path)
        line = loc.get('line')
        detected.add((fn, line))
    return detected

def compute_metrics(detected, truth):
    total = len(detected | truth)
    TP = len(detected & truth) / total if total > 0 else 0.0
    FP = len(detected - truth) / total if total > 0 else 0.0
    FN = len(truth - detected) / total if total > 0 else 0.0
    P  = TP/(TP+FP) if (TP+FP)>0 else 0.0
    R  = TP/(TP+FN) if (TP+FN)>0 else 0.0
    return TP, FP, FN, P, R

def main():
    p = argparse.ArgumentParser(
        description="Tính Precision/Recall cho Cppcheck trên Juliet v1.3"
    )
    p.add_argument('--manifest', required=True,
                   help="Đường dẫn tới manifest.xml của Juliet v1.3")
    p.add_argument('--xml',      required=True,
                   help="Đường dẫn tới output XML của Cppcheck (cppcheck.xml)")
    args = p.parse_args()

    if not os.path.isfile(args.manifest):
        sys.exit(f"Không tìm thấy manifest: {args.manifest}")
    if not os.path.isfile(args.xml):
        sys.exit(f"Không tìm thấy xml: {args.xml}")

    truth    = parse_ground_truth(args.manifest)
    detected = parse_cppcheck(args.xml)
    TP, FP, FN, P, R = compute_metrics(detected, truth)

    print(f"Precision: {P:.2f}")
    print(f"Recall:    {R:.2f}")
    print(f"TP={TP}, FP={FP}, FN={FN}")

if __name__ == "__main__":
    main()