import keyboard

text = input("Enter text: ")
while text == "":
    text = input("Enter text: ")
count = input("Enter number of massages: ")
while count == "":
    count = input("Enter number of massages: ")

start = 0

while start <= int(count):
    keyboard.write(text)
    keyboard.press('enter')
    start = start+1
