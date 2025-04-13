from typepeek import infer_type

def test_list_of_ints():
    assert str(infer_type([1, 2, 3])) == "typing.List[int]"
