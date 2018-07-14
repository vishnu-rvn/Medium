# import time
# from pynput.mouse import Button, Controller, Key
# controller = Controller()

# def position_mouse(x,y):#  put in you coords here
#     controller.position = (x, y)


# def left_click(numofclicks): #  mouse left clicks
#     controller.click(Button.left, numofclicks)


# def right_click(numofclicks): #  mouse right clicks
#     controller.click(Button.right, numofclicks)


# def keyboard_typer(sentence): # just for typing a sintence
#     controller.type(sentence)


def count_primes(max_number):
	primes = 0
	for number in range(2, max_number+1):
		if is_prime(number):
			primes += 1
	return primes

def is_prime(number):
	for n in range(2, number):
		if number % n == 0:
			return False
	return True

print(count_primes(20))