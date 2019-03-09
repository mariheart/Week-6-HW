
def setup():
    global img
    size(756, 1008)
    background(255)
    img = loadImage("tv.jpg")
    

def draw(): # Glitch out everything
    loadPixels()
    img.loadPixels()
    
    for y in xrange(height):
        for x in xrange(width):
            loc = x + (y * width)
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            # Motion!
            stroke(r, g, b * 2, 100)
            point(x - 15, y - 15)
            
            stroke(r, g * 2, b, 100)
            point(x - 35, y - 35)
            
            stroke(r * 2, g, b, 100)
            point(x - 55, y - 55)
            
            # Positive direction!
            
            stroke(r * 2, g, b, 100)
            point(x + 25, y + 25)
            
            stroke(r, g * 2, b, 100)
            point(x + 45, y + 45)
            
            stroke(r, g, b * 2, 100)
            point(x + 65, y + 65)
            
            # Main
            
            stroke(r, g, b, 175)
            point(x, y)
            
            noLoop()
            #pixels[loc] = color(r, g, b)
            
            
            
            
        #updatePixels()
        
        save("motion tv.png")

            
        
   
            

       # save("glitchy kitty4.png")

            
                        
                    
                
            


    
    #save("catte bits.png")
            
