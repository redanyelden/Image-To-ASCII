from PIL import Image

#open
image = Image.open('img.jpg', 'r')

#scaling
new_size = (256, 256)
image.thumbnail(new_size)
new_size = image.size

grayscale_image = image.copy().convert('L')

#get pixel values
pixel_values = list(image.getdata())
grayscale_pixel_values = list(grayscale_image.getdata())

characters = ["$","&","@","#","£","%","?","]",")","|","!","=","+","*","^","~","-",";",":","\"",",","`","'","."]

#write
file = open("ASCII_img.html", "w")
file.write("<!DOCTYPE html><html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"mystyle.css\"></head><body><p style = \"font-family: Lucida Console;\">")
for i in range(len(pixel_values)):
    r, g, b = pixel_values[i][0], pixel_values[i][1], pixel_values[i][2]
    if i%(new_size[0]) == 0:
        file.write("<br>")
    file.write("<font color=\"#" + str(hex(r)) + str(hex(g)) + str(hex(b)) + "\">")
    character = characters[int(grayscale_pixel_values[i]/255 * (len(characters)-1))]
    if (grayscale_pixel_values[i] < 100):
        file.write("<b>")
    file.write(character)
    if (grayscale_pixel_values[i] < 100):
        file.write("</b>")
    file.write("</font>")
file.write("</p></body></html>")