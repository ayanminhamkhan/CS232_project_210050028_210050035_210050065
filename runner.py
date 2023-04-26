import os

# Now LLC_WAYS = 16

# os.system("mkdir FINAL_RESULTS")

# LRU
os.system("./build_champsim.sh bimodal no no no no lru 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 cadical-high-60K-113B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt ./FINAL_RESULTS/113_lru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 cadical-high-60K-134B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-134B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt ./FINAL_RESULTS/134_lru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 cadical-high-60K-1227B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-1227B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt ./FINAL_RESULTS/1227_lru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 kissat-inc-high-30K-1802B.champsimtrace.xz")
os.system("mv ./results_10M/kissat-inc-high-30K-1802B.champsimtrace.xz-bimodal-no-no-no-no-lru-1core.txt ./FINAL_RESULTS/1802_lru.txt")


# LFU
os.system("./build_champsim.sh bimodal no no no no lfu 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-lfu-1core 1 10 cadical-high-60K-113B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-lfu-1core.txt ./FINAL_RESULTS/113_lfu.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lfu-1core 1 10 cadical-high-60K-134B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-134B.champsimtrace.xz-bimodal-no-no-no-no-lfu-1core.txt ./FINAL_RESULTS/134_lfu.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lfu-1core 1 10 cadical-high-60K-1227B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-1227B.champsimtrace.xz-bimodal-no-no-no-no-lfu-1core.txt ./FINAL_RESULTS/1227_lfu.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-lfu-1core 1 10 kissat-inc-high-30K-1802B.champsimtrace.xz")
os.system("mv ./results_10M/kissat-inc-high-30K-1802B.champsimtrace.xz-bimodal-no-no-no-no-lfu-1core.txt ./FINAL_RESULTS/1802_lfu.txt")

# FIFO
os.system("./build_champsim.sh bimodal no no no no fifo 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-fifo-1core 1 10 cadical-high-60K-113B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-fifo-1core.txt ./FINAL_RESULTS/113_fifo.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-fifo-1core 1 10 cadical-high-60K-134B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-134B.champsimtrace.xz-bimodal-no-no-no-no-fifo-1core.txt ./FINAL_RESULTS/134_fifo.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-fifo-1core 1 10 cadical-high-60K-1227B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-1227B.champsimtrace.xz-bimodal-no-no-no-no-fifo-1core.txt ./FINAL_RESULTS/1227_fifo.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-fifo-1core 1 10 kissat-inc-high-30K-1802B.champsimtrace.xz")
os.system("mv ./results_10M/kissat-inc-high-30K-1802B.champsimtrace.xz-bimodal-no-no-no-no-fifo-1core.txt ./FINAL_RESULTS/1802_fifo.txt")


# RAND
os.system("./build_champsim.sh bimodal no no no no rand 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-rand-1core 1 10 cadical-high-60K-113B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-rand-1core.txt ./FINAL_RESULTS/113_rand.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-rand-1core 1 10 cadical-high-60K-134B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-134B.champsimtrace.xz-bimodal-no-no-no-no-rand-1core.txt ./FINAL_RESULTS/134_rand.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-rand-1core 1 10 cadical-high-60K-1227B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-1227B.champsimtrace.xz-bimodal-no-no-no-no-rand-1core.txt ./FINAL_RESULTS/1227_rand.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-rand-1core 1 10 kissat-inc-high-30K-1802B.champsimtrace.xz")
os.system("mv ./results_10M/kissat-inc-high-30K-1802B.champsimtrace.xz-bimodal-no-no-no-no-rand-1core.txt ./FINAL_RESULTS/1803_rand.txt")


# MRU

os.system("./build_champsim.sh bimodal no no no no mru 1")
os.system("./run_champsim.sh bimodal-no-no-no-no-mru-1core 1 10 cadical-high-60K-113B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-113B.champsimtrace.xz-bimodal-no-no-no-no-mru-1core.txt ./FINAL_RESULTS/113_mru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-mru-1core 1 10 cadical-high-60K-134B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-134B.champsimtrace.xz-bimodal-no-no-no-no-mru-1core.txt ./FINAL_RESULTS/134_mru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-mru-1core 1 10 cadical-high-60K-1227B.champsimtrace.xz")
os.system("mv ./results_10M/cadical-high-60K-1227B.champsimtrace.xz-bimodal-no-no-no-no-mru-1core.txt ./FINAL_RESULTS/1227_mru.txt")

os.system("./run_champsim.sh bimodal-no-no-no-no-mru-1core 1 10 kissat-inc-high-30K-1802B.champsimtrace.xz")
os.system("mv ./results_10M/kissat-inc-high-30K-1802B.champsimtrace.xz-bimodal-no-no-no-no-mru-1core.txt ./FINAL_RESULTS/1803_mru.txt")