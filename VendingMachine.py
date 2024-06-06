class VendingMachine:
    def __init__(self, num_items, item_price):
        # Initialize the vending machine with items and prices
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        if req_items > self.num_items:
            return "Not enough items in the machine"
        if money < self.item_price * req_items:
            return "Not enough coins"
        
        self.num_items -= req_items
        change = money - self.item_price * req_items
        return change


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read the initial number of items and their price
    num_items = int(data[0])
    item_price = int(data[1])
    
    # Initialize the vending machine
    vending_machine = VendingMachine(num_items, item_price)
    
    # Read the number of purchase requests
    num_requests = int(data[2])
    
    # Read each purchase request
    index = 3
    results = []
    for _ in range(num_requests):
        req_items = int(data[index])
        money = int(data[index + 1])
        index += 2
        
        result = vending_machine.buy(req_items, money)
        if isinstance(result, str):
            results.append(result)
        else:
            results.append(f"{result:.0f}")
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()