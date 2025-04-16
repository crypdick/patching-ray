from unittest.mock import patch

from patching_ray.repro_infer import main
from tests.common import mock_load_model_and_preprocessor, mock_mock_me


@patch("patching_ray.repro_infer.load_model_and_preprocessor", mock_load_model_and_preprocessor)
def test_option_1():
    # Option 1: Mock the load_model_and_preprocessor function
    # this correctly patches the load_model_and_preprocessor function in the main function,
    # but not in the Validator.__init__ method because Ray gets the actual function and not the patched one.
    main()


@patch("patching_ray.actor1.mock_me", mock_mock_me)
def test_actor1_option_1():
    main()
