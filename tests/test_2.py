from unittest.mock import MagicMock, patch

import numpy as np

from patching_ray.repro_infer import main
from tests.common import mock_load_model_and_preprocessor


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
