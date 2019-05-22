class Node:
    def __init__(self):
        pass
    
    def evaluate(self):
        pass
        
    def execute(self):
        pass


class IntegerNode(Node):
    def __init__(self, value):
        self.value = int(value)
    
    def evaluate(self):
        return self.value


class DecimalNode(Node):
    def __init__(self, value):
        self.value = float(value)
    
    def evaluate(self):
        return self.value


class CharacterNode(Node):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        return self.value


class StringNode(Node):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self):
        return self.value


class PrintNode(Node):
    def __init__(self, value):
        self.value = value
    
    def execute(self):
        self.value = self.value.evaluate()
        print(self.value)


class TempNode(Node):
    def __init__(self, sl):
        self.sl = sl
    
    def execute(self):
        for s in self.sl:
            s.execute()

class BlockNode(Node):
    def __init__(self, sl = None):
        self.sl = sl
    
    def execute(self):
        if self.sl:
            for s in self.sl:
                s.execute()


class ProgramNode(Node):
    def __init__(self, block):
        self.block = block
    
    def __init__(self):
        self.block.execute()

