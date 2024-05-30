from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        if(self.IsValid(event)==False):
            message = self.GetErrorMessage( event)
            return  {
             "statusCode": 400,
             "message": message}
           
        
        return {
         "statusCode": 200,
         "message": "Hello from Lambda" }
    
    def IsValid(self, event):
        path = event.get('rawPath', '')

        httpmethod = event.get('httpMethod', '')

        print("path =" + path )
        if path == 'hello' and httpmethod =='GET':
            return True
        
        return False
    
    
    def GetErrorMessage(self, event) :
        # Retrieve the request path from the event object
        path = event.get('rawPath', '')
        httpmethod = event.get('httpMethod', '')
                
        # Retrieve query string parameters, if any
        query_string = event.get('rawQueryString', '')
        
        # Retrieve the host header to construct the full URL
        host ='host'# event.get('headers', '').get('host', '')
        
        # Default protocol is https
        protocol = 'https'
        
        # Construct the full URL
        if query_string:
            full_url = f"{protocol}://{host}{path}?{query_string}"
        else:
            full_url = f"{protocol}://{host}{path}"
        
        # Log the URL (optional)
        print(f"Request URL: {full_url}")
        #return  "Bad request syntax or unsupported method. Request path: {path}. HTTP method: {httpmethod}".format(path, httpmethod)
        return "Bad request syntax or unsupported method. Request path: {path}. HTTP method: {httpmethod}".format(path=path, httpmethod=httpmethod)


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)


