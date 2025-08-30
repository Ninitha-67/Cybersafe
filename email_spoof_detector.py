def detect_spoof(header):
    print("\n[+] Analyzing email header....")
    if "Received-SPF: fail" in header or "spf=fail" in header:
        print("Possible spoof detected: DKIM failed. ")
    elif "DKIM=fail" in header.lower():
        print("Possible spoof detected: DKIM failed. ")
    else:
        print("No obious spoofing detected (but not guranteed safe).")


if __name__ == "__main__":
    print("Paste your full email header below (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    raw_header = "\n".join(lines)
    detect_spoof(raw_header)