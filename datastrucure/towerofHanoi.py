"""
    |      |     |
    |      |     |
 ---|---   |     |
 ---|---   |     |
 ---|---   |     |
    to   center from
"""

def Tower(height, fromp, centre, top):
    if height >= 1:
        moveTower(height-1,fromp ,centre, top)
        print("moving the rings",fromp,top)
        moveTower(height-1,centre ,top ,fromp)

Tower(3,"A","B","C")
