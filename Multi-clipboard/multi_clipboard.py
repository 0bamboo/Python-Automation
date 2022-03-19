import sys
import json
# if u using ubuntu u need to install xclip first and don't care about the warning underline.
import pyperclip #same as clipboard
import clipboard

FILE_NAME = "clipboard.json"

# for copying what's on the clipboard to data
# another_data = pyperclip.paste()
# data = clipboard.paste()
# print(data, another_data)

# # for save new data to clipboard 
# clipboard.copy("Hola")
# data = clipboard.paste()
# print(data)

# Clipboard Class
class myClipBoard:
	''' This the class of myClipBoard, 
	'''
	def __init__(self, c = "none") -> None:
		self.command = c
		self.path = FILE_NAME
		self.data = {}
		self.load_data()
		self.start()
	
	def load_data(self):# fill data dict with the data of the json file
		try:
			with open(self.path, "r") as f:
				self.data = json.load(f)
		except:
				return {}

	def save_data(self):# add data to the json file
		with open(self.path, "w") as f:
			json.dump(self.data, f)
		print("Data saved !")
	
	def save(self):
		key = input("Enter a key : ")
		self.data[key] = clipboard.paste() # paste what's on the clipboard to data
		self.save_data()
	
	def load(self):
		key  = input("Enter a key: ")
		if key in self.data:
			clipboard.copy(self.data[key]) # copy what's on the data dict to clipboard
			print("Data copied to clipboard !")
		else:
			print("Key does not exist !")

	def listClipboard(self):
		self.load_data()
		print(self.data)

	def args(self):
		print(''' 
add : for adding new key to clipboard.
get : for loading the key from the clipboard.
		''')

	def start(self):
		if (self.command == "args"):
			self.args()
		elif (self.command == "add"):
			self.save()
		elif (self.command == "get"):
			self.load()
		elif (self.command == "list"):
			self.listClipboard()

def main():
	if (len(sys.argv) != 2):
		print("Wrong number of arguments [Only one arg is needed] !\n")
	else:
		hajime = myClipBoard(sys.argv[1])

# Starting point
if __name__ == "__main__":
	main()

