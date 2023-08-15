using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Net;
using System.Net.Mail;
using System.IO;
using System.Collections;
using System.ComponentModel;
using System.IO.Compression;
using Excel = Microsoft.Office.Interop.Excel;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using MySql.Data;
using MySql.Data.MySqlClient;
using Spire.Pdf;
using iTextSharp.text.pdf;
using iTextSharp.text;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Chapter13.Ch13Ex12();

            Console.ReadKey();
        }

        private static void mergePDFFiles(string[] fileList, string outMergeFile)
        {
            PdfReader reader;
            Document document = new Document();
            PdfWriter write = PdfWriter.GetInstance(document, new FileStream(outMergeFile, FileMode.Create));
            document.Open();
            PdfContentByte cb = write.DirectContent;
            PdfImportedPage newPage;
            for (int i = 0; i < fileList.Length; i++)
            {
                reader = new PdfReader(fileList[i]);
                int iPageNum = reader.NumberOfPages;
                for (int j = 1; j <= iPageNum; j++)
                {
                    document.NewPage();
                    newPage = write.GetImportedPage(reader, j);
                    cb.AddTemplate(newPage, 0, 0);
                }
            }
            document.Close();
            Console.WriteLine("combine finish!!!");
        }

        // C# 多线程        
        static void Thread1(object obj)
        {
            Console.WriteLine(obj);
        }

        /****************************/

        // C# 连接 mysql
        static void ConnectMysql()
        {
            const string conStr = "Data Source='127.0.0.1';User Id='hive';Password='hive';Database='test';Port=3306";
            MySqlConnection conn = new MySqlConnection(conStr);
            conn.Open();
            Console.WriteLine("连接成功！");
            MySqlCommand query = new MySqlCommand("select * from website", conn);
            
            MySqlDataReader reader = query.ExecuteReader();
            Console.WriteLine("id\t\tname\t\turl\t\talexa\t\tcountry");
            while (reader.Read())
            {
                Console.Write($"{reader.GetString("id"), -5:d}");
                Console.Write($"{reader.GetString("name"), -15:s}");
                Console.Write($"{reader.GetString("url"), -30:s}");
                Console.Write($"{reader.GetString("alexa"), -10:d}");
                Console.WriteLine($"{reader.GetString("country"), -20}");
            }
        }


        /*********************/

        static void TestRegex()
        {
            string numStr = "B";

            bool isNum = Regex.IsMatch(numStr, "\\d+");
            if (Regex.IsMatch(numStr, "\\d+"))
            {
                Console.WriteLine($"输入的是个数字：${numStr}");
            } else
            {
                if (!Regex.IsMatch(numStr, @"[A-Za-z]+"))
                {
                    throw new Exception($"无效的输入 {numStr}，只能接收26个英文字母，并且不区分大小写");
                }
                // 统一转大写
                char[] chars = numStr.ToUpper().ToCharArray();
                int index = 0;
                for (var i = 0; i < chars.Length; i++)
                {
                    index += ((int)chars[i] - (int)'A' + 1) * (int)Math.Pow(26, chars.Length - i - 1);
                }
                Console.WriteLine($"输入的是字母：{numStr}，转换后是：{index}");
            }
        }


        static void TestEveryThing()
        {
            List<int> numbers = new List<int> { 1, 1 };

            while (numbers.Count < 20)
            {
                int pre = numbers[numbers.Count - 1];
                int pre2 = numbers[numbers.Count - 2];

                numbers.Add(pre + pre2);
            }

            foreach(int n in numbers)
            {
                Console.WriteLine(n);
            }

           
        }

        static void ZipOperation()
        {
            string startPath;
            string zipPath;

            // ZipFile.CreateFromDirectory(startPath, zipPath, 0, includeBaseDirectory:true);

            DirectoryInfo directory = new DirectoryInfo(@"E:\temp");
            DirectoryInfo[] subdirs = directory.GetDirectories();
            foreach(DirectoryInfo info in subdirs)
            {
                startPath = info.FullName;
                zipPath = startPath + ".zip";
                FileInfo fi = new FileInfo(zipPath);
                if (fi.Exists)
                {
                    fi.Delete();
                }
                ZipFile.CreateFromDirectory(startPath, zipPath, 0, true);
                Console.WriteLine(info.FullName);
            }
            Console.ReadKey();
        }

        static void ReadJson()
        {
            string jsonFilePath = @"E:\temp\config.json";
            string jsonData = File.ReadAllText(jsonFilePath);
            JObject jObject = (JObject)JsonConvert.DeserializeObject(jsonData);
            JArray jArray = (JArray) jObject["directories"];
            foreach(JObject jo in jArray)
            {
                Console.WriteLine(jo["region"] + "\t\t" + jo["manager"]);
            }
            Console.ReadKey();
        }

        static void SendMail()
        {
            MailMessage mail = new MailMessage();
            mail.From = new MailAddress("xjr7670@163.com", "", Encoding.UTF8);
            mail.To.Add(new MailAddress("xjr30226@126.com", "Cavin@126", Encoding.UTF8));
            mail.To.Add(new MailAddress("284182470@qq.com", "Cavin@qq", Encoding.UTF8));
            mail.Subject = "C#发送";
            mail.SubjectEncoding = Encoding.UTF8;
            mail.IsBodyHtml = false;
            mail.Body = "这封邮件由C#程序发送";
            mail.BodyEncoding = Encoding.UTF8;
            mail.Attachments.Add(new Attachment(@"E:\temp\潮汕.zip"));

            SmtpClient smtp = new SmtpClient();
            smtp.Host = "smtp.163.com";
           
            smtp.EnableSsl = true;
            smtp.UseDefaultCredentials = false;
            // smtp.Credentials = new NetworkCredential("284182470@qq.com", "kalpiqvmnsawcaff");
            smtp.Credentials = new NetworkCredential("xjr7670@163.com", "GGTAIUYIJZMXOBNI");
            smtp.Send(mail);
            
            Console.WriteLine("邮件发送成功");
            Console.ReadKey();
        }

        static void ExcelOperation()
        {
            Excel.Application xlApp = new Excel.Application();
            Excel.Workbook wbk = xlApp.Workbooks.Open(@"E:\temp\员工信息-20201215.xlsx");
            Excel.Worksheet sht = wbk.Worksheets[1];

            Excel.Workbook wbk2 = xlApp.Workbooks.Add();
            Excel.Worksheet sht2 = wbk2.Worksheets[1];

            sht.Range[sht.Cells[1, 1], sht.Cells[1, 10]].Copy(sht2.Range[sht2.Cells[1, 1], sht2.Cells[1, 10]]);
            
            // Console.WriteLine(sht.Range["A2"].Text);

            
            wbk.Close(SaveChanges: false);
            wbk2.SaveAs(@"e:\temp\myexcel.xlsx", Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing);
            wbk2.Close();
            xlApp.Quit();
            Console.ReadKey();
        }
    }

    class BackGroudTest
    {
        private int Count;
        public BackGroudTest(int count)
        {
            this.Count = count;
        }
        public void RunLoop()
        {
            // 获取当前线程名称
            string threadName = Thread.CurrentThread.Name;
            for (int i = 0; i < Count; i++)
            {
                Console.WriteLine("{0} 计数：{1}", threadName, i.ToString());
                Thread.Sleep(1000);
            }
            Console.WriteLine("{0} 完成计数。", threadName);
        }
    }
}
