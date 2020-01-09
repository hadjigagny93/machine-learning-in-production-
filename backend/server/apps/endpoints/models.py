from django.db import models


class Endpoint(models.Model):

    """
    The Endpoint object represents a ML API endpoint 

    attributes:
    -----------
    name:
    owner:
    created_at:
    """
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    creatd_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):

    """
    The ML algorithm represent the ML algorithm object.
    
    Attributes:
    -----------
    name: the name of the algorithm 
    description: a short description of how the algorithm works 
    code: the lago code 
    version: version of algo similar to software versioning 
    owner: the name of the owner 
    created_at: the date when the algo was added
    parent_endpoint: the reference of the endpoint 
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):

    """
    the MLAlgoprithmStatus represents the status of the algorthim which can be changed during the time.

    Attributes:
    ----------
    status: the status of the algorithm in the endpoint. Can be: testing, staging, ab_testing, production 
    active: the boolean flag which point to the currently active status 
    created_by: the name of the creator
    created_at: the date of the status creation
    parent_MLalgorithm: the ref. to the corresponding algorithm 
    """
    status = models.CharField(max_length=128)
    active = models.BooleanField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.CharField(max_length=128)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

class MLRequest(models.Model):

    """
    the MLRequest model will keep information about all requests to ML algorithms.

    Attributes:
    ----------
    input_data: the input data to ML algorithm in JSON format 
    full_response: the response of the ML algorithm 
    response: the response of the ML akgorithm in JSON format 
    feedback: the feedback about the response in JSON format 
    created_at: the date when request was created
    parent_mlalgorithm: the reference about MLalgorithm used to compute response 
    """
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)



  

