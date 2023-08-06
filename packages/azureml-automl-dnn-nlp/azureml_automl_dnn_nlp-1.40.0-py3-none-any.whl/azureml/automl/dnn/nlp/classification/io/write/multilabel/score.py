# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Score text dataset from model produced by training run."""

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType

from azureml.automl.dnn.nlp.common.constants import ScoringLiterals, OutputLiterals

import numpy as np
import pandas as pd
import json
import pickle
import os


def init():
    """This function is called during inferencing environment setup and initializes the model"""
    global model
    model_path = os.path.join(os.getenv(ScoringLiterals.AZUREML_MODEL_DIR_ENV), OutputLiterals.MODEL_FILE_NAME)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)


@input_schema('data', PandasParameterType(pd.DataFrame({'text': ["This is an example"]})))
@output_schema(NumpyParameterType(np.array([0])))
def run(data: pd.DataFrame) -> str:
    """ This is called every time the endpoint is invoked. It returns the prediction of the input data

    :param data: input data provided by the user
    :type data: pd.DataFrame
    :return: json string of the result
    :rtype: str
    """
    try:
        fin_outputs = model.predict(data)
        return json.dumps({"result": [list(item) for item in fin_outputs]})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
