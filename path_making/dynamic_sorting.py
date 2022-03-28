from cmd_app import Database


def dyn_sorting():
    db_obj = Database()
    result = db_obj.share_item_location()
    #print(result)
    item_list=[]
    for item in result.keys():
        item_list.append(item)
    #print(item_list)
    return item_list,result

if __name__ == "__main__":
    print(dyn_sorting())
#'happy happy', '50 50', 'cadbury choco cookie', 'mysore soap',