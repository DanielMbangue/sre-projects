def read_log_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def count_error_types(lines):
    error_counts = {}
    unique_errors = set()
    for line in lines:
        unique_errors.add(line)
        level = line.split()[0]
        if level in error_counts:
            error_counts[level] += 1
        else:
            error_counts[level] = 1
    return error_counts, unique_errors

    

def main():
    try:
        lines = read_log_file('sample.log')
        print(f"Total lines: {len(lines)}")

        counts,unique_errors = count_error_types(lines)
        print("\nError type breakdown:")

        
        for level, count in counts.items():
            print(f" {level}: {count}")    

        print(f"\nTotal Unique Errors: {len(unique_errors)}")  
    except FileNotFoundError:
        print("Error: log file not found")
main()

