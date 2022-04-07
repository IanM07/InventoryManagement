class Brand:
    def __init__(self,brand):
        self.brand = brand


#Create a phone class with a brand, how many megapixels are in the camera, screen size, and storage size
class Phone(Brand):
    def __init__(self,brand,mgp,screen,storage):
        super().__init__(brand)
        self.mgp = mgp
        self.screen = screen
        self.storage = storage
    def __str__(self):
        return "Phone \nBrand: {}\nMegapixels: {}\nScreen: {}\nStorage Size: {}\n".format(self.brand,
                                                                                          self.mgp,
                                                                                          self.screen,
                                                                                          self.storage)
    #When this is called it allows the program to check the name of an objects class, this is used in the edit function so the program knows what class the object is
    def class_name(self): 
        return self.__class__.__name__
                                                                            

    
#Create a speaker class with a brand, bluetooth capabilites, number of channels, and frequency
class Speaker(Brand):
    def __init__(self,brand,bluetooth,channelnums,frequency):
        super().__init__(brand)
        self.bluetooth = bluetooth
        self.channelnums = channelnums
        self.frequency = frequency
    def __str__(self):
        return "Speaker \nBrand: {}\nBluetooth: {}\nNumber of Channels: {}\nFrequency: {}\n".format(self.brand,
                                                                                                    self.bluetooth,
                                                                                                    self.channelnums,
                                                                                                    self.frequency)
    def class_name(self): 
        return self.__class__.__name__

#Create a printer class with a brand, printspeed, twosided printing capabilites, and autofeeding
class Printer(Brand):
    def __init__(self,brand,prntspd,twoside,autofeed):
        super().__init__(brand)
        self.prntspd = prntspd
        self.twoside = twoside
        self.autofeed = autofeed
    def __str__(self):
        return "Printer \nBrand: {}\nPrinting Speed: {}\nTwo Sided Printing: {}\nAutofeeder: {}\n".format(self.brand,
                                                                                                          self.prntspd,
                                                                                                          self.twoside,
                                                                                                          self.autofeed)
    def class_name(self): 
        return self.__class__.__name__

#Create a Desktop class with a ceratain amount of memory, ram, cpu speed, and gpu speed
class Desktop:
    def __init__(self,storage,ram,cpu,gpu):
        self.storage = storage
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
    def __str__(self):
        return "Desktop \nMemory: {}\nRAM: {}\nCPU Speed: {}\nGPU Speed: {}\n".format(self.storage,
                                                                                      self.ram,
                                                                                      self.cpu,
                                                                                      self.gpu)
    def class_name(self): 
        return self.__class__.__name__ 

#Create a TV class that has a brand, resolution, dimensions, and smart TV capabilities
class Tv(Brand):
    def __init__(self,brand,resolution,dimension,smart):
        super().__init__(brand)
        self.resolution = resolution
        self.dimension = dimension
        self.smart = smart
    def __str__(self):
        return "TV \nBrand: {}\nResolution: {}\nDimensions: {}\nSmart TV: {}\n".format(self.brand,
                                                                                      self.resolution,
                                                                                      self.dimension,
                                                                                      self.smart)
    def class_name(self): 
        return self.__class__.__name__

#Creates the cart list and adds 4 new objects to it
cart = []
phone1 = Phone("Apple", "12", "6in", "128gb")
speaker1 = Speaker("Bose", "Yes", "5", "50 Hertz")
printer1 = Printer("HP", "1pps", "Yes", "No")
desktop1 = Desktop("1Tb", "16gb", "3.2ghz", "2ghz")
tv1 = Tv("Samsung", "4k", "40in", "Yes")
#Converts objects to key-value pairs to be put into dictionary
cart = [{phone1.class_name() : phone1.__dict__}, {speaker1.class_name() : speaker1.__dict__}, {printer1.class_name() : printer1.__dict__}, {desktop1.class_name() : desktop1.__dict__}, {tv1.class_name() : tv1.__dict__}]
count = 0
for item in cart:
    count +=1
    print(count, ")", item)

def add(cart):
    #Allows the user to add an item
    count = 0
    print("----------------------------------------------------------")
    count = int(input("Input how many items would you like to add: "))
    for i in range(count):
        selection = input("Would you like to add a Phone, Speaker, Printer, Desktop, or TV: ")
        if selection == "Phone" or selection == "phone":
            brand = input("Input what brand of phone you would like: ")
            mgp = input("Input how many megapixels the camera is: ")
            size = input("Input how big the screen is in inches: ")
            storage = input("Input how much storage the phone will have in gigabytes: ")
            new_phone = Phone(brand, mgp, size, storage)
            cart.append({new_phone.class_name() : new_phone.__dict__})
            
        elif selection == "Speaker" or selection == "speaker":
            brand = input("Input what brand of speaker you would like: ")
            blutooth = input("Is the speaker blutooth: ")
            channelnums = input("Input the number of channels: ")
            frequency = input("Input the frequency in hertz: ")
            new_speaker = Speaker(brand, blutooth, channelnums, frequency)
            cart.append({new_speaker.class_name() : new_speaker.__dict__})

        elif selection == "Printer" or selection == "printer":
            brand = input("Input what brand of printer you would like: ")
            speed = input("Input the printing speed in pages per minute: ")
            twosides = input("Can it print on two sides: ")
            autofeed = input("Does the printer have autofeeding: ")
            new_printer = Printer(brand, speed, twosides, autofeed)
            cart.append({new_printer.class_name() : new_printer.__dict__})

        elif selection == "Desktop" or selection == "desktop":
            storage = input("Input the amount of storage in gigabytes: ")
            ram = input("Input the amount of ram in gigabytes: ")
            cpu = input("Input the cpu clock speed in gigahertz: ")
            gpu = input("Input the gpu clock speed in gigahertz: ")
            new_desktop = Desktop(storage, ram, cpu, gpu)
            cart.append({new_desktop.class_name() : new_desktop.__dict__})

        elif selection == "TV" or selection == "tv":
            brand = input("Input what brand of TV you would like: ")
            resolution = input("Input the resolution of the TV in pixels: ")
            dimension = input("Input how big the screen is in inches: ")
            smart = input("Does the TV have smart capabilites: ")
            new_tv = Tv(brand, resolution, dimension, smart)
            cart.append({new_tv.class_name() : new_tv.__dict__})
            
    print("----------------------------------------------------------")

