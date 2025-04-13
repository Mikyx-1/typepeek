from typing import Any, Dict, List, Set, Tuple, Union, get_args, get_origin


def infer_type(obj: Any, agnostic: bool = False) -> Any:
    """
    Infer the type hint of the given object.

    Parameters:
        obj: The object for which to infer the type.
        agnostic: (bool)
            - For tuples, if True, return a union of all element types as a single type.
              For example, (1, 2.3, 4, 5) becomes Tuple[Union[int, float]]
            - If False, return a positionally aware tuple type.
              For example, (1, 2.3, 4, 5) becomes Tuple[int, float, int, int]

    Returns:
        A typing object representing the inferred type.
    """

    if isinstance(obj, list):
        if not obj:
            return List[Any]
        element_types = {infer_type(el, agnostic=agnostic) for el in obj}
        if len(element_types) == 1:
            return List[element_types.pop()]
        # Always treat lists as agnostic because List only accepts one type parameter.
        return List[Union[tuple(element_types)]]

    elif isinstance(obj, dict):
        if not obj:
            return Dict[Any, Any]
        key_types = {infer_type(k, agnostic=agnostic) for k in obj.keys()}
        val_types = {infer_type(v, agnostic=agnostic) for v in obj.values()}
        key_type = key_types.pop() if len(key_types) == 1 else Union[tuple(key_types)]
        val_type = val_types.pop() if len(val_types) == 1 else Union[tuple(val_types)]
        return Dict[key_type, val_type]

    elif isinstance(obj, tuple):
        if agnostic:
            # Agnostic mode: summarize all element types in a union without the ellipsis.
            if not obj:
                return Tuple[Any]
            element_types = {infer_type(x, agnostic=agnostic) for x in obj}
            if len(element_types) == 1:
                return Tuple[element_types.pop()]
            else:
                return Tuple[Union[tuple(element_types)]]
        else:
            # Strict mode: return a tuple type with each element's type in order.
            return Tuple[tuple(infer_type(x, agnostic=agnostic) for x in obj)]

    elif isinstance(obj, set):
        if not obj:
            return Set[Any]
        element_types = {infer_type(el, agnostic=agnostic) for el in obj}
        if len(element_types) == 1:
            return Set[element_types.pop()]
        return Set[Union[tuple(element_types)]]

    else:
        return type(obj)


if __name__ == "__main__":
    pass
