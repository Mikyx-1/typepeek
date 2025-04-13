from typing import Any, Dict, List, Set, Tuple, Union, get_args, get_origin


def infer_type(obj: Any) -> Any:
    if isinstance(obj, list):
        if not obj:
            return List[Any]
        element_types = {infer_type(el) for el in obj}
        if len(element_types) == 1:
            return List[element_types.pop()]
        return List[Union[tuple(element_types)]]

    elif isinstance(obj, dict):
        if not obj:
            return Dict[Any, Any]
        key_types = {infer_type(k) for k in obj.keys()}
        val_types = {infer_type(v) for v in obj.values()}
        key_type = key_types.pop() if len(key_types) == 1 else Union[tuple(key_types)]
        val_type = val_types.pop() if len(val_types) == 1 else Union[tuple(val_types)]
        return Dict[key_type, val_type]

    elif isinstance(obj, tuple):
        return Tuple[tuple(infer_type(x) for x in obj)]

    elif isinstance(obj, set):
        if not obj:
            return Set[Any]
        element_types = {infer_type(el) for el in obj}
        if len(element_types) == 1:
            return Set[element_types.pop()]
        return Set[Union[tuple(element_types)]]

    else:
        return type(obj)


if __name__ == "__main__":
    pass
