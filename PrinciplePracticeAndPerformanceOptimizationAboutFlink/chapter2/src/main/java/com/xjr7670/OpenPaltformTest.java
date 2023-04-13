package com.xjr7670;

import com.alibaba.gov.api.client.AtgBusClient;
import com.alibaba.gov.api.client.DefaultAtgBusClient;
import com.alibaba.gov.api.domain.AtgBusSecretKey;
import com.alibaba.gov.api.internal.util.HttpMethodEnum;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OpenPaltformTest {
    public static void main(String[] args) {
        execut();
    }
    public static void execut() {
        String gatewayUrl = "http://47.94.127.133:8087/openapi";
        String appId = "100201";
        List<AtgBusSecretKey> secretKeys = new ArrayList<>();
        AtgBusSecretKey atgBusSecretKey = new AtgBusSecretKey("qcgv0zjoez2wxwd95btd1u7lrsu7xf8a", "eGwx1ZDbV3g6neAhl7WVZBJV");
        secretKeys.add(atgBusSecretKey);

        //2. 初始化客户端
        AtgBusClient atgBusClient = new DefaultAtgBusClient(gatewayUrl, appId, secretKeys);
        Map map = new HashMap<String, Object>();
        map.put("name", "Cavin");
        atgBusClient.execute("{'name':'cavin'}", HttpMethodEnum.POST, map);
        //3. 找到对应服务的request，拼装业务信息

       // GovMetadatacenterXjrDatashareApiTestPostRequest govMetadatacenterXjrDatashareApiTestPostRequest = new GovMetadatacenterXjrDatashareApiTestPostRequest();
        //4. 请求开放服务，获取response
        //GovMetadatacenterXjrDatashareApiTestPostResponse response = atgBusClient.execute(govMetadatacenterXjrDatashareApiTestPostRequest);
    }
}
