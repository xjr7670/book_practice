class CheckExtend extends Class1 {
    Integer age = 18;
    public static void main(String[] args) {
        Class1 cls = new Class1();
        String a = cls.getString();
        System.out.println(a);
    }
    public static String getString() {
        return "age";
    }
}