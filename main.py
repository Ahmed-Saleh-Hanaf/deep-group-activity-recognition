import argparse

from utils.config_loader import load_config
from utils.log_handler import setup_logging
from train.train import train
from evaluation.evaluation import evaluate


def main(config_path: str):
    logging = setup_logging()
    logging.info("Loading configuration...")

    # Loading configration file 
    config = load_config(config_path)

    try:
        # Training
        logging.info("Starting training phase...")
        best_model = train(config, logging)
        logging.info("Training completed successfully.")

        # Evaluation
        logging.info("Starting evaluation phase...")
        evaluate(best_model, config, logging)
        logging.info("Evaluation completed successfully.")

    except Exception as e:
        logging.exception("An error occurred during execution.")
        raise e

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deep Group Activity Recognition Pipeline")
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to the configuration YAML file"
    )

    args = parser.parse_args()
    main(args.config)