package com.smart.oxm.xstream;

import com.smart.oxm.domain.User;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.CompactWriter;
import com.thoughtworks.xstream.io.xml.PrettyPrintWriter;

import java.io.*;

public class ObjectStreamSample {
    private static XStream xStream;

    static {
        xStream = new XStream();
    }

    // java 对象转 xml
    public void objectToXml() throws Exception {
        // 实例化序列化对象
        User user = new User();

        // 创建一个 PrintWriter 对象，用于输出
        PrintWriter pw = new PrintWriter("out/ObjectStreamSample.xml");

        // 选用一个 HierarchicalStreamWriter 的实现类来创建输出
        PrettyPrintWriter ppw = new PrettyPrintWriter(pw);
        CompactWriter cw = new CompactWriter(pw);

        // 创建对象输出流
        ObjectOutputStream out = xStream.createObjectOutputStream(ppw);
        out.writeObject(user);
        out.close();
    }

    // XML 转为 java 对象
    public User xmlToObject() throws Exception {
        // 通过对象流进行输入操作
        FileReader reader = new FileReader("out/ObjectStreamSample.xml");
        BufferedReader bufferedReader = new BufferedReader(reader);

        // 创建对象输入流
        ObjectInputStream input = xStream.createObjectInputStream(bufferedReader);

        // 从 XML 文件中读取对象
        User user = (User) input.readObject();
        return user;
    }

    public static void main(String[] args) throws Exception {
        ObjectStreamSample objectStreamSample = new ObjectStreamSample();
        objectStreamSample.objectToXml();
        objectStreamSample.xmlToObject();
    }
}
