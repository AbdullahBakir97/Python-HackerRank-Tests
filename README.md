# Python Certification Test Solutions

![HackerRank_certificate_py](https://github.com/AbdullahBakir97/Python-HackerRank-Tests/assets/127149804/2d38f405-343f-4f9a-a5f9-348147e36326)


## Overview

This repository contains solutions to two coding challenges as part of the Python certification test from HackerRank. These challenges are designed to test proficiency in Python programming through real-world problem-solving scenarios.
Certificate: [Certificate](https://www.hackerrank.com/certificates/9ae979da8e2c) 

## Challenges

### 1. Vending Machine

This challenge involves creating a `VendingMachine` class that models a simple vending machine. Users can buy items from the vending machine, and the machine keeps track of the remaining items and the money transactions.

#### Implementation Details

**Class: `VendingMachine`**

- **__init__(self, num_items, item_price)**
  - **Parameters:**
    - `num_items` (int): The initial number of items in the vending machine.
    - `item_price` (float): The price per item in the vending machine.
  - **Description:**
    - Initializes the vending machine with the specified number of items and item price.

- **buy(self, req_items, money)**
  - **Parameters:**
    - `req_items` (int): The number of items the user wants to buy.
    - `money` (float): The amount of money inserted by the user.
  - **Returns:**
    - If the transaction is successful, the method returns the remaining change.
    - If there are not enough items in the machine, it returns "not enough items in the machine".
    - If the inserted money is insufficient, it returns "not enough coins".
  - **Description:**
    - Allows users to buy a specified number of items by inserting the required amount of money. It updates the number of items in the machine and calculates the change if the transaction is successful.

#### Example Usage

```python
class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        if req_items > self.num_items:
            return "not enough items in the machine"
        if money < self.item_price * req_items:
            return "not enough coins"
        
        self.num_items -= req_items
        change = money - self.item_price * req_items
        return change

# Example usage
vending_machine = VendingMachine(10, 2)
print(vending_machine.buy(1, 5))  # Output: 3
print(vending_machine.buy(10, 100))  # Output: "not enough items in the machine"
print(vending_machine.buy(7, 100))  # Output: 86
print(vending_machine.buy(2, 3))  # Output: "not enough coins"
```

## 2. Dominant Cells in a Grid

This challenge involves writing a function `numCells(grid)` to count the number of dominant cells in a given grid. A dominant cell is one whose value is greater than all the neighboring cells' values.

### Implementation Details

**Function: `numCells(grid)`**

- **Parameters:**
  - `grid` (List[List[int]]): A 2D grid of integers.
- **Returns:**
  - An integer representing the number of dominant cells in the grid.
- **Description:**
  - This function calculates the number of dominant cells in the given grid based on the criteria mentioned above.

#### Example Usage

```python
def numCells(grid):
    def is_dominant(r, c):
        current_value = grid[r][c]
        rows = len(grid)
        cols = len(grid[0])
        
        # List of neighbor positions (8 directions)
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),          (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] >= current_value:
                    return False
        return True
    
    dominant_cells_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_dominant(r, c):
                dominant_cells_count += 1
    
    return dominant_cells_count

# Example usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numCells(grid))  # Output: 0
```


## License

This project is licensed under the [MIT License](LICENSE).
