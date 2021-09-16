def food(s, vegan=False):

    if vegan:
        print("lactosemjölk" )
    else: 
        print("mjölk")

food("mjölk")       # mjölk
food("mjölk", True) # sojamjölk