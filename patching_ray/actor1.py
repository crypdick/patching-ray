import ray

from patching_ray.common import mock_me


@ray.remote
class Actor1:
    def __init__(self):
        self.attribute = mock_me()


def main():
    ray.init()

    mock_me()
    print("mock_me successfully patched in main()")

    actor = Actor1.remote()
    ray.get(actor.attribute)


if __name__ == "__main__":
    main()
