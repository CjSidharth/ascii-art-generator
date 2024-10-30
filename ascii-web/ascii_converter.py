from PIL import Image # loads Image class

ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
string_length = len(ascii_string)


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


def convert_to_ascii(path, scale_factor=3):
    im = Image.open(path).resize((400, 400))
    x, y = im.size
    pix = im.load()
    pixel_matrix = create_matrix(x, y)
    brightness_matrix = create_matrix(x, y)
    img_matrix = create_matrix(x, y)
    store_rgb(pixel_matrix, pix, x, y)
    brightness_setting(pixel_matrix, brightness_matrix, x, y)
    image_former(img_matrix, brightness_matrix, x, y)
    
    ascii_output = ""
    for j in range(y):
        for i in range(x):
            ascii_output += img_matrix[i][j] * scale_factor
        ascii_output += "\n"
    return ascii_output

