# • Add options for the user to choose the color of the QR code. This will allow 
# users to generate QR codes that match their style or branding. 

# • Implement a feature that lets the user generate multiple QR codes at once by 
# providing a list of URLs or texts. Each QR code should be saved with a unique 
# filename. 
import qrcode
import re


def OneQRCodeGenerator():
    # Define the data you want to encode
    data = input("Write the contents of the QR CODE (link,text,etc): ").strip()

    # Create a QR code instance
    qr = qrcode.QRCode(
        box_size= 10,  # Size of each box in the QR code grid
        border=4,     # Thickness of the border (minimum is 4)
    )

    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    listofcolors = ["black", "white", "red", "blue", "green"]
    def is_hex_color(input_str):
        # Full match for a hex color code pattern
        return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", input_str))

    while True:
        fillColor = input("Foreground color of QR-Code: ")
        if fillColor in listofcolors or is_hex_color(fillColor) == True: break
        else: continue

    while True:
        backColor = input("Background color of QR-Code: ")
        if backColor in listofcolors or is_hex_color(backColor) == True: break
        else: continue

    # Create an image of the QR code
    img = qr.make_image(fill=fillColor, back_color=backColor)

    # Save the image
    filename = input("Gimme Your File's Name: ")
    img.save(filename + ".png")

    print(f"Your file has been saved as {filename}.png")

def MultiQRCodeGenerator():
    while True:
        print("Welcome to Multi-QR-Code Generator.")
        numberOfTimesToCreateQRCodes = int(input("How many qr-codes do you want to generate.(Quit = 65786974)"))
        if numberOfTimesToCreateQRCodes < 1 or numberOfTimesToCreateQRCodes > 100:
            print("Sorry, you cannot generate less than zero or more than hundred qr codes.")
        else: break
    for generators in range(numberOfTimesToCreateQRCodes):
        print(f"QR-Code Number: {generators}.")
        OneQRCodeGenerator()

while True:
    try:
        print("How many qr codes do you want to generate: ")
        usermainInput = input(": ")
        
        if usermainInput.lower() == "exit":
            break
        
        usermainInput = int(usermainInput)
    except ValueError:
        print("Give a Number bruh.")
        continue
    
    if usermainInput == 1:
        OneQRCodeGenerator()
    elif usermainInput > 1 and usermainInput < 100:
        MultiQRCodeGenerator()
    elif usermainInput < 1 or usermainInput > 100:
        print("Enter a Number after 0 and below 100.")
