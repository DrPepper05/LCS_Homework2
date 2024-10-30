from binarytree import Node

def is_wff(s):
    binary_connectives = {"⇔", "⇒", "∨", "∧"}
    unary_connectives = {"¬"}

    stack = []
    root = None

    i = 0
    length = len(s)

    while i < length:
        char = s[i]

        if char.isspace():
            i += 1
            continue

        if char == '(':
            # Create a new node with placeholder '#'
            new_node = Node('#')
            if not stack:
                # This is the root node
                root = new_node
            else:
                parent_node, state = stack[-1]
                if state == 'expect_subformula1':
                    if parent_node.left is None:
                        parent_node.left = new_node
                    else:
                        return False, f"Error: Parent node already has left child at position {i}."
                elif state == 'expect_subformula2':
                    if parent_node.right is None:
                        parent_node.right = new_node
                    else:
                        return False, f"Error: Parent node already has right child at position {i}."
                else:
                    return False, f"Error: Unexpected '(' at position {i}."
            # Push the new node with expectation to assign subformula1
            stack.append((new_node, 'expect_subformula1'))
            print(f"Step {i}: Encountered '('. Created new node '#'")
            print_tree(root)
            print("\n" + "-"*50 + "\n")
            i += 1

        elif char in binary_connectives:
            if not stack:
                return False, f"Error: connective '{char}' at position {i} without a corresponding '('."
            current_node, state = stack[-1]
            if state != 'expect_connective':
                return False, f"Error: connective '{char}' at position {i} not expected."
            if current_node.value != '#':
                return False, f"Error: connective '{current_node.value}' assigned to node at position {i}."
            current_node.value = char
            if char in binary_connectives:
                # Binary connective expects subformula2 next
                if current_node.left is None or current_node.left.value == '#':
                    return False, f"Error: Binary connective '{char}' at position {i} requires a left subformula."
                # Push the current node with expectation to assign subformula2
                stack[-1] = (current_node, 'expect_subformula2')
            print(f"Step {i}: Encountered connective '{char}'. Assigned to upper node.")
            print_tree(root)
            print("\n" + "-"*50 + "\n")
            i += 1
        elif char in unary_connectives:
        # Unary connective expects subformula1 next (only left subformula)
            if not stack:
                return False, f"Error: connective '{char}' at position {i} without a corresponding '('."
            current_node, state = stack[-1]
            current_node.value = char
            if current_node.left is not None:
                return False, f"Error: Unary connective '{char}' at position {i} already has a left subformula."
                # Push the current node with expectation to assign subformula1
            stack[-1] = (current_node, 'expect_subformula1')
            print(f"Step {i}: Encountered connective '{char}'. Assigned to a new node.")
            print_tree(root)
            print("\n" + "-"*50 + "\n")
            i += 1
        elif char.isalpha():
            if not stack:
                return True, f"{char} is a well formed formula"
            current_node, state = stack[-1]
            if state == 'expect_subformula1':
                if current_node.left is None:
                    # Assign subformula to left child
                    current_node.left = Node(char)
                else:
                    return False, f"Error: Left subformula already assigned for connective '{current_node.value}' at position {i}."
                # After assigning subformula1, expect connective
                stack[-1] = (current_node, 'expect_connective')
            elif state == 'expect_subformula2':
                if current_node.right is None:
                    # Assign subformula to right child
                    current_node.right = Node(char)
                else:
                    return False, f"Error: Right subformula already assigned for connective '{current_node.value}' at position {i}."
                # After assigning subformula2, state is done
                stack[-1] = (current_node, 'done')
            else:
                return False, f"Error: subformula '{char}' at position {i} not expected."
            print(f"Step {i}: Encountered subformula '{char}'. Assigned to a new node.")
            print_tree(root)
            print("\n" + "-"*50 + "\n")
            i += 1
        elif char == ')':
            if not stack:
                return False, f"Error: Unmatched closing parenthesis ')' at position {i}."
            current_node, state = stack.pop()
            if stack:
                parent_node, parent_state = stack[-1]
                if parent_state == 'expect_subformula1':
                    # After assigning subformula1, expect connective
                    stack[-1] = (parent_node, 'expect_connective')
                elif parent_state == 'expect_subformula2':
                    # After assigning subformula2, state is done
                    stack[-1] = (parent_node, 'done')
            print(f"Step {i}: Encountered ')'. Going up in the binary tree")
            print_tree(root)
            print("\n" + "-"*50 + "\n")
            i += 1

        else:
            return False, f"Error: Invalid character '{char}' at position {i}."

    if stack:
        return False, "Error: Unmatched opening parenthesis '(' remaining in stack."

    if root:
        if root.value == "#":
            return False , "The compound formula has an extra pair of parantheses"
        return True, ""
    else:
        return False, "Error: No valid formula found."

def print_tree(root):
    if root is None:
        print("Empty Tree")
    else:
        print(root)

if __name__ == "__main__":
    test_strings = [
        "(((P ⇒ Q) ∨ S) ⇔ T)", 
        "((P ⇒ (Q ∧ (S ⇒ T))))",
        "(¬(B(¬Q)) ∧ R)",                  
        "((P ⇒ Q) ∧ ((¬Q) ∧ P))",                   
        "((P ⇒ Q) ⇒ (Q ⇒ P))",                       
        #"((((((A ∧ W) ⇒ P) ∧ ((¬A) ⇒ I)) ∧ ((¬W) ⇒ M)) ∧ (¬P)) ∧ (E ⇒ ((¬I) ∧ (¬M))))"                                                     
    ]

    for idx, string in enumerate(test_strings, 1):
        print("\n" + "="*50)
        print(f"Test Case {idx}: '{string}'\n")
        res, msg = is_wff(string)
        if res:
            print(f"Result: '{string}' is a well-formed formula.\n")
        else:
            print(f"Result: '{string}' is NOT a well-formed formula. Reason: {msg}\n")