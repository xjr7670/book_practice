package com.xjr7670;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.text.MessageFormat;
// import net.sf.json.JSONObject;

public class GetGeoData {

    public String getLngLat(String address) throws JSONException {
        StringBuffer json = new StringBuffer();
        HttpURLConnection conn = null;
        InputStream is = null;
        BufferedReader br = null;
        StringBuffer sbf = new StringBuffer();
        try {
            String encodedAddress = java.net.URLEncoder.encode(address, "UTF-8");
            String city = java.net.URLEncoder.encode("北京", "UTF-8");
            String url = MessageFormat.format("https://restapi.amap.com/v3/geocode/geo?address={0}&city={1}&output=JSON&key=249d1a9542822da789f5e2e34534698b", encodedAddress, city);
            URL u = new URL(url);
            System.out.println(u.toString());
            conn = (HttpURLConnection) u.openConnection();
            conn.setRequestMethod("GET");
            conn.connect();
            is = conn.getInputStream();
            br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            String inputline = null;
            while((inputline = br.readLine())!=null){
                sbf.append(inputline);
                sbf.append("\r\n");
            }
            System.out.println(sbf.toString());
        } catch (MalformedURLException e){
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != br) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (null != is) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            conn.disconnect();
        }
        String jsonStr = sbf.toString();
        JSONObject object = new JSONObject(jsonStr);
        JSONArray geocodesArr = object.getJSONArray("geocodes");
        JSONObject info = geocodesArr.getJSONObject(0);
        return info.getString("location");

    }

    public static void main(String[] args) throws JSONException {

        GetGeoData test = new GetGeoData();
        String add = test.getLngLat("东城区和平里街道");
        System.out.println(add);
    }

}