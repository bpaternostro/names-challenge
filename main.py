import time

from src.core.constants import RESULTS_STEP2, FINAL_REPORT
from src.core.logs import logging
from src.core.util import *

###############################################################################################################################
###############################################################################################################################
# General comments:
# 1 - I create a generator with a list of dictionaries with the data of the file. Applying rules.
# 2 - Calculates cardinality
# 3 - for step1 --> I create a list of names and lastnames. I filter using defined criteria.
# 4 - for step2 
#       --> I used like input the list created in step 1. I sent a question related to this, but i did not receive an answer.
#       --> returns the generator mixing names and lastnames using sorting

# IMPORTANT: Before running the script complete variables--> 'file_path' and 'n_limit'
###############################################################################################################################
###############################################################################################################################

# INPUT PARAMETERS
file_path = "input_data/coding-test-data.txt"  # filename to be processed
n_limit = 25 # list limit

try:
    start_time = time.time()
    # creating generators
    list_generator_for_cardinality, list_generator, counter = get_limited_generator(
        path=file_path, limit=n_limit, copies=3
    )

    totals = get_cardinality(persons=list_generator_for_cardinality)

    # Step1 - creating internal list
    internal_list = filter_list(limited_list=list_generator)

    # Step2
    step2_result = mix_person_names(person_list=internal_list, last_name=internal_list[-1])
    create_file(file_name=RESULTS_STEP2, rows=step2_result)

    create_html_repo(
        file=RESULTS_STEP2,
        counts=parse_for_final_report(data=totals),
        file_name=file_path,
        rows=str(n_limit),
        time="--- %s seconds ---" % (time.time() - start_time),
    )

    logging.info(
        " File: {file_name} with {n} rows was executed successfully. Please check results in project folder: {path}/{report}".format(
            file_name=file_path, n=len(list(counter)), path=PATH_TO_RESULTS, report=FINAL_REPORT
        )
    )

except Exception as e:
    logging.error(e)
