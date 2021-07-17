# Heading 0

## Heading 1

### Heading 2

#### Heading 3

---



# Font

---

**This is bold font**

*This is Italic font*

***This is bold & Italic font***

~~This is slash font~~



# Image

---

![My Picture](C:\Users\Pyrad\Desktop\tmps\1497625898188.jpg)



# Hyperlink

---

[My Link](www.google.com)



# List

---

### Unordered List

- row a
- row b
- row c

### Ordered List

1. row a 
2. row b
3. row c



# Table

---

| name  | sex  | age  |
| ----- | ---- | ---- |
| Pyrad | Male | 18   |







# Java内存

---

1. 线程内存区域
   1. 程序计数器
   2. Java虚拟机栈
   3. 本地方法栈
2. 堆
3. 方法区
4. 运行时常量池
5. 直接内存

- Java VM启动时会开启Garbage Collection的线程
  - 引用计数法
  - 引用可达法（根搜索算法）
- 年轻代
  - Eden区：（1个）尽可能收集生命周期短的对象（新生成的对象首先放这里），对应Minor GC，复制算法效率高，但浪费内存空间。
  - survivor区：（2个，分别是from和to）
- 年老代
  - Eden区经过N次GC之后仍然存活的，被放到这里。
  - 有一个tenured区
  - 当年老代越来越多的时候，启动Major GC和Full GC全面清理年轻代和年老代区

- 持久代
  - JDK8之后使用元数据和metaspace

- 在一个java class类的构造器（constructor）里可以调用重载的其他的构造器，但必须是位于函数体的第一句，且使用this

  ```java
  public class User {
      int id;
      String name;
      String pwd;
      
      public User(int id, String name) {
          this.id = id;
          this.name = name;
      }
      
      public User(int id, String name, String pwd) {
          this(id, name); // <- overloaded constructor
          this.pwd = pwd;
      }
  }
  ```

  

# 面向对象三大特征

- 继承
  - Java中类只有单继承，没有C++中的类多继承
  - 但是Java中有接口的多继承
- 封装
- 多态
- Java中使用extends来实现继承

# 运算符 instanceof 

instanceof是二元运算符

```java
System.out.println(s instanceof Person);
System.out.println(s instanceof Student);
```



# 类中方法的重写

Java中重写函数的返回值，可以是本类的object，也可以是直接父类的object，但不可以是间接父类的object（爷爷辈的class）



# 关键字final

- 修饰变量：一旦被赋值，不能再改变
- 修饰方法：方法不可被重写，但可以被重载
- 修饰类：修饰的类不能被继承



# equals和==

- ==

  就是比较两个object的地址是否相同

- equals

  Object类里面的method，默认就是比较两个object的地址，但是可以被重载，用来比较两个object的内容是否相同（或者其他用途）

# super

可以看做是子类对父类对象的引用，可以通过super来引用父类的方法和熟悉（成员）

一个类中，构造方法的第一行没有显示调用super(...)或this(...)，Java编译器会自动默认调用super()，即调用父类的无参数构造函数。



# 封装

|  修饰符   | 同一个类 | 同一个包中 | 子类 | 所有类 |
| :-------: | :------: | :--------: | :--: | :----: |
|  private  |    *     |            |      |        |
|  default  |    *     |     *      |      |        |
| protected |    *     |     *      |  *   |        |
|  public   |    *     |     *      |  *   |   *    |



父类和子类在同一个包中，子类***可以***访问父类的protected成员，也***可以***访问父类对象的protected成员

父类和子类不在同一个包中，子类***可以***访问父类的protected成员，但***不可以***访问父类对象的protected成员

