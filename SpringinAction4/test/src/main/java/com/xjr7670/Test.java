package com.xjr7670;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.text.MessageFormat;
// import net.sf.json.JSONObject;

public class Test {

    public String getLngLat(String address) throws JSONException {
        StringBuffer json = new StringBuffer();

        try {
            String encodedAddr = java.net.URLEncoder.encode(address, "UTF-8");
            String city = java.net.URLEncoder.encode("北京", "UTF-8");
            String url = MessageFormat.format("https://restapi.amap.com/v3/geocode/geo?address={0}&city={1}&output=JSON&key=249d1a9542822da789f5e2e34534698b", encodedAddr, city);
            URL u = new URL(url);
            URLConnection yc = u.openConnection();
            //读取返回的数据
            BufferedReader in = new BufferedReader(new InputStreamReader(yc.getInputStream(),"UTF-8"));
            String inputline = null;
            while((inputline=in.readLine())!=null){
                json.append(inputline);
                System.out.println(json.toString());
            }
            in.close();
        }catch(MalformedURLException e){
            System.out.println(e);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        String jsonStr=json.toString();
        JSONObject object = new JSONObject(jsonStr);
        JSONArray geocodesArr = object.getJSONArray("geocodes");
        JSONObject info = geocodesArr.getJSONObject(0);
        return info.getString("location");

    }

    public static void main(String[] args) throws JSONException {

        Test test = new Test();
        String add = test.getLngLat("东城区和平里街道");
        System.out.println(add);
    }

}