class CoffeeMachine:
	def __init__(self):
	    self.coffee = 1000
	    self.sugar = 1000
	    self.milk = 1000

	def make_coffee(self, coffee, sugar, milk):
	    if coffee <= self.coffee and sugar <= self.sugar and milk <= self.milk:
	        print('Готова, держи свое кофе!')
	        self.__subtract__coffee(coffee)
	        self.__subtract__sugar(sugar)
	        self.__subtract__milk(milk)
	    else:
	        if coffe > self.coffee:
	            print(str(coffee - self.coffee) + 'граммов кофе не хватает, пж заполните.')
	        if sugar > self.sugar:
	            print(str(sugar - self.sugar) + 'граммов сахара не хватает, пж заполните.')
	        if milk > self.milk:
	            print(str(milk - self.milk) + 'граммов молока не хватает, пж заполните.')

    def __subtract_coffee(self, coffee):
    	self.coffee -= coffee

    def __subtract__sugar(self, sugar):
        self.sugar -= sugar

    def __subtract__milk(self, milk):
        self.milk -= milk


if __name__ == '__main__':
    coffee = int(input('Сколько кофе мы должны добавить: '))
    sugar = int(input('Сколько сахара мы должеы добавить: '))
    milk = int(input('Сколько молока мы должны добавить: '))


costumer = CoffeeMachine()
costumer.make_coffee(coffee, sugar, milk)                	