def remove(cart):
    #Allows the users to remove an item
    count = 0
    print("----------------------------------------------------------")
    print("Items in Cart: \n")
    for item in cart:
        count = count + 1
        print(count,")",item)
    selection = int(input("Please type the number of the item you wish to remove: ")) - 1
    del cart[selection]
    print("----------------------------------------------------------")

def edit(cart):
    selection = 0
    count = 0
    print("----------------------------------------------------------")
    print("Items in Cart: \n")
    for item in cart:
        count = count + 1
        print(count,")",item)
    #Asks users which object they want to edit
    selection = int(input("Please type the number of the item you wish to edit: ")) - 1
    choice = cart[selection]
    del cart[selection]
    for key in choice:
        selection = key
    #Allows the user to edit all parts of the object they chose
    if selection == 'Phone':
        brand = input("Input what brand of phone you would like: ")
        mgp = input("Input how many megapixels the camera is: ")
        size = input("Input how big the screen is in inches: ")
        storage = input("Input how much storage the phone will have in gigabytes: ")
        new_phone = Phone(brand, mgp, size, storage)
        cart.append({new_phone.class_name() : new_phone.__dict__})
        
    elif selection == 'Speaker':
        brand = input("Input what brand of speaker you would like: ")
        blutooth = input("Is the speaker blutooth: ")
        channelnums = input("Input the number of channels: ")
        frequency = input("Input the frequency in hertz: ")
        new_speaker = Speaker(brand, blutooth, channelnums, frequency)
        cart.append({new_speaker.class_name() : new_speaker.__dict__})

    elif selection == 'Printer':
        brand = input("Input what brand of printer you would like: ")
        speed = input("Input the printing speed in pages per minute: ")
        twosides = input("Can it print on two sides: ")
        autofeed = input("Does the printer have autofeeding: ")
        new_printer = Printer(brand, speed, twosides, autofeed)
        cart.append({new_printer.class_name() : new_printer.__dict__})

    elif selection == 'Desktop':
        storage = input("Input the amount of storage in gigabytes: ")
        ram = input("Input the amount of ram in gigabytes: ")
        cpu = input("Input the cpu clock speed in gigahertz: ")
        gpu = input("Input the gpu clock speed in gigahertz: ")
        new_desktop = Desktop(storage, ram, cpu, gpu)
        cart.append({new_desktop.class_name() : new_desktop.__dict__})
            
    elif selection == 'Tv':
        brand = input("Input what brand of TV you would like: ")
        resolution = input("Input the resolution of the TV in pixels: ")
        dimension = input("Input how big the screen is in inches: ")
        smart = input("Does the TV have smart capabilites: ")
        new_tv = Tv(brand, resolution, dimension, smart)
        cart.append({new_tv.class_name() : new_tv.__dict__})
    print("----------------------------------------------------------")

def PrintCart(cart):
    #Prints out the cart
    count = 0
    print("----------------------------------------------------------")
    print("Items in Cart: \n")
    count = 0
    for item in cart:
        count +=1
        print(count, ")", item)
    print("----------------------------------------------------------")

def menu(cart):
    #Creates menu loop so that the menu is always returned to
    while True:
        selection = 0
        print ("1)Print Cart \n2)Add an Item\n3)Remove an Item\n4)Edit an Item\n5)Leave the Program")
        selection = int(input("Please type the number of the option you wish to use: "))
        if selection == 1:
            PrintCart(cart)
            
        elif selection == 2:
            add(cart)
            
        elif selection == 3:
            remove(cart)
            
        elif selection == 4:
            edit(cart)

        elif selection == 5:
            return
    
if __name__ == "__main__":
    menu(cart)


#Unit Tests
assert phone1 in cart
assert printer1 in cart
assert desktop1 in cart
assert tv1 in cart
assert speaker1 in cart
assert phone1.brand == "Apple"
assert printer1.brand == "HP"
assert desktop1.memory == "1Tb"
assert tv1.brand == "Samsung"
assert speaker1.brand == "Bose"
assert phone1.storage == "128gb"
assert printer1.twoside == "Yes"
assert desktop1.cpu == "3.2ghz"
assert tv1.resolution == "4k"
assert speaker1.bluetooth == "Yes"
