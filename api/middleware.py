import json
import time
from uuid import uuid4

import redis
import settings

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = redis.Redis(host=settings.REDIS_IP,
     port=settings.REDIS_PORT, db=settings.REDIS_DB_ID
)


def model_predict(data):
    """
    Receives a dict and queues the job into Redis.
    Will loop until getting the answer from our ML service.

    Parameters
    ----------
    data : dict
        Name for the image uploaded by the user.

    Returns
    -------
    prediction, score : tuple(str, float)
        Model predicted class as a string and the corresponding confidence
        score as a number.
    """
   
    score = None


    # Assign an unique ID for this job and add it to the queue.
    # We need to assing this ID because we must be able to keep track
    # of this particular job across all the services
    # TODO
    job_id = str(uuid4())

    # Create a dict with the job data we will send through Redis having the
    # following shape:
    # {
    #    "id": str,
    #    "image_name": str,
    # }
    # TODO

    job_data = {"id": job_id, "data": data}

    # Send the job to the model service using Redis
    # Hint: Using Redis `lpush()` function should be enough to accomplish this.
    # TODO
    job_results = db.lpush(settings.REDIS_QUEUE, json.dumps(job_data))

    # Loop until we received the response from our ML model
    while True:
        # Attempt to get model predictions using job_id
        # Hint: Investigate how can we get a value using a key from Redis
        # TODO
        job_results = db.get(job_id)
        if job_results:
            results = json.loads(job_results)
            #prediction = results["prediction"]
            score = results["Score"]
            result = results["Result"]            
            # Don't forget to delete the job from Redis after we get the results!
            # Then exit the loop
            # TODO
            db.delete(job_id)
            return {"Score":score, "Result":result}

        # Sleep some time waiting for model results
        time.sleep(settings.API_SLEEP)
    
