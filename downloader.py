import pathlib
import pandas as pd

import logger


NGO_URL = "https://www.ngobureau.go.ug/ngos-search.php"
OUTPUT_DIR = "output"
OUTPUT_FILE = OUTPUT_DIR / "data.csv"


def create_output_dir(output_dir: str):
    logger.info(f"Creating output directory {output_dir}")
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    logger.info("Output directory created")
    return pathlib.Path(output_dir)


def downdload_data():
    logger.info(f"Downloading data from {NGO_URL}")
    data = pd.read_html(NGO_URL)
    logger.info(f"Downdloaded {len(data)} rows")
    return data


def save_data(data, output_file: str):
    logger.info(f"Saving data to {output_file}")
    data.to_csv(output_file, index=False)
    logger.info("Data saved")


def main():
    data = downdload_data()
    output_dir = create_output_dir("output")
    save_data(data, output_dir / "data.csv")


if __name__ == "__main__":
    main()
