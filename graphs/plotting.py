import matplotlib.pyplot as plt
from results import results

benchmarks = ["specbzip", "spechmmer", "speclibm", "specmcf", "specsjeng"]

for i in range(len(benchmarks)):
    data_graph = []
    for j in range(6):
        data_graph.append(results[i * 6 + j])

    instances = list(range(6))
    fig_path = "graphs/pngs/" + benchmarks[i]
    plt.bar(instances, data_graph)
    plt.title("Peak power for " + benchmarks[i] + " benchmarks")
    plt.xlabel("Instance")
    plt.ylabel("Peak power")
    plt.savefig(fig_path)
    plt.close()
