from unittest.mock import patch

from patching_ray.actor1 import main
from tests.test_util import mock_mock_me


def mock_actor1_init(self, *args, **kwargs):
    print("#" * 50)
    print("Using mock_actor1_init")
    print("#" * 50)
    self.attribute = mock_mock_me()


@patch("patching_ray.actor1.mock_me", mock_mock_me)
@patch("patching_ray.actor1.CallableClass.__init__", mock_actor1_init)
def test_actor1_option_2():
    main()
