from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline



STAGE_NAME = 'Data Ingestion Pipeline'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\nx========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Pipeline'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\nx========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation Pipeline'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\nx========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e
    
    

STAGE_NAME = 'Model Trainer Pipeline'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\nx========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e