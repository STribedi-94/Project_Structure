import logging
import os
from datetime import datetime

# structure of our logging text file

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



# Lest test if the logging is working properly

# if __name__=="__main__":
#     logging.info("Logging has statrted")


# To test if the logging file is working type-- python .\src\logger.py   and enter
# It will create a log file in the working directory