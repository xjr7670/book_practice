package org.example;


import net.sf.json.JSONObject;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;


/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException {
        if (args.length < 1) {
            System.out.println("Please specified the config path!");
        }
//        System.out.println(System.getProperty("user.dir"));
        String filePath = args[0];
        File file = new File(filePath);
        List lines = FileUtils.readLines(file, "UTF-8");
        String jsonString = String.join("", lines);
//        System.out.println(jsonString);
        JSONObject json = JSONObject.fromObject(jsonString);
        JSONObject sender = json.getJSONObject("sender");
        String username = sender.getString("username");
        String password = sender.getString("password");
        System.out.printf("Username: %s\n", username);
        System.out.printf("Password: %s", password);
    }
}
