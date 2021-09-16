def tasks_match(task1, task2):
    if task1 == task2:
        return True
    return False

def get_preferred_option(task1, task2):
    if task1 == task2:
        return task1.name
    elif task1.name == "Wash Dishes":
        if task2.name == "Cook Dinner":
            return "Wash Dishes"
        if task2.name == "Clean Windows":
            return "Clean Windows"
    elif task1.name == "Clean Windows":
        if task2.name == "Wash Dishes":
            return "Clean Windows"
        if task2.name == "Cook Dinner":
            return "Cook Dinner"
    elif task1.name == "Cook Dinner":
        if task2.name == "Clean Windows":
            return "Cook Dinner"
        if task2.name == "Wash Dishes":
            return "Wash Dishes"
    
        
    