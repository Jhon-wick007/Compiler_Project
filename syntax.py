import re

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def parse_expr(tokens):
    node = parse_term(tokens)
    if tokens and tokens[0] in ['+', '-']:
        op = tokens.pop(0)
        node_op = Node(op)
        node_op.children.append(node)
        node_op.children.append(parse_expr(tokens))
        node = node_op
    return node

def parse_term(tokens):
    node = parse_factor(tokens)
    if tokens and tokens[0] in ['*', '/']:
        op = tokens.pop(0)
        node_op = Node(op)
        node_op.children.append(node)
        node_op.children.append(parse_term(tokens))
        node = node_op
    return node

def parse_factor(tokens):
    if tokens[0] == '(':
        tokens.pop(0) # Consume '('
        node = parse_expr(tokens)
        tokens.pop(0) # Consume ')'
        return node
    elif re.match(r'\d+', tokens[0]):
        return Node(tokens.pop(0))
    else:
        raise ValueError("Invalid expression")

def print_tree(node, level=0):
    print("  " * level + str(node.value))
    for child in node.children:
        print_tree(child, level + 1)

def main():
    expr = "2 + (3 * 4 - 5) / 6"
    tokens = re.findall(r'\d+|\S', expr)
    root = parse_expr(tokens)
    print_tree(root)

if __name__ == "__main__":
    main()

