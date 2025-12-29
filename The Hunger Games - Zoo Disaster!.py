def who_eats_who(zoo):
    food = {
        "antelope": ["grass"],
        "big-fish": ["little-fish"],
        "bug": ["leaves"],
        "bear": ["big-fish","bug","chicken","cow","leaves","sheep"],
        "chicken": ["bug"],
        "cow": ["grass"],
        "fox": ["chicken","sheep"],
        "giraffe": ["leaves"],
        "lion": ["antelope","cow"],
        "panda": ["leaves"],
        "sheep": ["grass"]
    }
    
    zoo_list = zoo.split(",")
    result = [zoo]
    
    while True:
        eaten = False
        for i, animal in enumerate(zoo_list):
            if animal in food:
                if i > 0 and zoo_list[i-1] in food[animal]:
                    prey = zoo_list[i-1]
                    zoo_list.pop(i-1)
                    result.append(f"{animal} eats {prey}")
                    eaten = True
                    break
                elif i < len(zoo_list)-1 and zoo_list[i+1] in food[animal]:
                    prey = zoo_list[i+1]
                    zoo_list.pop(i+1)
                    result.append(f"{animal} eats {prey}")
                    eaten = True
                    break
        if not eaten:
            break
            
    result.append(",".join(zoo_list))
    return result