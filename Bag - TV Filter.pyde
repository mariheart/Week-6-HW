
def setup():
    global img
    size(756, 1008)
    background(255)
    img = loadImage("catte.jpg")
    

def draw(): # Glitch out everything
    
    loadPixels()
    img.loadPixels()
    
    for y in xrange(height):
        for x in xrange(width):
            
            currpix = x + (y * width)
            
            r = red(img.pixels[currpix])
            g = green(img.pixels[currpix])
            b = blue(img.pixels[currpix])
            a = alpha(img.pixels[currpix])
            
            grey = (r + g + b) / 3
            
            #Here we start to glich out the stuff.
            
            if (50 < grey < 255) and b > 167 or g > 253:
                pixels[currpix] = color(random(255))
            
            else:
                pixels[currpix] = color(r / 2, g / 2, b, a)
            
    updatePixels()
    
    save("glitchcatte.png")
            
