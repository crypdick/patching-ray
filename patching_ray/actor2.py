import ray

from patching_ray.common import mock_me

# make ray.data less verbose
ray.data.DataContext.get_current().enable_progress_bars = False
ray.data.DataContext.get_current().print_on_execution_start = False


class CallableClass:
    def __init__(self, loader):
        self.attribute = loader()

    def __call__(self, batch):
        return batch


def main():
    mock_me()
    print("#" * 50)
    print(f"Successfully mocked mock_me in main(): {type(mock_me)}")
    print("#" * 50)

    ds = ray.data.range(1000)
    ds = ds.map_batches(CallableClass, concurrency=1, fn_constructor_kwargs={"loader": mock_me})

    print(ds.to_pandas())


if __name__ == "__main__":
    main()
