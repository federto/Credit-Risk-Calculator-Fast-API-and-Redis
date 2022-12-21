import json
import os
import time

import numpy as np
import redis
import settings
import pickle
import pandas as pd
import sklearn

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = redis.Redis(host=settings.REDIS_IP,port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)


def predict(data):
    """
    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.

    Parameters
    ----------
    image_name : str
        Image filename.

    Returns
    -------
    class_name, pred_probability : tuple(str, float)
        Model predicted class as a string and the corresponding confidence
        score as a number.
    """
    class_name = None
    pred_probability = None
    
    pickle_in = open('/src/preprocessing_pipeline.pkl','rb')

    preproccesing = pickle.load(pickle_in)

    pickle_in_model = open('/src/model_lightgbm.pkl','rb')

    model = pickle.load(pickle_in_model)

    credit_df = pd.DataFrame([data])

    x = preproccesing.transform(credit_df)

    preds = model.predict(x)

    preds_proba = model.predict_proba(x)
    predict_proba_first = preds_proba[:,1]
    J = round(predict_proba_first[0],2)
    


    return {"preds":preds[0],"preds_proba":J*1000}

    
def classify_process():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, uses the loaded ML
    model to get predictions and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.
    """
    while True:
        # Inside this loop you should add the code to:
        #   1. Take a new job from Redis
        #   2. Run your ML model on the given data
        #   3. Store model prediction in a dict with the following shape:
        #      {
        #         "prediction": str,
        #         "score": float,
        #      }
        #   4. Store the results on Redis using the original job ID as the key
        #      so the API can match the results it gets to the original job
        #      sent
        # Hint: You should be able to successfully implement the communication
        #       code with Redis making use of functions `brpop()` and `set()`.
        # TODO
        # Take a new job from Redis
         q = db.brpop(settings.REDIS_QUEUE)[1]
         print(q)

         # Decode the JSON data for the given job
         q = json.loads(q)

         # Important! Get and keep the original job ID
         job_id = q["id"]
         preds = predict(q["data"])
         output = {"Score": str(preds["preds_proba"]),"Result":str(preds["preds"])}
         
         # update the key value store, so the client can get the results.
         db.set(job_id, json.dumps(output))

         # Don't forget to sleep for a bit at the end
         time.sleep(settings.SERVER_SLEEP)

if __name__ == "__main__":
    # Now launch process
    print("Launching ML service...")
    classify_process()
