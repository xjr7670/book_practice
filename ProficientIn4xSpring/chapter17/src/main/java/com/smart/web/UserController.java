package com.smart.web;

import com.smart.UserService;
import com.smart.domain.Dept;
import com.smart.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.format.datetime.DateFormatter;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.util.FileCopyUtils;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;
import org.springframework.validation.BindingResult;
import org.springframework.validation.ValidationUtils;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.support.SessionStatus;
import org.springframework.web.client.AsyncRestTemplate;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.WebUtils;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.validation.Valid;
import javax.xml.xpath.XPath;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.List;
import java.util.concurrent.Callable;

@Controller
@RequestMapping("/user")
@SessionAttributes("user")
public class UserController {

    private UserService userService;

    @Autowired
    public void setUserService(UserService userService) {
        this.userService = userService;
    }

    @RequestMapping(method = RequestMethod.POST)
    public ModelAndView createUser(User user) {
        userService.createUser(user);
        ModelAndView mav = new ModelAndView();
        mav.setViewName("user/createSuccess");
        mav.addObject("user", user);
        return mav;
    }

    @RequestMapping(value = "/register", method = RequestMethod.GET, params = "!myParam")
    public String register(@ModelAttribute("user") User user) {
        return "user/register";
    }

    @RequestMapping(value = "/delete", method = RequestMethod.POST, params = "userId")
    public String test1(@RequestParam("userId") String userId) {
        // do sth
        return "user/test1";
    }

    @RequestMapping(value = "/show", headers = "content-type=text/*")
    public String test2(@RequestParam("userId") String userId) {
        // do sth
        return "user/test2";
    }

    // ①请求参数按名称匹配的方式绑定到方法入参中，方法返回对应的字符串代表逻辑视图名
    @RequestMapping(value = "/handle1")
    public String handle1(@RequestParam("userName") String userName,
                          @RequestParam("password") String password,
                          @RequestParam("realName") String realName) {
        return "success";
    }

    // ②将Cooke值及报文头属性绑定到入参中、方法返回ModelAndView
    @RequestMapping(value = "/handle2")
    public ModelAndView handle2(@CookieValue("JSESSIONID") String sessionId,
                                @RequestHeader("Accept-Language") String accpetLanguage) {
        ModelAndView mav = new ModelAndView();
        mav.setViewName("success");
        mav.addObject("user", new User());
        return mav;
    }

    // ③请求参数按名称匹配的方式绑定到user的属性中、方法返回对应的字符串代表逻辑视图名
    @RequestMapping(value = "/handle3")
    public String handle3(User user) {
        return "success";
    }

    // ④直接将HTTP请求对象传递给处理方法、方法返回对应的字符串代表逻辑视图名
    @RequestMapping(value = "/handle4")
    public String handle4(HttpServletRequest request) {
        return "success";
    }

    @RequestMapping(value = "/handle11")
    public String handle11(
            @RequestParam(value = "userName", required = false) String userName,
            @RequestParam("age") int age) {
        return "success";
    }

    @RequestMapping(value = "/handle12")
    public String handle12(
            @CookieValue(value = "sessionId", required = false) String sessionId,
            @RequestParam("age") int age) {
        return "success";
    }

    @RequestMapping(value = "/handle13")
    public String handle13(@RequestHeader("Accept-Encoding") String encoding,
                           @RequestHeader("Keep-Alive") long keepAlive) {
        return "success";
    }

    @RequestMapping(value = "/handle14")
    public String handle14(User user) {
        return "success";
    }

    @RequestMapping(path = "/handle21")
    public void handle21(HttpServletRequest request, HttpServletResponse response) {
        String userName = WebUtils.findParameterValue(request, "userName");
        response.addCookie(new Cookie("userName", userName));
    }

    @RequestMapping(path = "/handle22")
    public ModelAndView handle22(HttpServletRequest request) {
        String userName = WebUtils.findParameterValue(request, "userName");
        ModelAndView mav = new ModelAndView();
        mav.setViewName("success");
        mav.addObject("userName", userName);
        return mav;
    }

    @RequestMapping(path = "/handle23")
    public String handle23(HttpSession session) {
        session.setAttribute("sessionId", 1234);
        return "success";
    }

    @RequestMapping(path = "/handle24")
    public String handle24(HttpServletRequest request, @RequestParam("userName") String userName) {
        return "success";
    }

    @RequestMapping(path = "/handle25")
    public String handle25(WebRequest request) {
        String userName = request.getParameter("userName");
        return "success";
    }

