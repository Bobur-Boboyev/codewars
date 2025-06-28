def i_tri(s):
    if s == 0:
        return "Starting Line... Good Luck!"
    elif s >= 140.6:
        return "You're done! Stop running!"
    elif s >= 130.6:
        return {'Run': 'Nearly there!'}
    elif s <= 2.4:
        return {'Swim': f"{round(140.6 - s, 2)}0 to go!"}
    elif s <= 114.4:
        return {'Bike': f"{round(140.6 - s, 2)}0 to go!"}
    else:
        return {'Run': f"{round(140.6 - s, 2)}0 to go!"}