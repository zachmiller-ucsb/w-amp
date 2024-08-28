import matplotlib.pyplot as plt
import sys

def read_numbers(file_path, max_size_gb):
    numbers = []
    with open(file_path, 'r') as file:
      for line in file:
        line_split = line.split()
        if line_split[1] == 'GB' and float(line_split[0]) > max_size_gb:
           break
        numbers.append(float(line_split[2]))
    return numbers

def plot_numbers(rocks, autumn_6):
    indices_rocks = range(1, len(rocks) + 1)
    indices_6 = range(1, len(autumn_6) + 1)
    
    # Plot both datasets
    plt.plot(indices_rocks, rocks, linestyle='-', color='b', label="RocksDB")
    plt.plot(indices_6, autumn_6, linestyle='-', color='r', label="Autumn 0.6")
    
    plt.title("Write Amplification Comparison")
    plt.xlabel("Time (min)")
    plt.ylabel("Sum W-amp")
    plt.grid(True)
    
    # Add legend
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    path_rocks = sys.argv[1]  
    rocks = read_numbers(path_rocks, 200)

    path_autumn = sys.argv[2]  
    autumn_6 = read_numbers(path_autumn, 200)
    
    plot_numbers(rocks, autumn_6)
