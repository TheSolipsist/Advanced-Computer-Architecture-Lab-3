import matplotlib.pyplot as plt
from results import results

benchmarks = ["specbzip", "spechmmer", "speclibm", "specmcf", "specsjeng"]

for i in range(len(benchmarks)):
    data_graph = []
    for j in range(6):
        curr_dict = results[i * 6 + j]
        data_graph.append(curr_dict["energy"] * curr_dict["runtime"])

    instances = list(range(6))
    fig_path = "important_results/graphs/" + benchmarks[i]
    plt.bar(instances, data_graph)
    plt.title("EDP for " + benchmarks[i] + " benchmarks")
    plt.xlabel("Instance")
    plt.ylabel("EDP")
    plt.savefig(fig_path)
    plt.close()


