class Dog {
    String name;
    public static void main(String[] args) {
        // 创建 Dog 对象
        Dog dog1 = new Dog();
        dog1.bark();
        dog1.name = "Bart";

        // 创建 Dog 数组
        Dog[] myDogs = new Dog[3];
        // 关门放狗
        myDogs[0] = new Dog();
        myDogs[1] = new Dog();
        myDogs[2] = dog1;

        // 通过数组引用存取 Dog
        myDogs[0].name = "Fred";
        myDogs[1].name = "Marge";

        System.out.print("last dog's name is ");
        System.out.println(myDogs[2].name);

        int x = 0;
        while (x < myDogs.length) {
            myDogs[x].bark();
            x = x + 1;
        }
    }
    public void bark() {
        System.out.println(name + "say Ruff!");
    }

    public void eat() {}
    public void chaseCat() {}
}

