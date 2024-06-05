class God:
    _instance = None

    def __new__(cls):
        # If an instance does not exist, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def create_world(self):
        print("Creating the world")

    def destroy_world(self):
        print("Destroying the world")


# Client code using the Singleton God class
def main():
    god_instance1 = God()
    god_instance1.create_world()

    god_instance2 = God()
    god_instance2.destroy_world()

    # Both instances refer to the same object
    print(god_instance1 is god_instance2)  # Output: True


if __name__ == "__main__":
    main()
