import ray

from patching_ray.common import mock_me


@ray.remote
class Actor2:
    def __init__(self, loader):
        self.attribute = loader()


def main():
    ray.init()

    mock_me()
    print("mock_me successfully patched in main()")

    actor = Actor2.remote(mock_me)
    ray.get(actor.attribute)


if __name__ == "__main__":
    main()
