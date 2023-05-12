package org.example;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;

import org.apache.commons.lang.StringUtils;



import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class ServiceUtils {

	private static final long serialVersionUID = 1L;


	
	public static String doPost(String sid,String rid,String appKey,String whereListValue) throws ServletException, IOException {
	//	req.setCharacterEncoding("utf-8");
	//	resp.setCharacterEncoding("utr-8");
		MyPage mypage = new MyPage();
		String rtime = "" + System.currentTimeMillis();
		if(StringUtils.isNotEmpty(sid) && StringUtils.isNotEmpty(rid) && StringUtils.isNotEmpty(appKey)){
			String appSecret = getAppSecret(sid,rid,appKey);
			System.out.println("appSecret======================"+appSecret);
			//得到sign值
			String sign = SymmetricEncoder.getAppSecret(rtime, appSecret,sid,rid);
			//String url = "http://192.166.136.54:8181/httpproxy";//正式环境
		    String url = "http://172.26.50.221:8181/httpproxy";//正式环境
			
			
			String serviceNo ="";
			String returnType = "";
			String page = "";
			String pageSize ="2";
			String columns = "";
			String column = "";
			String logical = "";
			String queryValue = "";
			if(1==1){
				net.sf.json.JSONObject j = new net.sf.json.JSONObject();
				j.put("serviceNo", serviceNo);
				j.put("returnType", returnType);
				j.put("page", page);
				j.put("pageSize", pageSize);
				j.put("columns", columns);
				net.sf.json.JSONArray jArray = new net.sf.json.JSONArray();
				net.sf.json.JSONArray jArray2 = new net.sf.json.JSONArray();
				if(StringUtils.isNotEmpty(column) && StringUtils.isNotEmpty(logical)){
					net.sf.json.JSONObject jTemp = new net.sf.json.JSONObject();
					jTemp.put("queryField", column);
					jTemp.put("logical", logical);
					jTemp.put("queryValue", queryValue);
					jArray.add(jTemp);
					jArray2.add(jArray);
				}
				j.put("whereList", jArray2);
				if(StringUtils.isNotEmpty(whereListValue)){
					 JSONArray myJsonArray = JSONArray.fromObject(whereListValue);
					j.put("whereList", myJsonArray);
				}
				//JSONObject j = new JSONObject(remark);
				String jsonStr = post(url,j.toString(),sid,rid,sign,rtime);
			
				if(StringUtils.isNotEmpty(jsonStr)&&!"null".equals(jsonStr)){
					net.sf.json.JSONObject json = net.sf.json.JSONObject.fromObject(jsonStr);
					JSONArray columnsInfoJsonArray = (JSONArray) json.get("columnsInfo");//列信息
					String columnsTwo = json.getString("columns");
					String[] columnsArr = columnsTwo.split(",");
					//List<String> listStr = new ArrayList<String>();
					JSONArray columnsJson = new JSONArray();
					for(String s:columnsArr){
						net.sf.json.JSONObject jsonTemp = new net.sf.json.JSONObject();
						jsonTemp.put("id", s);
						String temp=s;
						//把列备注显示
						for(int p=0;p<columnsInfoJsonArray.size();p++){
							net.sf.json.JSONObject jsonTemp2 = (net.sf.json.JSONObject) columnsInfoJsonArray.get(p);
							if(s.toLowerCase().trim().equals(jsonTemp2.getString("columnName").toLowerCase().trim())){
								if(StringUtils.isNotEmpty(jsonTemp2.getString("columnComments"))){
									temp = jsonTemp2.getString("columnComments");
								}
								break;
							}
						}
						jsonTemp.put("text", temp);
						columnsJson.add(jsonTemp);
					}
					
					
					JSONArray jsonArray = (JSONArray) json.get("dataList");
					List<Map<String,Object>> list = new ArrayList<Map<String,Object>>();
					for(int i=0;i<jsonArray.size();i++){
						net.sf.json.JSONObject jsonTemp = (net.sf.json.JSONObject) jsonArray.get(i);
						Map<String,Object> map = new LinkedHashMap<String,Object>();
						Iterator<String> it=jsonTemp.keys();
						while(it.hasNext()){
							String key = it.next();
							String value = jsonTemp.getString(key);
							//把列备注显示
							for(int p=0;p<columnsInfoJsonArray.size();p++){
								net.sf.json.JSONObject jsonTemp2 = (net.sf.json.JSONObject) columnsInfoJsonArray.get(p);
								if(key.toLowerCase().trim().equals(jsonTemp2.getString("columnName").toLowerCase().trim())){
									if(StringUtils.isNotEmpty(jsonTemp2.getString("columnComments"))){
										key = jsonTemp2.getString("columnComments");
									}
									break;
								}
							}
							map.put(key, value);
						}
						list.add(map);
					}
					
					page = json.getString("page");
					pageSize = json.getString("maxCount");
					String counts = json.getString("counts");
					mypage.setList(list);
					mypage.setFullListSize(Integer.parseInt(counts));
					mypage.setPageNumber(Integer.parseInt(page));
					mypage.setObjectsPerPage(Integer.parseInt(pageSize));
					
					//System.out.println("查询结果:"+jsonStr);
					return jsonStr;
					
				}
			}
		}
		
		return null;
	}
	
	
	public static String post(String strURL, String params,String sid,String rid,String sign,String rtime) {  
        System.out.println(strURL);  
        System.out.println(params); 
        String result = "";
        BufferedReader in = null;
        try {  
            URL url = new URL(strURL);// 创建连接  
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();  
            connection.setDoOutput(true);  
            connection.setDoInput(true);  
            connection.setUseCaches(false);  
            connection.setInstanceFollowRedirects(true);  
            connection.setRequestMethod("POST"); // 设置请求方式  
            connection.setRequestProperty("Accept", "application/json"); // 设置接收数据的格式  
            connection.setRequestProperty("Content-Type", "application/json"); // 设置发送数据的格式  
            connection.setRequestProperty("BJS_sid", sid);
            connection.setRequestProperty("BJS_rid", rid);
            connection.setRequestProperty("BJS_sign", sign);
            connection.setRequestProperty("BJS_rtime", rtime);
            System.out.println("sid================="+sid);	 
            System.out.println("rid================="+rid);	 
            System.out.println("sign================="+sign);	 
            connection.connect();  
            if (params != null && !"".equals(params)) {
                OutputStream outwritestream = connection.getOutputStream();
                outwritestream.write(params.getBytes());
                outwritestream.flush();
                outwritestream.close();
            }
            int responseCode = connection.getResponseCode();  
	    	InputStream inputStream = null;  

	    	
            if (responseCode == 200) {//接收成功
	    		inputStream = new BufferedInputStream(connection.getInputStream());  
            } else {//接收失败  
	    		inputStream = new BufferedInputStream(connection.getErrorStream());  
	    	} 
            
            in = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
			String line;
			while ((line = in.readLine()) != null) {
				result+=line;
			}
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (in != null) {
                try {
                	in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        
        System.out.println("rtime================="+rtime);	 
       
        return result;
    }
	
	public static String getAppSecret(String sid,String rid,String appKey){
		String appSecret="";
		String rtime = "" + System.currentTimeMillis();
		//获取sign值
		String sign = SymmetricEncoder.getAppSecret(rtime, appKey,sid,rid);
		//请求接口获取appSecret
		//String url = "http://172.26.50.221:8080/TISMP/restServiceAPI/nosession/restful/gxservices/auth/refreshappsecret";//正式环境
		String url = "http://172.26.50.221:8181/sysapi/auth/refreshappsecret";
		//String url = "http://192.166.136.54:8181/sysapi/auth/refreshappsecret";
		net.sf.json.JSONObject j = new net.sf.json.JSONObject();
		j.put("BJS_sid", sid);
		j.put("BJS_rid", rid);
		j.put("BJS_rtime", rtime);
		j.put("BJS_sign", sign);
		String jsonStr = post2(url,j.toString());
		if(StringUtils.isNotEmpty(jsonStr)){
			net.sf.json.JSONObject json = net.sf.json.JSONObject.fromObject(jsonStr);
			net.sf.json.JSONObject jsonData = (JSONObject) json.get("data");
			//得到加过密的密文
			String appSecretMi = jsonData.getString("secret");
			//得到解密后的密文
			appSecret = SymmetricEncoder.AESDncode(appKey, appSecretMi);
		}
		return appSecret;
	}
	
	public static String post2(String strURL, String params) {  
        System.out.println(strURL);  
        System.out.println(params); 
        String result = "";
        BufferedReader in = null;
        try {  
            URL url = new URL(strURL);// 创建连接  
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();  
            connection.setDoOutput(true);  
            connection.setDoInput(true);  
            connection.setUseCaches(false);  
            connection.setInstanceFollowRedirects(true);  
            connection.setRequestMethod("POST"); // 设置请求方式  
            connection.setRequestProperty("Accept", "application/json"); // 设置接收数据的格式  
            connection.setRequestProperty("Content-Type", "application/json"); // 设置发送数据的格式  
            connection.connect();  
            if (params != null && !"".equals(params)) {
                OutputStream outwritestream = connection.getOutputStream();
                outwritestream.write(params.getBytes("GBK"));
                outwritestream.flush();
                outwritestream.close();
            }
            int responseCode = connection.getResponseCode();  
	    	InputStream inputStream = null;  

	    	
            if (responseCode == 200) {//接收成功
	    		inputStream = new BufferedInputStream(connection.getInputStream());  
            } else {//接收失败  
	    		inputStream = new BufferedInputStream(connection.getErrorStream());  
	    	} 
            
            in = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
			String line;
			while ((line = in.readLine()) != null) {
				result+=line;
			}
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (in != null) {
                try {
                	in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
     
        System.out.println("================="+result);	 
        return result;
    }


	
}
