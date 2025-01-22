from collections import defaultdict, deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif self.right is None:
            self.right = Node(value)
        else:
            self.right.insert(value)

    def inorder(self) -> list[int]:
        items = []

        if self.left:
            items += self.left.inorder()

        items.append(self.value)

        if self.right:
            items += self.right.inorder()

        return items

    def inorder_no_recursion(self) -> list[int]:
        items = []
        stack = []
        current = self

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            items.append(current.value)
            current = current.right

        return items

    def preorder(self) -> list[int]:
        items = []
        items.append(self.value)

        if self.left:
            items += self.left.preorder()
        if self.right:
            items += self.right.preorder()

        return items

    def preorder_no_recursion(self) -> list[int]:
        items = []
        stack = [self]

        while stack:
            current = stack.pop()
            items.append(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return items

    def postorder(self) -> list[int]:
        items = []

        if self.left:
            items += self.left.postorder()
        if self.right:
            items += self.right.postorder()

        items.append(self.value)

        return items

    def postorder_no_recursion(self) -> list[int]:
        items = []
        stack1 = [self]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            current = stack2.pop()
            items.append(current.value)

        return items

    def level_order(self) -> dict[int, list[int]]:
        if self.left is None and self.right is None:
            return {0: [self.value]}

        result = defaultdict(list)
        queue = deque([self])
        level = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                result[level].append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return result

    def depth(self) -> int:
        left = 0
        right = 0
        if self.left:
            left = self.left.depth() + 1
        if self.right:
            right = self.right.depth() + 1

        return max(left, right)


t = Node(3)
t.insert(4)
t.insert(1)
t.insert(2)
t.insert(5)

print("in order:")
print(t.inorder())
print("in order no recursion")
print(t.inorder_no_recursion())
print("pre order:")
print(t.preorder())
print("pre order no recursion:")
print(t.preorder_no_recursion())
print("post order:")
print(t.postorder())
print("post order no recursion:")
print(t.postorder_no_recursion())
print("level order:")
result = t.level_order()
[print(l, nodes) for l, nodes in t.level_order().items()]
print("depth:")
print(Node.depth(t))
