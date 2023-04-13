package practice;



import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

import java.io.IOException;

public class JsonParse {
    public static void main(String[] args) {
        JsonParse parse = new JsonParse();
        parse.parse();
    }
    public void parse()  {
        String jsonPath = "e:/temp/config.json";
        String data = "";
        try {
            data = FileIO2.readData(jsonPath);
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
        if (!data.equals("")) {
            JSONObject parser = JSON.parseObject(data);
            JSONObject account = parser.getJSONObject("account");
            JSONObject sender  = account.getJSONObject("sender");
            JSONObject receiver = account.getJSONObject("receiver");
            System.out.println(sender.getString("name"));
            System.out.println(receiver.getString("name"));
        }
    }
}
