
def setup():
    global img
    size(756, 1008)
    background(255)
    img = loadImage("tv.jpg")
    

def draw(): # Glitch out everything
    
    loadPixels()
    img.loadPixels()
    
    for y in xrange(0, height, 5):
        for x in xrange(0, width, 10):
            loc = x + (y * width)
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            noStroke()
            fill(r + 15, g + 20, b + 25, 55)
            def mousePressed():
                ellipse(x, y, mouseX, 25)
            mousePressed()
                     
    save("square tv.png")

            
