import ray


# make ray.data less verbose
ray.data.DataContext.get_current().enable_progress_bars = False
ray.data.DataContext.get_current().print_on_execution_start = False

def load_model_and_preprocessor():
    raise Exception("Patching unsuccessful >:C")

class Validator:
    def __init__(self):
        self.model, self.preprocessor = load_model_and_preprocessor()

    def __call__(self, batch):
        return batch
        


def main():
    model, preprocessor = load_model_and_preprocessor()
    print("#"*50)
    print(f"Successfully mocked load_model_and_preprocessor in main(): {type(preprocessor)}")
    print("#"*50)
    
    ds = ray.data.range(1000)
    ds = ds.map_batches(
        Validator,
        concurrency=1
    )

    df = ds.to_pandas()
    print(df)
if __name__ == "__main__":
    main()
