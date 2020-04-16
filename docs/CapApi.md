# varsom_flood_client.CapApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/flood/v1.0.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cap_feed**](CapApi.md#cap_feed) | **GET** /api/Cap/Feed/{startdate}/{enddate} | 
[**cap_id**](CapApi.md#cap_id) | **GET** /api/Cap/Id/{id} | 

# **cap_feed**
> FormattedContentResultListAlert cap_feed(startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.CapApi()
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.cap_feed(startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapApi->cap_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**FormattedContentResultListAlert**](FormattedContentResultListAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cap_id**
> FormattedContentResultAlert cap_id(id)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.CapApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.cap_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapApi->cap_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FormattedContentResultAlert**](FormattedContentResultAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

