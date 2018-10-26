class Phone:
	def __init__(self, brand, model, price):
		self.brand = brand
		self.model = model
		self.price = price

	def get_phone_info(self):
	    return f'Телефон {brand} {model} стоимость {price} сом.'

if __name__ == '__main__':
	brand = input("Введите бренд вашего телефона: ")
	model = input('Введите модель вашего телефона: ')
	price = input('Введите стоимость вашего телефона: ')
	
	phone = Phone(brand,model,price)
	print(phone.get_phone_info())