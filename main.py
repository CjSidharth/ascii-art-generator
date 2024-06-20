
from PIL import Image # loads Image class
import pygame
import pygame.camera



ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
string_length = len(ascii_string)



def capture_image():
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0],(400,400))
        cam.start()
        image = cam.get_image()
        pygame.image.save(image,"capture.jpg")
        cam.stop()
    else:
        print("No camera was detected")


# uses list comprehension to create matrix
def create_matrix(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

def store_rgb(pixel_matrix,pix,x,y):
    for i in range(x): # uses for loops to store data in matrix
        for j in range(y):
            pixel_matrix[i][j] = pix[i,j]


def brightness_function(R,G,B):
    #understand these functions.
    #return round(0.21*R + 0.72*G + 0.07*B)
    return round((R+G+B)/3)


# brightness matrix
def brightness_setting(pixel_matrix,brightness_matrix,x,y):
    for i in range(x):
        for j in range(y):
            R = pixel_matrix[i][j][0]
            G = pixel_matrix[i][j][1]
            B = pixel_matrix[i][j][2]
            avg  = brightness_function(R,G,B)
            brightness_matrix[i][j] = avg

def ascii_mapper(brightness_range,length,brightness):
    interval_length = round(brightness_range/length)
    index = round(brightness/interval_length)
    return index

def image_former(img_matrix,brightness_matrix,x,y):
    for i in range(x):
        for j in range(y):
            index = ascii_mapper(255,string_length,brightness_matrix[i][j])
            img_matrix[i][j] = ascii_string[index]

def print_image(img_matrix,x,y,n):
    for j in range(y):
        for i in range(x):
            print(img_matrix[i][j]*n,end='')
        print("")

def main():
    ss = int(input("Enter 1 for camera otherwise enter 2 for custom file. "))
    if ss == 1:
        capture_image()
        path = "capture.jpg"
    else:
        path = input("Name of file: ")
    try:
        im = Image.open(path) # opens
    except FileNotFoundError:
        print("File was not found at the required location")
    im = im.resize((400,400))
    pix = im.load() # loads image for processing
    x,y = im.size # gets size
    pixel_matrix = create_matrix(x,y)
    brightness_matrix = create_matrix(x,y)
    img_matrix = create_matrix(x,y)
    store_rgb(pixel_matrix,pix,x,y)
    brightness_setting(pixel_matrix,brightness_matrix,x,y)
    image_former(img_matrix,brightness_matrix,x,y)
    print_image(img_matrix,x,y,3)

if __name__=="__main__": 
    main() 