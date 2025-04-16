from unittest.mock import MagicMock, patch

import numpy as np

from patching_ray.repro_infer import main
from tests.common import mock_load_model_and_preprocessor, mock_mock_me


def mock_validator_init(self, *args, **kwargs):
    print("#" * 50)
    print("Using mock_validator_init")
    print("#" * 50)
    self.model = MagicMock()
    self.model.predict.side_effect = lambda x: np.random.random(size=(len(x),))


@patch("patching_ray.repro_infer.load_model_and_preprocessor", mock_load_model_and_preprocessor)
@patch("patching_ray.repro_infer.Validator.__init__", mock_validator_init)
def test_option_2():
    # Option 2: Also mock the Validator.__init__ method
    # This does not work. Ray seems to pickle the original class without the patched init
    main()


def mock_actor1_init(self, *args, **kwargs):
    print("#" * 50)
    print("Using mock_actor1_init")
    print("#" * 50)
    self.attribute = mock_mock_me()


@patch("patching_ray.actor1.mock_me", mock_mock_me)
@patch("patching_ray.actor1.Actor1.__init__", mock_actor1_init)
def test_actor1_option_2():
    main()
