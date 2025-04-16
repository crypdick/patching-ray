from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import ray

from patching_ray.repro_infer import main
from tests.common import mock_load_model_and_preprocessor, mock_mock_me


class MockValidator:
    def __init__(self):
        self.model, self.preprocessor = MagicMock(), MagicMock()
        self.model.predict.side_effect = lambda x: np.random.random(size=(len(x),))

    def __call__(self, batch):
        predictions = self.model.predict(batch)
        return pd.DataFrame({"prediction": predictions})


@patch("patching_ray.repro_infer.load_model_and_preprocessor", mock_load_model_and_preprocessor)
@patch("patching_ray.repro_infer.Validator", MockValidator)
def test_option_3():
    # Option 3: Mock the entire Validator class
    # This does not work because when the Validator class is serialized,
    # pickle cannot find the `test_3` module:
    # ModuleNotFoundError: No module named 'test_3'
    print("Running test_option_3")
    main()


@ray.remote
class MockActor1:
    def __init__(self):
        self.attribute = mock_mock_me()


@patch("patching_ray.actor1.mock_me", mock_mock_me)
@patch("patching_ray.actor1.Actor1", MockActor1)
def test_actor1_option_3():
    main()
