# Description
You can use this module to retrieve price information, product details, and more from Amazon without needing to understand the SP-API provided by Amazon.

# Usage
Please create a "data" folder directly under the Project folder and create a "config.yaml" file within it.
Next, describe authentication information in the config.yaml file as follows.

amazon_config:
  SPAPI_LWA_Client_ID: ''
  SPAPI_LWA_Client_PW: ''
  SPAPI_Refresh_Token: ''
  SPAPI_Access_Token_Endpoint: 'https://api.amazon.com/auth/o2/token'
  SPAPI_IAM_User_Access_Key: ''
  SPAPI_IAM_User_Secret_Key: ''
  SPAPI_Service: 'execute-api'
  SPAPI_Domain: 'sellingpartnerapi-fe.amazon.com'
  SPAPI_MarketplaceId: 'A1VC38T7YXB528'
  SPAPI_Region: 'us-west-2'
  SPAPI_Endpoint: 'https://sellingpartnerapi-fe.amazon.com'
  SPAPI_SignatureMethod: 'AWS4-HMAC-SHA256'
  SPAPI_UserAgent: ''
  SPAPI_Method: 'GET'

# Install
pip install sp_lib
