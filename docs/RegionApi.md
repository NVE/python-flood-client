# varsom_flood_client.RegionApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/flood/v1.0.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**region_get**](RegionApi.md#region_get) | **GET** /api/Region/{countyId} | 

# **region_get**
> list[County] region_get(county_id)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.RegionApi()
county_id = 'county_id_example' # str | 

try:
    api_response = api_instance.region_get(county_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **county_id** | **str**|  | 

### Return type

[**list[County]**](County.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

