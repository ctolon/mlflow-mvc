from typing import List, Any

def genericTransformer(value: Any) -> dict:
    """_summary_

    Args:
        value (Any): _description_

    Returns:
        dict: _description_
    """
    return dict((x, y) for x, y in tuple(value))
                 
def genericMultiTransformer(value: Any) -> List[dict]:
    """_summary_

    Args:
        value (Any): _description_

    Returns:
        List[dict]: _description_
    """
    
    merge_list = []
    for i in range(len(value)):
        merge_list.append(dict((x, y) for x, y in tuple(value[i])))
    return merge_list
    