from typing import Dict, Union, Tuple

class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right
    
    def __str__(self) -> str:
        return f"left: {self.left}, right: {self.right}"

def get_characters_by_frequency(input_string: str) -> Dict[str, int]:
    table = dict()
    for character in input_string:
        if character.lower() in table:
             table[character.lower()] += 1
        else:
            table[character.lower()] = 1
    return sorted(table.items(), key=lambda x: x[1], reverse=True)

def get_huffman_tree(input_string: str) -> TreeNode:
    nodes = get_characters_by_frequency(input_string)
    while len(nodes) > 1:
        left, left_freq = nodes[-1]
        right, right_freq = nodes[-2]
        nodes = nodes[:-2]
        node = TreeNode(left, right)
        nodes.append((node, left_freq + right_freq))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    return nodes[0][0]

def get_tree_code(node, binary_string: str='') -> Dict[str, str]:
    if type(node) is str:
        return {node: binary_string}
    left, right = node.children()
    codes_map = dict()
    codes_map.update(get_tree_code(left, binary_string + '0'))
    codes_map.update(get_tree_code(right, binary_string + '1'))
    return codes_map
    

if __name__ == '__main__':
   input_string = "Some string with many e and t letters"
   top_node = get_huffman_tree(input_string)
   codes_map = get_tree_code(top_node)
   print(codes_map)