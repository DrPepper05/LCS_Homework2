
# Logical Formula Validator and Evaluator

## Overview

This code verifies if a given logical formula is well-formed and then evaluates its truth value based on provided interpretations. It builds a binary tree representation of logical formulas using standard logical connectives (`⇔`, `⇒`, `∨`, `∧`, `¬`) and can validate custom formulas against multiple interpretations.

## Requirements

1. **Python** 3.6 or higher
2. **Binarytree Library**:
   - Install via pip:
     ```bash
     pip install binarytree
     ```

## Setup Instructions

### For macOS, Linux, and Windows

1. **Clone or Download the Repository**: Download this file or clone the repository where this code is saved.
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies**:
   Run the following in the terminal or command prompt:
   ```bash
   pip install binarytree
   ```

   **Note**: This code depends on the `binarytree` library. If you encounter issues installing, refer to the [official documentation](https://pypi.org/project/binarytree/).

3. **Run the Script**:
   Execute the code with:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the name of the Python file containing the code.

## Code Overview

This code performs two main tasks:

1. **Check if a Formula is Well-Formed**:
   - The `is_wff` function parses a logical formula string and verifies if it adheres to the rules of well-formed formulas (WFFs).
   - It uses a stack-based approach to handle nesting and validate structure.

2. **Evaluate Formula Against Interpretations**:
   - The `treeValid` function computes the truth value of a formula using various interpretations provided as dictionaries (e.g., `interpretation1`, `interpretation2`).
   - Logical connectives (`⇔`, `⇒`, `∨`, `∧`, `¬`) are evaluated based on the binary tree representation of the formula.

## Usage Guide

### Modify Formulas

To analyze different logical formulas, you can change the strings within `test_strings`:

```python
test_strings = [
    "((P ⇒ Q) ∧ ((¬Q) ∧ (¬P)))",       # Example formula a
    "((P ⇒ Q) ⇒ ((Q ⇒ S) ⇒ ((P ∨ Q) ⇒ R)))",  # Example formula b
    "((¬(P ⇒ Q)) ⇔ ((P ∨ R) ∧ ((¬P) ⇒ Q)))",  # Example formula c
    "((P ⇔ Q) ⇔ (¬(P ⇒ (¬Q))))"         # Example formula d
]
```

Replace any formula with a custom one. Ensure it adheres to syntax rules: use `(` and `)` for grouping and include only defined connectives.

### Update Interpretations

To assign new truth values for variables, modify the interpretation dictionaries:

```python
interpretation1 = {
    'P': False,
    'Q': False,
    'S': True,
    'T': True,
    'R': True,
    'B': False
}
```

Each interpretation can include any variable (`P`, `Q`, etc.) relevant to your formula. Set each variable to either `True` or `False`.

## Functions

### `is_wff(s: str) -> Tuple[Node, bool, str]`
- **Purpose**: Verifies if the given formula string `s` is a well-formed formula.
- **Returns**:
  - A binary tree `Node` if the formula is well-formed.
  - A Boolean indicating if the formula is well-formed.
  - An error message if the formula is invalid.
- **Usage**: No changes needed unless modifying error-handling behavior or debug messages.

### `print_tree(root: Node)`
- **Purpose**: Prints a visual representation of the formula’s binary tree structure.
- **Usage**: This function is automatically called in debugging statements to show the tree at each parsing stage.

### `treeValid(node: Node, interpretation: dict) -> bool`
- **Purpose**: Calculates the truth value of a well-formed formula against a given interpretation.
- **Parameters**:
  - `node`: Root node of the binary tree representing the formula.
  - `interpretation`: Dictionary mapping variables to `True`/`False`.
- **Usage**: Used internally; modify only if adjusting logical connectives.

## Running Tests

- After defining your formulas and interpretations, run the script.
- Each formula will print a result indicating whether it is well-formed.
- For well-formed formulas, the truth value of each interpretation is displayed.

## Troubleshooting

1. **Installation Issues**:
   - Ensure you have Python 3.6 or higher.
   - Verify `binarytree` is installed; reinstall with `pip install binarytree`.

2. **Formula Parsing Errors**:
   - Ensure formulas use only the defined connectives (`⇔`, `⇒`, `∨`, `∧`, `¬`).
   - Use parentheses `(` and `)` to specify precedence.

3. **Additional Help**:
   - For more on Python syntax, check the [Python documentation](https://docs.python.org/3/).
   - If issues persist, consult the [binarytree documentation](https://pypi.org/project/binarytree/) or refer to the [GitHub Issues page](https://github.com/joowani/binarytree/issues) for similar issues.

## Example Output

```plaintext
==================================================
Test Case 1: '((P ⇒ Q) ∧ ((¬Q) ∧ (¬P)))'

Result: '(P ⇒ Q) ∧ ((¬Q) ∧ (¬P))' is a well-formed formula.

Compound formula is well-formed, therefore we can find the truth value from each interpretation:
I1: True
I2: False
I3: True
```

The code will automatically display each formula’s well-formed status and its evaluation for each interpretation.

---

## Further Notes

This code provides a foundational approach for working with logical formulas in binary trees. It can be extended to support additional logical operators or complex syntax by modifying the `is_wff` and `treeValid` functions.
