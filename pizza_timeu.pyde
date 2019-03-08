
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

    
    for i in range(0, 10):
        defa = 10
        noStroke()
        strokeWeight(defa)
        fill (r, g, b, a)
        ellipse(x, y, defa, defa)
        if i % 5 != 0:
            defa += 1
            ellipse(x, y, defa, defa)
    save("pointza timed.png")

            
                        
                    
                
            


    
    #save("redpizza.png")
            
