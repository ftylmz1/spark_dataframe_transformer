def first(dt, column, type):
    for x in dt:
        if x[0] == column and x[1] == type:
            return x
    raise Exception(f"Column does not exist: Column: '{column}' with Type: '{type}'")