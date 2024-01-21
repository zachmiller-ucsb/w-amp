import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

if __name__ == '__main__':
    # data
    c = [0.9, 0.8, 0.7, 0.6, 0.5]

    point_read_latencies = [15.780, 15.665, 15.515, 34.514, 32.524]
    small_scan_latencies = [33.139, 33.947, 34.741, 71.807, 63.325]
    large_scan_latencies = [98.946, 102.235, 110.382, 121.016, 132.651]

    fig, axes = plt.subplots(3, 1, figsize=(8, 6))

    # Point Read
    axes[0].plot(c, point_read_latencies)
    axes[0].set_title('Point Reads: readrandom')

    # Small scans
    axes[1].plot(c, small_scan_latencies)
    axes[1].set_title('Small Scans: seekrandom, seek_nexts=10')

    # Large scans
    axes[2].plot(c, large_scan_latencies)
    axes[2].set_title('Large Scans: seekrandom, seek_nexts=100')

    # Set the x ticks
    for ax in axes:
        ax.set_xticks(c)

    plt.suptitle('Point/range query for T = 3, max_bytes_for_level_base = 10 MB, block cache disabled, DB size is 10GB.', fontsize='medium')
    plt.tight_layout()

    plt.savefig('micro_bench_aws')
    plt.show()

