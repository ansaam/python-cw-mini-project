# write your code here
def padel_court_cost(court_type):
if court_type=="indoor":
    return 30
elif court_type=="outdoor":
    return 20
else:
    return False
padel_court_cost("indoor")
print(padel_court_cost("indoor"))
def rackets_cost(racket_brand):
    if racket_brand=="Bullpadel":
        return 100
    elif racket_brand=="Nox":
        return 140
    elif racket_brand=="siux":
        return 200
    else:
        return False
    rackets_cost("Nox")
    print(rackets_cost("Nox"))
    def padel_balls_cost(ball_boxes):
        if ball_boxes==1:
            return 2
        elif ball_boxes==2:
            return 3.5
        elif ball_boxes==3:
            return 5
        else:
            return False
        padel_balls_cost(3)
        print(padel_balls_cost(3))
        def padel_game_cost():
            court_type=input("enter the the court type:")
            racket_brand=input("enter the racket brand:")
            ball_boxes=int(input("enter the number of ball boxes:"))
            price=(padrl_balls_cost(ball_boxes))+padel_court_cost(court_type)+rackets_cost(racket_brand)
            return price
        rackets_cost("Nox")
        print(rackets_cost("Nox"))
        def padel_balls_cost(ball_boxes):
            if ball_boxes==1:
                return 2
            elif ball_boxes==2:
                return 3.5
            elif ball_boxes==3:
                return 5
            else:
                return False
            padel_balls_cost(3)
            print(padel_balls_cost(3))
            def padel_game_cost():
                court_type=input("enter the the court type:")
                racket_brand=input("enter the racket brand:")
                ball_boxes=int(input("enter the number of ball boxes:"))
                price=(padel_balls_cost(ball_boxes))+padel_court_cost(court_type)+rackets_cost(racket_brand)
                price=(padel_balls_cost(ball_boxes))+padel_court_cost(court_type)+rackets_cost(racket_brand)
                return price
            print(padel_game_cost())
          #hours:3
          #court_type:indoors
          #racket_brand:Nox
          #ball_boxes:2
  