    @RequestMapping(path = "/handle31")
    public void handle31(OutputStream os) throws IOException {
        Resource res = new ClassPathResource("/image.jpg");
        FileCopyUtils.copy(res.getInputStream(), os);
    }

    @RequestMapping(path = "/handle41")
    public String handle4(@RequestBody String requestBody) {
        System.out.println(requestBody);
        return "success";
    }

    @ResponseBody
    @RequestMapping(path = "/handle42/{imageId")
    public byte[] handle42(@PathVariable("imageId") String imageId) throws IOException {
        System.out.println("load image of " + imageId);
        Resource res = new ClassPathResource("/image.");
        byte[] fileData = FileCopyUtils.copyToByteArray(res.getInputStream());
        return fileData;
    }

    @RequestMapping(path = "/handle43")
    public String handle43(HttpEntity<String> httpEntity) {
        long contentLen = httpEntity.getHeaders().getContentLength();
        System.out.println(httpEntity.getBody());
        return "success";
    }

    @RequestMapping(path = "/handle44/{imageeId}")
    public ResponseEntity<byte[]> handle44(@PathVariable("imageId") String imageId) throws Throwable {
        Resource res = new ClassPathResource("/image.jpg");
        byte[]  fileData = FileCopyUtils.copyToByteArray(res.getInputStream());
        ResponseEntity<byte[]> responseEntity = new ResponseEntity<byte[]>(fileData, HttpStatus.OK);
        return responseEntity;
    }

    @RequestMapping("/api")
    public Callable<User> api() {
        System.out.println("=====hello");
        return new Callable<User>() {
            @Override
            public User call() throws Exception {
                Thread.sleep(10L * 1000);
                User user = new User();
                user.setUserId("1L");
                user.setUserName("haha");
                return user;
            }
        };
    }

    @RequestMapping(path = "/handle61")
    public String handle61(@ModelAttribute("user") User user) {
        user.setUserId("1000");
        return "/user/createSuccess";
    }

    @ModelAttribute("user")
    public User getUser() {
        User user = new User();
        user.setUserId("1001");
        return user;
    }
    @RequestMapping(path = "/handle62")
    public String handle62(@ModelAttribute("user") User user) {
        user.setUserName("tom");
        return "/user/showUser";
    }

    @RequestMapping(path = "/handle63")
    public String handle63(ModelMap modelMap) {
        modelMap.addAttribute("testAttr", "value1");
        User user = (User) modelMap.get("user");
        user.setUserName("tom");
        return "/user/showUser";
    }

    @RequestMapping(path = "/handle71")
    public String handle71(@ModelAttribute("user") User user) {
        user.setUserName("John");
        return "redirect:/user/handle72.html";
    }

    @RequestMapping(path = "handle72")
    public String handle72(ModelMap modelMap, SessionStatus sessionStatus) {
        User user = (User) modelMap.get("user");
        if (user != null) {
            user.setUserName("Jetty");
            sessionStatus.setComplete();
        }
        return "/user/showUser";
    }

    @RequestMapping(path = "handle81")
    public String handle81(@RequestParam("user") User user, ModelMap modelMap) {
        modelMap.put("user", user);
        return "/user/showUser";
    }

    @InitBinder
    public void initBinder(WebDataBinder binder) {
        binder.addCustomFormatter(new DateFormatter("yyyy-MM-dd"));
    }

