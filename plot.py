import matplotlib.pyplot as plt
import sys

def read_wamp(file_path, max_size_gb):
    wamp, gb_wrtn = [], []
    with open(file_path, 'r') as file:
      for line in file:
        line_split = line.split()
        if line_split[1] == 'GB' and float(line_split[0]) > max_size_gb:
           break
        wamp.append(float(line_split[3]))
        gb_wrtn.append(float(line_split[2]))
    return wamp, gb_wrtn

def read_iostat(file_path, num_lines):
    gb_total_wrtn = []
    with open(file_path, 'r') as file:
        line_no = 0
        baseline = None
        for line in file:
            if line_no == num_lines + 1:
                break
            kb_wrtn = float(line.strip())
            if baseline is None:
                baseline = kb_wrtn
            else:
                gb_total_wrtn.append((kb_wrtn - baseline) / pow(10, 6))
            line_no += 1
    return gb_total_wrtn

def read_levels(file_path, num_lines):
    levels = []
    with open(file_path, 'r') as file:
        line_no = 0
        for line in file:
            if line_no == num_lines:
                break
            levels.append(float(line.strip()))
            line_no += 1
    return levels

def plot(wamp_rocks, levels_rocks, gc_wamp_rocks, wamp_6, levels_6, gc_wamp_6, wamp_8, levels_8, gc_wamp_8):
    indices_rocks = range(1, len(wamp_rocks) + 1)
    indices_6 = range(1, len(wamp_6) + 1)
    indices_8 = range(1, len(wamp_8) + 1)
    
    _, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
    
    ax1.plot(indices_rocks, wamp_rocks, linestyle='-', color='b', label="RocksDB")
    ax1.plot(indices_6, wamp_6, linestyle='-', color='r', label="Autumn 0.6")
    ax1.plot(indices_8, wamp_8, linestyle='-', color='g', label="Autumn 0.8")
    
    ax1.set_title("Write Amplification")
    ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Sum W-amp")
    ax1.grid(True)
    ax1.legend()

    ax2.plot(indices_rocks, levels_rocks, linestyle='-', color='b', label="RocksDB")
    ax2.plot(indices_6, levels_6, linestyle='-', color='r', label="Autumn 0.6")
    ax2.plot(indices_8, levels_8, linestyle='-', color='g', label="Autumn 0.8")

    ax2.set_title("Levels")
    ax2.set_xlabel("Time (min)")
    ax2.set_ylabel("Number of Levels")
    ax2.grid(True)
    ax2.legend()

    ax3.plot(indices_rocks, gc_wamp_rocks, linestyle='-', color='b', label="RocksDB")
    ax3.plot(indices_6, gc_wamp_6, linestyle='-', color='r', label="Autumn 0.6")
    ax3.plot(indices_8, gc_wamp_8, linestyle='-', color='g', label="Autumn 0.8")

    ax3.set_title("GC Write Amplification")
    ax3.set_xlabel("Time (min)")
    ax3.set_ylabel("GC W-amp")
    ax3.set_ylim(bottom=1.0)
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    wamp_rocks, gb_wrtn_rocks = read_wamp(sys.argv[1], 200)
    levels_rocks = read_levels(sys.argv[2], len(wamp_rocks))
    writes_rocks = read_iostat(sys.argv[3], len(wamp_rocks))
    gc_wamp_rocks = [writes_rocks[i] / gb_wrtn_rocks[i] for i in range(len(wamp_rocks))]

    wamp_6, gb_wrtn_6 = read_wamp(sys.argv[4], 200)
    levels_6 = read_levels(sys.argv[5], len(wamp_6))
    writes_6 = read_iostat(sys.argv[6], len(wamp_6))
    gc_wamp_6 = [writes_6[i] / gb_wrtn_6[i] for i in range(len(wamp_6))]

    wamp_8, gb_wrtn_8 = read_wamp(sys.argv[7], 200)
    levels_8 = read_levels(sys.argv[8], len(wamp_8))
    writes_8 = read_iostat(sys.argv[9], len(wamp_8))
    gc_wamp_8 = [writes_8[i] / gb_wrtn_8[i] for i in range(len(wamp_8))]
    
    plot(wamp_rocks, levels_rocks, gc_wamp_rocks, wamp_6, levels_6, gc_wamp_6, wamp_8, levels_8, gc_wamp_8)
