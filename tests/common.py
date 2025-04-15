from unittest.mock import MagicMock
import numpy as np

def mock_load_model_and_preprocessor():
    mock_preprocessor = MagicMock()
    mock_preprocessor.transform_batch.side_effect = lambda x: x
    mock_model = MagicMock()
    mock_model.predict.side_effect = lambda x: np.random.random(size=(len(x),))
    return mock_preprocessor, mock_model