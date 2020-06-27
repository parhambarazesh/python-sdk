from dapr import Dapr

import proto.response_pb2 as response_messages

with Dapr() as d:
    # Create a typed message with content type and body
    resp = d.invoke_service(
        id='invoke-receiver',
        method='my_method',
        data=b'SOME_DATA',
        content_type='text/plain; charset=UTF-8',
    )

    res = response_messages.CustomResponse()
    resp.unpack(res)

    # Print Result
    print(res, flush=True)
