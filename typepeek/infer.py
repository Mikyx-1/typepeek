from typing import Any, Dict, List, Set, Tuple, Union
from logger_config import setup_logger

# Import internal _GenericAlias to allow for positional list inference.
try:
    from typing import _GenericAlias
except ImportError:
    # For older versions of Python (<3.7), fallback if needed.
    from typing import GenericMeta as _GenericAlias

logger = setup_logger()

def infer_type(obj: Any, agnostic: bool = True) -> Any:
    """
    Infer the type hint of the given object.

    Parameters:
        obj: The object for which to infer the type.
        agnostic:
            - If True, returns a homogenized type hint for sequences.
              e.g., [1, 2.3, 4, 5] becomes List[Union[int, float]] and
                    (1, 2.3, 4, 5) becomes Tuple[Union[int, float]]
            - If False (default), returns a positionally aware type hint.
              e.g., [1, 2.3, 4, 5] becomes List[int, float, int, int] and
                    (1, 2.3, 4, 5) becomes Tuple[int, float, int, int]

    Returns:
        A typing object (or a _GenericAlias) representing the inferred type.
    """
    if isinstance(obj, list):
        if not obj:
            return List[Any]
        if agnostic:
            element_types = {infer_type(el, agnostic=agnostic) for el in obj}
            if len(element_types) == 1:
                # Convert set to list to index the single element.
                return List[list(element_types)[0]]
            else:
                return List[Union[tuple(element_types)]]
        else:
            pos_types = tuple(infer_type(x, agnostic=agnostic) for x in obj)
            # Use _GenericAlias to simulate a "positional" List.
            return _GenericAlias(List, pos_types)

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
            if not obj:
                return Tuple[Any]
            element_types = {infer_type(x, agnostic=agnostic) for x in obj}
            if len(element_types) == 1:
                return Tuple[list(element_types)[0]]
            else:
                return Tuple[Union[tuple(element_types)]]
        else:
            pos_types = tuple(infer_type(x, agnostic=agnostic) for x in obj)
            return Tuple[pos_types]

    elif isinstance(obj, set):
        if not obj:
            return Set[Any]

        if not agnostic:
            logger.info(
                "Sets in Python are inherently unordered. Strict mode (agnostic == False) does not apply to sets. Automatically switch to agnostic = True."
            )
            agnostic = True
        element_types = {infer_type(el, agnostic=agnostic) for el in obj}
        if len(element_types) == 1:
            return Set[list(element_types)[0]]
        else:
            return Set[Union[tuple(element_types)]]

    else:
        return type(obj)


if __name__ == "__main__":
    pass
