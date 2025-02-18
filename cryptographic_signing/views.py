from django.shortcuts import render, HttpResponse
from django.core import signing
from time import sleep


def index(request):
    # signer = signing.Signer()
    signer = signing.TimestampSigner()
    
    # data = "Hello world"
    # signed_data = signer.sign(data)
    # original = signer.unsign(signed_data)
    
    # data = "Hello world"
    # signed_data = signer.sign(data)
    # try:
    #     signed_data += "m"
    #     original = signer.unsign(signed_data)
    # except signing.BadSignature:
    #     return HttpResponse("Tampering detected!")
    
    data = "Hello world"
    signed_data = signer.sign(data)
    # sleep(11)
    original = signer.unsign(signed_data, max_age=10)
    
    
    result = f'''
    <div>
        <p>signed_data: {signed_data}</p>
        <p>original: {original}</p>
    </div>
    '''
    return HttpResponse(result)