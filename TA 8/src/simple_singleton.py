class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Example usage:
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(singleton_instance1 is singleton_instance2)  # Output will be: True

# # also works but problematic!
# # Java style
# class Singleton:
#     _instance = None
#
#     def __init__(self):
#         # Private constructor
#         if Singleton._instance is not None:
#             raise Exception("This class is a singleton!")
#         Singleton._instance = self
#
#     @staticmethod
#     def get_instance():
#         if Singleton._instance is None:
#             Singleton()
#         return Singleton._instance
#
#
# # Example usage:
# singleton_instance1 = Singleton.get_instance()
# singleton_instance2 = Singleton.get_instance()
#
# print(singleton_instance1 is singleton_instance2)  # Output will be: True
