# The correct way to patch the Actor2 class

from unittest.mock import patch

from patching_ray.actor2 import main
from tests.test_util import mock_mock_me


@patch("patching_ray.actor2.mock_me", mock_mock_me)
def test_actor2():
    main()
