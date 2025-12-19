def cannons_ready(gunners):
    
    for i in gunners.values():
        if i == 'nay':
            return "Shiver me timbers!"
    
    return "Fire!"