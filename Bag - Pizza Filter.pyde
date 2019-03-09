
def setup():
    global img
    size(378, 504)
    background(255)
    img = loadImage("pizza.jpg")
    

def draw(): # Glitch out everything
    
    loadPixels()
    img.loadPixels()
    
    y = int(random(img.height))
    x = int(random(img.width))
            
    loc = x + (y * width)
    
    r = red(img.pixels[loc])
    g = green(img.pixels[loc])
    b = blue(img.pixels[loc])
    a = alpha(img.pixels[loc])
    
    grey = (r + g + b) / 3
    
    #Here we start to glich out the stuff.
    s = second()
    defa = 20
    noStroke()
    fill (r, g, b, a)
    
    if s % 5 == 0:
        defa += 10
        ellipse(x - 10, y + 10, defa, defa)
        
        if s % 10 == 0:
            fill(random(r), random(g), random(b), a)
            ellipse(x + 10, y - 10, defa, defa)
    
    else:
        ellipse(x, y, defa, defa)
                     
    save("pointzaaa random.png")

            
