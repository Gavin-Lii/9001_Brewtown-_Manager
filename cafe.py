from menu_data import MENU_ITEMS

class Cafe:
    def __init__(self, name):
        self.name = name

        #Starting staff number
        self.baristas = 2
        self.servers = 1

        #Starting business status
        self.marketing_level = 0
        self.satisifaction = 5
        self.queue_time = 14

        #Tracks cumulative profit across all fortnights
        self.total_profit = 0

        #Building menu from Menu_items
        self.menu=[]

        for item in MENU_ITEMS:
            self.menu.append({
                "name": item["name"],

                # Original reference values
                "base_price": item["base_price"],
                "base_sales": item["base_sales"],

                # Current editable values
                "price": item["base_price"],

                # Product cost
                "cost": item["cost"]
            })
        self.update_queue_time()

    # ── Cost calculations ─────────────────────────────────────────

    #Staff cost
    def calculate_staff_cost(self):

        barista_cost = self.baristas * 600
        servers_cost = self.servers * 450
        total_staff_cost = servers_cost + barista_cost

        return total_staff_cost

    #Marketing cost
    def calculate_marketing_cost(self):
        return self.marketing_level * 500

    #Fixed cost
    def calculate_fixed_cost(self):
        return 1000

    def calculate_total_cost(self):
        return self.calculate_fixed_cost() + self.calculate_staff_cost() + self.calculate_marketing_cost()

    # ── Sales calculations ────────────────────────────────────────
    def calculate_item_sales(self,item):
        # calculate current price with original price
        price_difference = item["price"]-item["base_price"]

        #price impact sales
        sales = item["base_sales"]-(price_difference*20)

        sales += self.marketing_level*20

        #Satisifaction <= 5 decrease sales. satisifaction >= 7 incresaes sales
        sales += (self.satisifaction - 5) * 15

        return max(0, int(sales))

    #Product revenue logic
    def calculate_revenue(self):
        total_revenue = 0

        for item in self.menu:
            sales = self.calculate_item_sales(item)
            total_revenue += sales * item["price"]
        return int(total_revenue)

    #Product cost logic
    def calculate_product_cost(self):
        # Sum of ingredient costs across all items sold this fortnight
        total_product_cost = 0

        for item in self.menu:
            sales = self.calculate_item_sales(item)
            total_product_cost += sales * item["cost"]
        return int(total_product_cost)

    #Profit logic
    def calculate_profit(self):
        revenue = self.calculate_revenue()

        total_cost = self.calculate_total_cost() + self.calculate_product_cost()

        profit = int(revenue - total_cost)
        return profit

    #Update total profit
    def update_total_profit(self):
        self.total_profit += self.calculate_profit()

    #Adjust price logic
    def update_item_price(self, item_index, new_price):
        self.menu[item_index]["price"] = new_price


    # ── Menu and staff management ─────────────────────────────────
    #Staff management
    def hire_barista(self, amount):

        self.baristas += amount

    def hire_server(self, amount):

        self.servers += amount

    def fire_barista(self, amount):

        if self.baristas - amount >= 1:
            self.baristas -= amount

    def fire_server(self, amount):

        if self.servers - amount >= 1:
            self.servers -= amount

    # ── Customer experience ───────────────────────────────────────
    def calculate_total_sales(self):
        total_sales = 0

        for item in self.menu:
            total_sales += self.calculate_item_sales(item)

        return total_sales

    def update_queue_time(self):
        total_customers = self.calculate_total_sales()

        # Each barista/server can handle some customers per fortnight
        staff_capacity = (self.baristas * 200) + (self.servers * 150)

        if staff_capacity == 0:
            self.queue_time = 30
            return

        # Pressure ratio: >1.0 means staff are overwhelmed
        pressure = total_customers / staff_capacity

        if pressure <= 0.8:
            self.queue_time = 4
        elif pressure <= 1.0:
            self.queue_time = 7
        elif pressure <= 1.3:
            self.queue_time = 11
        elif pressure <= 1.6:
            self.queue_time = 15
        else:
            self.queue_time = 20

    #Satisifaction logic
    def update_satisfaction(self):
        score = 5

        # Queue time is the biggest factor in satisfaction
        if self.queue_time > 15:
            score -= 2
        elif self.queue_time > 11:
            score -= 1
        elif self.queue_time > 7:
            score += 0
        elif self.queue_time > 4:
            score += 2
        elif self.queue_time <= 4:
            score += 3

        # Any item priced more than $2 above original takes a satisfaction hit
        for item in self.menu:
            if item["price"] > item["base_price"]+2:
                score -= 1
                break
        score = max(1,min(score,10))

        self.satisifaction = score


    # ── End of fortnight update ───────────────────────────────────
    def process_fortnight(self):
        # Recalculate all metrics after the player's decisions take effect
        self.update_queue_time()
        self.update_satisfaction()
        self.update_total_profit()














