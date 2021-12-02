import os
import shutil
import logging

from tests.addition_test import test_static_calculation_addition


from tests.division_test import test_calculation_division
from tests.multiplication_test import test_calculation_multiplication
from tests.subtraction_test import test_static_calculation_subtraction
from calc.utils.file_reader import PandasFileReader
import pathlib

BASE_DIR = pathlib.Path().resolve()

input_path = os.path.join(BASE_DIR, "tests", "input_csv_files")
results_path = os.path.join(BASE_DIR, "tests", "result")
output_file_path = os.path.join(BASE_DIR, "tests", "done_csv_files")

logging.basicConfig(
    filename=os.path.join(results_path, "results.log"),
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

def process_files(file_path):
    for file_name in os.listdir(file_path):
        input_file_full_path = os.path.join(file_path, file_name)
        print(f"Processing File {file_name}")
        panda_frame = PandasFileReader(file_name).read_file()
        if "addition" in file_name:
            test_static_calculation_addition(panda_frame)
        elif "subtraction" in file_name:
            test_static_calculation_subtraction(panda_frame)
        elif "multiplication" in file_name:
            test_calculation_multiplication(panda_frame)
        elif "division" in file_name:
            test_calculation_division(panda_frame, file_name)
        shutil.move(input_file_full_path, output_file_path)
        print("Done Processing")

if __name__ == "__main__":
    process_files(input_path)
