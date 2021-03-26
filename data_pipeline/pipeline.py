from typing import Generator


# ETL - Pipeline: Extract, Transform, Load. Out
def read_large_dataset(file_name: str) -> Generator:
    with open(file_name) as f:
        for line in f:
            yield line

def split_lines(file_generator: Generator):
    print("Split Lines Generator: ", type(file_generator))
    """Splitte Zeilen in eine Liste (kommasepariert)--
    lifelock,LifeLock,,web,Tempe,AZ,1-May-07,6850000,USD,b
    """
    result = (line.strip().split(',') for line in file_generator)
    return result

def dictify(list_generator: Generator):
    cols = next(list_generator)
    return (dict(zip(cols, data)) for data in list_generator)

def load_data(file_name: str):
    file_generator = read_large_dataset(file_name)
    split_generator = split_lines(file_generator)
    result = dictify(split_generator)
    return result


