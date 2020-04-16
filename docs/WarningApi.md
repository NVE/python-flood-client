# varsom_flood_client.WarningApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/flood/v1.0.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warning_all**](WarningApi.md#warning_all) | **GET** /api/Warning/All/{langkey}/{startdate}/{enddate} | 
[**warning_county**](WarningApi.md#warning_county) | **GET** /api/Warning/County/{county}/{langkey}/{startdate}/{enddate} | 
[**warning_get**](WarningApi.md#warning_get) | **GET** /api/Warning/{langkey}/{startdate}/{enddate} | 
[**warning_municipality**](WarningApi.md#warning_municipality) | **GET** /api/Warning/Municipality/{municipality}/{langkey}/{startdate}/{enddate} | 

# **warning_all**
> list[Warning] warning_all(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.WarningApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_all(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[Warning]**](Warning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_county**
> list[Warning] warning_county(county, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.WarningApi()
county = 'county_example' # str | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_county(county, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_county: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **county** | **str**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[Warning]**](Warning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_get**
> list[Warning] warning_get(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.WarningApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_get(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[Warning]**](Warning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_municipality**
> list[Warning] warning_municipality(municipality, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_flood_client
from varsom_flood_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_flood_client.WarningApi()
municipality = 'municipality_example' # str | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_municipality(municipality, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_municipality: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **municipality** | **str**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[Warning]**](Warning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/javascript, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

