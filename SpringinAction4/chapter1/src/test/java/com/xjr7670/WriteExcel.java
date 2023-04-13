package com.xjr7670;

import java.io.FileOutputStream;
import java.io.OutputStream;
import com.alibaba.easyexcel.ExcelWriter;

public class WriteExcel {
    @Test
    public static writeExcel() throws Exception {
        OutputStream out = new FileOutputStream("e://temp//test.xlsx");
        ExcelWriter writer = EasyExcelFactory.getWriter(out);
    }
}
