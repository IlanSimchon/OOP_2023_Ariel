import psutil
import matplotlib.pyplot as plt


class SingletonInit:
    _instance = None
    numbers = [x for x in range(10000)]

    def __init__(self):
        if SingletonInit._instance is not None:
            raise Exception("This class is a singleton!")
        SingletonInit._instance = self

    @staticmethod
    def get_instance():
        if SingletonInit._instance is None:
            SingletonInit._instance = SingletonInit()
        return SingletonInit._instance


class SingletonNew:
    _instance = None
    numbers = [x for x in range(10000)]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonNew, cls).__new__(cls)
        return cls._instance

def measure_memory_usage(create_instance_func, num_instances):
    memory_usage = []
    for _ in range(num_instances):
        instance = create_instance_func()
        # Adding a manual garbage collection step to release the instance
        del instance
        memory_usage.append(psutil.Process().memory_info().rss)
    return memory_usage

num_instances = 1000  # Reduced number of instances for demonstration

# Measure memory usage for SingletonInit
memory_usage_init = measure_memory_usage(SingletonInit.get_instance, num_instances)

# Measure memory usage for SingletonNew
memory_usage_new = measure_memory_usage(SingletonNew, num_instances)

# Plot the results
plt.plot(memory_usage_init, label='SingletonInit')
plt.plot(memory_usage_new, label='SingletonNew')
plt.xlabel('Number of Instances Created')
plt.ylabel('Memory Usage (bytes)')
plt.title('Memory Usage Comparison')
plt.legend()
plt.grid(True)
plt.show()
