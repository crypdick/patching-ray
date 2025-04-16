from unittest.mock import patch

from patching_ray.actor1 import main
from tests.test_util import mock_mock_me


@patch("patching_ray.actor1.mock_me", mock_mock_me)
def test_actor1_option_1():
    main()