    @RequestMapping(path = "/handle91")
    public String handle91(@Valid @ModelAttribute("user") User user, BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            return "/user/register3";
        } else {
            return "/user/showUser";
        }
    }

    @RequestMapping(path = "/handle92")
    public String handle92(@ModelAttribute("user") User user, BindingResult bindingResult) {
        ValidationUtils.rejectIfEmptyOrWhitespace(bindingResult, "userName", "required");
        if ("aaaa".equalsIgnoreCase(user.getUserName())) {
            bindingResult.rejectValue("userName", "reserved");
        }
        if (bindingResult.hasErrors()) {
            return "/user/register4";
        } else {
            return "/user/showUser";
        }
    }

    @RequestMapping(path = "/showUserListByFtl")
    public String showUserListInFtl(ModelMap mm) {
        List<User> userList = new ArrayList<>();

        mm.addAttribute("userList", userList);
        return "userListFtl";
    }

    @RequestMapping(path = "/showUserListByXls")
    public String showUserListInExcel(ModelMap mm) {
        Calendar calendar = new GregorianCalendar();

        List<User> userList = new ArrayList<User>();
        User user1 = new User();
        user1.setUserName("tom");
        user1.setRealName("汤姆");
        calendar.set(1980, 1, 1);
        user1.setBirthday(calendar.getTime());
        User user2 = new User();
        user2.setUserName("john");
        user2.setRealName("约翰");
        user2.setBirthday(calendar.getTime());
        userList.add(user1);
        userList.add(user2);
        mm.addAttribute("userList", userList);
        return "userListExcel";
    }

    @RequestMapping(path = "/showUserListByPDF")
    public String showUserListInPdf(ModelMap mm) {
        Calendar calendar = new GregorianCalendar();

        List<User> userList = new ArrayList<>();
        User user1 = new User();
        user1.setUserName("tom");
        user1.setRealName("汤姆");
        calendar.set(1980, 1, 1);
        user1.setBirthday(calendar.getTime());
        User user2 = new User();
        user2.setUserName("john");
        user2.setRealName("约翰");
        user2.setBirthday(calendar.getTime());
        userList.add(user1);
        userList.add(user2);
        mm.addAttribute("userList", userList);
        return "userListPdf";
    }

    @RequestMapping(path = "/showUserListByXml")
    public String showUserListInXml(ModelMap mm) {
        Calendar calendar = new GregorianCalendar();

        List<User> userList = new ArrayList<>();
        User user1 = new User();
        user1.setUserName("tom");
        user1.setRealName("汤姆");
        calendar.set(1980, 1, 1);
        user1.setBirthday(calendar.getTime());
        User user2 = new User();
        user2.setUserName("john");
        user2.setRealName("约翰");
        user2.setBirthday(calendar.getTime());
        userList.add(user1);
        userList.add(user2);
        mm.addAttribute("userList", userList);
        return "userListXml";
    }

    @RequestMapping(path = "/showUserListByJson")
    public String showUserListInJson(ModelMap mm) {
        Calendar calendar = new GregorianCalendar();

        List<User> userList = new ArrayList<>();
        User user1 = new User();
        user1.setUserName("tom");
        user1.setRealName("汤姆");
        calendar.set(1980, 1, 1);
        user1.setBirthday(calendar.getTime());
        User user2 = new User();
        user2.setUserName("john");
        user2.setRealName("约翰");
        user2.setBirthday(calendar.getTime());
        userList.add(user1);
        userList.add(user2);
        mm.addAttribute("userList", userList);
        return "userListJson";
    }

    @RequestMapping(value = "/showUserListMix")
    public String showUserListMix(ModelMap mm) {
        Calendar calendar = new GregorianCalendar();

        List<User> userList = new ArrayList<>();
        User user1 = new User();
        user1.setUserName("tom");
        user1.setRealName("汤姆");
        calendar.set(1980, 1, 1);
        user1.setBirthday(calendar.getTime());
        User user2 = new User();
        user2.setUserName("john");
        user2.setRealName("约翰");
        user2.setBirthday(calendar.getTime());
        userList.add(user1);
        userList.add(user2);
        mm.addAttribute("userList", userList);
        return "userListMix";
    }

    @RequestMapping(path = "/uploadPage")
    public String updatePage() {
        return "uploadPage";
    }
    @RequestMapping(path = "/upload")
    public String updateThumb(@RequestParam("name") String name, @RequestParam("file") MultipartFile file) throws Exception {
        if (!file.isEmpty()) {
            file.transferTo(new File("e:/temp/" + file.getOriginalFilename()));
            return  "redirect:success.html";
        } else {
            return "redirect:fail.html";
        }
    }

    @RequestMapping(path = "/throwException")
    public String throwException() {
        if (2 > 1) {
            throw new RuntimeException("ddd");
        }
        return "success";
    }

    @ExceptionHandler(RuntimeException.class)
    public String handleException(RuntimeException re, HttpServletRequest request) {
        return "forward:/error.jsp";
    }

    public static void main(String[] args) {
        AsyncRestTemplate template = new AsyncRestTemplate();

        // 1 调用完后立即返回（没有阻塞）
        ListenableFuture<ResponseEntity<User>> future = template.getForEntity("http://localhost:8080/chapter17/api.html", User.class);

        // 2 处理服务器端响应的异步回调方法
        future.addCallback(new ListenableFutureCallback<ResponseEntity<User>>() {
            @Override
            public void onFailure(Throwable throwable) {
                System.out.println("=====client failure: " + throwable);
            }

            @Override
            public void onSuccess(ResponseEntity<User> userResponseEntity) {
                System.out.println("=====client get result: " + userResponseEntity.getBody());
            }
        });
        System.out.println("==no wait");
    }
}
