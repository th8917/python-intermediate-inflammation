from unittest.mock import Mock

def test_sum_shapes():
    mock_shape1 = Mock()
    mock_shape1.get_area().return_value = 10


    mock_shape2() = Mock()
    mock_shape3.get_area().return_value = 13
    my_shapes = [Mock.shape1,Mock.shape2]
    total_area = sum(shape.get_area() for shape in my_shapes)

    assert total_area =23