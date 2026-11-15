# USN: 25BTRAD133
# Lab Exercise 11: Log File Reader Program

def analyze_log(filename):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        with open(filename, 'r') as f:
            for line in f:
                for k in counts:
                    if k in line: counts[k] += 1
        print("\n--- Log Summary ---")
        for k, v in counts.items(): print(f"{k}: {v}")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    analyze_log("app.log")