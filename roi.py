# Create an Object Oriented Program to calculate the ROI on an investment property

class ReturnOnInvestment():
    """attributes"""
    def __init__(self, total_monthly_income, total_monthly_expenses, cash_flow, r_o_i):
        self.total_monthly_income = total_monthly_income
        self.total_monthly_expenses = total_monthly_expenses
        self.cash_flow = cash_flow
        self.r_o_i = r_o_i
    
    # Method that takes in all income variables
    def income_input(self):
        response_x = input("What is your total projected monthly income on this property?: ")
        self.total_monthly_income = int(response_x)
        new_income_variable = int(response_x) * 12
        print(f"The total income for this property PER YEAR is: {new_income_variable}")

    # Method that takes in expense variables
    def expense_input(self):
        response_y = input("What are your total monthly expenses? Please include all tax, insurance, utilities, HOA, vacancy expenses, etc.: ")
        self.total_monthly_expenses = int(response_y)
        new_expense_variable = int(response_y) * 12
        print(f"The total expenses for this property PER YEAR is: {new_expense_variable}")

    def cash_flow_input(self):
        self.cash_flow = (self.total_monthly_income * 12) - (self.total_monthly_expenses * 12)
        print(f"The total cash flow for this property PER YEAR is: {self.cash_flow}")

    def r_o_i_input(self):
        response_a = int(input("What is your total down payment on this property?: "))
        response_b = int(input("What were your closing costs?: "))
        response_c = int(input("What was your rehab budget?: "))
        response_d = int(input("Additional costs to you?: "))
        total_investment = response_a + response_b + response_c + response_d
        self.r_o_i = (self.cash_flow / total_investment) * 100
        print(f"The ROI for this property is: {self.r_o_i} %")

return_ = ReturnOnInvestment([], [], [], [])

def run():
    while True:
        response_a = input("Press 'X' to begin ROI calculation: ")
        if response_a.lower() == 'x':
            return_.income_input()
            return_.expense_input()
            return_.cash_flow_input()
            return_.r_o_i_input()
            break
        else:
            print("Try again.")        

run()