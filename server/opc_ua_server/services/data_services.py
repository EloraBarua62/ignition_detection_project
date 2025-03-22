class DataService:
    @staticmethod
    def update_variable(node, value):
        node.set_value(value)
        print(f"Variable updated to: {value}")