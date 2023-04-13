package com.smart.placeholder;

import sun.misc.BASE64Decoder;
import sun.misc.BASE64Encoder;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import java.security.Key;
import java.security.SecureRandom;

public class DESUtils {
    // 指定 DES 加密解密所用的密钥
    private static Key key;
    private static String KEY_STR = "myKey";
    static {
        try {
            KeyGenerator keyGenerator = KeyGenerator.getInstance("DES");
            keyGenerator.init(new SecureRandom(KEY_STR.getBytes()));
            key = keyGenerator.generateKey();
            keyGenerator = null;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // 对字符串进行 DES 加密，返回 BASE64 编码的加密字符串
    public static String getEncryptString(String str) {
        BASE64Encoder base64en = new BASE64Encoder();
        try {
            byte[] strBytes = str.getBytes("UTF8");
            Cipher cipher = Cipher.getInstance("DES");
            cipher.init(Cipher.ENCRYPT_MODE, key);
            byte[] encryptStrBytes = cipher.doFinal(strBytes);
            return base64en.encode(encryptStrBytes);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // 对 BASE64 编码的加密字符串进行解密，返回解密后的字符串
    public static String getDecryptString(String str) {
        BASE64Decoder base64de = new BASE64Decoder();
        try {
            byte[] strBytes = base64de.decodeBuffer(str);
            Cipher cipher = Cipher.getInstance("DES");
            cipher.init(Cipher.DECRYPT_MODE, key);
            byte[] decryptStrBytes = cipher.doFinal(strBytes);
            return new String(decryptStrBytes, "UTF8");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // 对入参的字符串进行加密，打印出加密后的串
    public static void main(String[] args) throws Exception {
        if (args == null || args.length < 1) {
            System.out.println("请输入要加密的字符，用空格分隔");
        } else {
            for (String arg: args) {
                System.out.println(arg + ": " + getEncryptString(arg));
            }
        }
    }
}
