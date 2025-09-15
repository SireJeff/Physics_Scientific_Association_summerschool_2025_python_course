# solution_q1.py

class PizzaShop:
    """A base class for a pizza shop."""
    
    # The base menu is a class attribute shared by all instances
    MENU = {'pepperoni': 150, 'margherita': 120, 'vegetable': 95}
    
    def __init__(self, name):
        self.name = name
        self.current_order = []

    def add_to_order(self, pizza_name):
        """Adds a pizza to the current order if it's on the menu."""
        if pizza_name in self.MENU:
            self.current_order.append(pizza_name)
            print(f"Added {pizza_name} to the order at {self.name}.")
        else:
            print(f"Sorry, {pizza_name} is not on the menu.")

    def calculate_total(self):
        """Calculates the total price of the order using the instance's tariff."""
        base_price = sum(self.MENU[pizza] for pizza in self.current_order)
        # self.tariff is defined in the child classes
        final_price = base_price * self.tariff
        
        print(f"\nOrder at {self.name} (Tariff: {self.tariff}):")
        for pizza in self.current_order:
             # Show the price for each pizza after applying the tariff
             print(f"- {pizza.title()} Pizza: {self.MENU[pizza] * self.tariff}")
        print(f"Total Price: {final_price}")
        print("---")
        
        # Clear the order for the next customer
        self.current_order = []

# --- Child classes for specific branches ---

class TehranBranch(PizzaShop):
    """A branch in Tehran with a 10% higher tariff."""
    def __init__(self):
        # Call the parent class's __init__ method
        super().__init__(name="Tehran Branch")
        self.tariff = 1.10 # 10% markup

class ShirazBranch(PizzaShop):
    """A branch in Shiraz with a 5% lower tariff."""
    def __init__(self):
        super().__init__(name="Shiraz Branch")
        self.tariff = 0.95 # 5% discount

# --- Main execution to demonstrate functionality ---
if __name__ == "__main__":
    tehran_shop = TehranBranch()
    shiraz_shop = ShirazBranch()
    
    # Place an order at the Tehran branch
    tehran_shop.add_to_order('pepperoni')
    tehran_shop.add_to_order('margherita')
    tehran_shop.calculate_total()
    
    # Place an order at the Shiraz branch
    shiraz_shop.add_to_order('pepperoni')
    shiraz_shop.add_to_order('vegetable')
    shiraz_shop.calculate_total()