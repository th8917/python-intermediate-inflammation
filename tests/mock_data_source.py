from unittest.mock import Mock
import math
import numpy.testing as npt

def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data
    # create an instance of the Mock class that will 
    # act as the data source (which is expecting a class)
    data_source = Mock()
    # the return value of the load inflammation data function
    # is set to these values 
    # 
    data_source.load_inflammation_data.return_value = [[[0,2,0]],
                                                       [[0,1,0]]]
    
    result = analyse_data(data_source)
    npt.assert_array_almost_equal(result,[0,math.sqrt(0.25),0])