benchmarks = ["specbzip", "spechmmer", "speclibm", "specmcf", "specsjeng"]

with open("graphs/results.py", "w") as file_write:
    file_write.write("results = [")
    for benchmark in benchmarks:
        for i in range(6):
            file_read_path = "gem5_to_mcpat/" + benchmark + "_" + str(i) + ".txt"
            with open(file_read_path, "r") as file_read:
                lines = file_read.readlines()
                for line in lines:
                    if "Peak Power" in line:
                        value = line.split()[3]
                        file_write.write(f"{value}, ")
                        break
    file_write.write("]")
