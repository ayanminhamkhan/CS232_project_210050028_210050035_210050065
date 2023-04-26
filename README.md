# CS232_project_210050028_210050035_210050065

# Download traces

To run Champsim you need traces 

1. Download traces from https://www.dropbox.com/sh/xs2t9y4cuqlgrlp/AACpzGOj6BcSB-BUolGaBjbta?dl=0 . Download only traces 'cadical-high-60K-134B.champsimtrace.xz', 'cadical-high-60K-1227B.champsimtrace.xz', 'kissat-inc-high-30K-1802B.champsimtrace.xz' in 'back-end-bound' folder.

2. Make a folder named 'dpc3-traces' . Move these traces into folder named 'dpc3-traces'.

3. Run any of these 3 traces as required

# How to Make Cache Hierarchy Inclusive, Non-Inclusive or Exclusive

To simulate cache hierarchy in different modes, follow these steps:

1. Go to the `/src` folder, where you will find three `.txt` files named `cache_inc.txt`, `cache_noninc.txt`, and `cache_excl.txt`.

2. Depending on the mode you want to simulate (inclusive, non-inclusive, or exclusive), copy the contents of the respective file (`cache_inc.txt`, `cache_noninc.txt`, or `cache_excl.txt`) into `cache.cc`.

3. Once you have made the necessary changes in `cache.cc`, run `champsim` as intended to simulate the cache hierarchy in the desired mode. 

Note that the choice of cache hierarchy mode (inclusive, non-inclusive, or exclusive) depends on the specific use case and the performance goals of the system being simulated.


# How to change set size of cache 

To change size of cache 

1. Go to the '/inc' folder, where you will find 'cache.h' file.

2. In 'cache.h' file, to change size of L1, L2, or LLC caches change 'L1d_SET', 'L1d_WAY, 'L2C_SET', 'L2C_WAY', 'LLC_SET' or 'LLC_WAY' variables as neccessary.

# Compile

```
$ chmod +x build_champsim.sh
```

ChampSim takes seven parameters: Branch predictor, L1I prefetcher, L1D prefetcher, L2C prefetcher, LLC prefetcher, LLC replacement policy, and the number of cores. 
For example, `./build_champsim.sh bimodal no no no next_line lru 1` builds a single-core processor with bimodal branch predictor, no L1 instruction prefetcher, no L1/L2 data prefetchers, ip-stride LLC prefetcher and the baseline LRU replacement policy for the LLC.
```
$ ./build_champsim.sh bimodal no no no next_line lru 1

$ ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE}
```

# Run simulation

Execute `run_champsim.sh` with proper input arguments. The default `TRACE_DIR` in `run_champsim.sh` is set to `$PWD/dpc3_traces`. <br>

* Single-core simulation: Run simulation with `run_champsim.sh` script.

```
Usage: ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
$ ./run_champsim.sh bimodal-no-no-no-next_line-lru-1core 1 10 600.perlbench_s-210B.champsimtrace.xz

${BINARY}: ChampSim binary compiled by "build_champsim.sh" (bimodal-no-no-no-next_line-lru-1core)
${N_WARM}: number of instructions for warmup (1 million)
${N_SIM}:  number of instructinos for detailed simulation (10 million)
${TRACE}: trace name (600.perlbench_s-210B.champsimtrace.xz)
${OPTION}: extra option for "-low_bandwidth" (src/main.cc)
```
Simulation results will be stored under "results_${N_SIM}M" as a form of "${TRACE}-${BINARY}-${OPTION}.txt".<br> 
