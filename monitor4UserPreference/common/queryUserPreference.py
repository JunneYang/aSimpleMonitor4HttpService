#!/usr/bin/env python
#-*- coding: utf-8 -*-
import upps_pb2
import rpc_client.client.channel as channel
import rpc_client.client.controller as controller
import rpc_client.client.transport as transport
import rpc_client.client.stub as stub
import rpc_client.client.protocol as protocol
import rpc_client.client.error as error

def queryUserPreference():
    try:
        request = upps_pb2.GetUserPreferenceRequest()
        request.header.servicekey = "tuangou"
        request.header.secretkey = "10af214253a015b8ffdfbac9f98077b4"
        request.header.subservice = "userpreference"
        request.cuid = "fff85c03bb3eaf403ae4e966a41d4e11"
        request.srcType.append(12)
        request.include_tag.append('76')
        request.include_tag.append('AAAAA')
        request.exclude_tag.append('61916')

        ctrl = controller.RpcController()
        ctrl.serviceName = "UserService"
        tt = transport.Transport()
        pp = protocol.PbProtocol(tt)
        cc = channel.RpcChannel(pp, "10.52.75.52", 7788, True)
        ctrl.response_buffer_size = 10000
        ss =stub.RpcStub(upps_pb2.UserService_Stub, cc, request, ctrl)
        response = ss.GetUserPreference(request, ctrl)
        #print response

        key='values'
        res = []
        obj_list = eval('response.%s' %key)
        for o in obj_list:
            data = {}
            for f in ["tag","level","value","srcType"]:
                try:
                    if o.HasField(f):
                        exec('data["%s"]=o.%s'%(f, f))
                except:
                    exec('data["%s"]=o.%s'%(f, f))
            res.append(data)

        result_list=res
        result_list = sorted(result_list, key=lambda x:(x.get('level', 0),x.get('value', 0)))
        #print(result_list)
        exp_list=[{'tag': u'AAAAA', 'srcType': 12}, {'tag': u'76', 'srcType': 12, 'value': 3.4571070671081543, 'level': 1}]
        #assert(exp_list == result_list)
        assert(len(result_list) != 0)
        return 0
    except Exception:
        return -1

