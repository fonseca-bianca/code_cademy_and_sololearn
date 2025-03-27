"""
When should you use static methods instead of class methods? Static methods don't accept the 'cls' parameter, meaning they can't access or modify the class's state. They are useful when you require functionality that doesn't depend on the class's behavior or instance state and doesn't affect it. Essentially, static methods are suited for tasks that are self-contained and do not require knowledge of the class or instance.
1- Complete the static method signature:
"""

@staticmethod
def play_credits(film):
    print(f"Playing credits for {film}.")