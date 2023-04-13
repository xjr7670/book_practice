package org.example;

import net.sf.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import javax.servlet.ServletException;

public class MyServiceTestMain {
    public static void main(String[] args) throws ServletException, IOException {
        if (args.length < 1) {
            System.out.println("please input your config file path");
        }
        String filePath = args[0];
        File file = new File(filePath);
        FileReader reader = new FileReader(file);
        BufferedReader br = new BufferedReader(reader);
        StringBuilder sb = new StringBuilder();
        String line = null;
        while ((line = br.readLine()) != null) {
            sb.append(line);
        }
        JSONObject config = JSONObject.fromObject(sb.toString());
        String SID = config.getString("sid");
        String RID = config.getString("rid");
        String APPKEY= config.getString("appkey");
        String whereListValue = config.getString("wherelist");
        String result=ServiceUtils.doPost(SID, RID, APPKEY,whereListValue);
        System.out.println("查询结果:"+result);
    }
}
