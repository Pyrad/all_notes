# Java容器



## ArrayList类

- 本质是动态数组，底层用数组实现（底层以**1.5**倍上次数组大小的方式扩容）

- 线程不安全；多线程中可以用Vector或CopyOnWriteArrayList

- 有几个两个重要对象

  - **elementData**：是一个Object[]，即object的数组
  - **size**：动态数组的实际大小
  - **DEFAULTCAPACITY_EMPTY_ELEMENTDATA**（一个final的空数组，默认构造时会赋值给elementData，JDK1.8之后的特点，**延迟加载**）

- 继承自AbstractList，并实现了以下几个接口

  - List：提供基本的增删改和遍历
  - RandomAccess：支持随机访问
  - Cloneable：可被克隆
  - java.io.Serializable：即可以支持序列化

  ```java
  public class ArrayList<E> extends AbstractList<E>
          implements List<E>, RandomAccess, Cloneable, java.io.Serializable {}
  ```

- 包含的方法

  ```java
  // Collection中定义的API
  boolean             add(E object)
  boolean             addAll(Collection<? extends E> collection)
  void                clear()
  boolean             contains(Object object)
  boolean             containsAll(Collection<?> collection)
  boolean             equals(Object object)
  int                 hashCode()
  boolean             isEmpty()
  Iterator<E>         iterator()
  boolean             remove(Object object)
  boolean             removeAll(Collection<?> collection)
  boolean             retainAll(Collection<?> collection)
  int                 size()
  <T> T[]             toArray(T[] array)
  Object[]            toArray()
  // AbstractCollection中定义的API
  void                add(int location, E object)
  boolean             addAll(int location, Collection<? extends E> collection)
  E                   get(int location)
  int                 indexOf(Object object)
  int                 lastIndexOf(Object object)
  ListIterator<E>     listIterator(int location)
  ListIterator<E>     listIterator()
  E                   remove(int location)
  E                   set(int location, E object)
  List<E>             subList(int start, int end)
  // ArrayList新增的API
  Object              clone()
  void                ensureCapacity(int minimumCapacity)
  void                trimToSize()
  void                removeRange(int fromIndex, int toIndex)
  ```

- 三种遍历方式

  ```java
  List<String> a = new ArrayList<>(20); //可以用父类的引用（指针）
  a.add("good"); a.add("day"); a.add("today");
  
  // 迭代器遍历
  Iterator itr = b.iterator(); // itr开始没有指向任何值
  while (itr.hasNext()) {
      String cur = (String) itr.next();
      System.out.println(cur);
  }
  System.out.println("----");
  
  // 索引遍历（随机访问）
  for (int i = 0; i < b.size(); i++) {
      System.out.println(b.get(i));
  }
  System.out.println("----");
  
  // 增强for循环遍历
  b.remove(b.iterator().next());
  for (String s : b) {
      System.out.println(s);
  }
  ```



## Vector类

Vector实现了List的接口，底层也是用数组实现的，相关的方法都有**同步检查**，所以是线程安全的。

Vector和ArrayList的使用基本上是一样的（方法基本都相同）

Vector扩容的倍数是以原先容量的**2倍扩容**

Vector采用的**默认初始化方式**是**立即初始化**，即最开始给elementData数组初始化为capacity是10（即容量为10）的数组。



## Stack类

Stack是**Vector**类的一个**子类**，即继承于Vector，特点是LIFO（Last In First Out）

扩展了Vector的5个方法

```java
boolean empty() // 查看栈是否空
E       peak() // 查看栈顶
E       pop() // 出栈
E       push(E item) // 入栈
int     search(Object o) // 返回元素在栈中的位置
```



```java
// 一个stack检查括号匹配的小程序
public static boolean symmetry() {
    String symbol = "...{..[..(...).....]..}...";
    Stack<String> stk = new Stack<>();
    for (int i = 0; i < symbol.length(); i++) {
        char c = symbol.charAt(i);
        if (c == '{') { stk.push("}"); }
        if (c == '[') { stk.push("]"); }
        if (c == '(') { stk.push(")"); }
        if (c == '}' || c == ']' || c == ')') {
            if (stk.empty()) {
                return false;
            }
            if (stk.peek().charAt(0) != c) {
                return false;
            }
            stk.pop();
        }
    }

    return stk.empty();
}
```



## LinkedList

- 也是实现了**List**的接口

- 底层用**双向链表**实现存储，查询效率低，增删效率高，线程不安全

- 继承（实现）关系

  ```java
  public class LinkedList<E>
      extends AbstractSequentialList<E>
      implements List<E>, Deque<E>, Cloneable, java.io.Serializable {}
  ```

  

- 重要的成员变量

  ```java
  transient int size;
  transient Node<E> first; // 指向链表的第一个元素
  transient Node<E> last; // 指向链表的最后一个元素
  ```

  

- 节点表示，是**LinkedList**的一个内部类

  ```java
  class Node<E> {
      E item;
      Node<E> next;
      Node<E> prev;
  }
  ```

- LinkedList除了Collection中的方法，还有自己的如下方法

  ```java
  void addFirst(E e); //元素添加到链表开头
  void addLast(E e); // 元素添加到链表尾
  getFirst(); // 返回链表第一个元素
  getLast(); // 返回链表最后一个元素
  removeFirst(); // 移除第一个元素，并返回该元素
  removeLast(); // 移除最后一个元素，并返回该元素
  E pop(); // 等效于removeFirst，移除头部元素（第一个）
  void push(E e); //等效于addFirst，在头部添加元素（第一个）
  boolean isEmpty();
  ```

  

## Set接口

- Set在是个**接口**，继承自Collection接口，但其方法和Collection的完全一致，并没有新增方法。
- 无序，不可重复，类似于C++中的std::set、std::unordered_set
- 常见的Set
  - HashSet
  - TreeSet



## HashSet

- 就是一个没有重复元素的集合

- 底层是**HashMap**实现的（简化版的HashMap）

- **HashMap**底层是用<font color='red'>**数组**</font>（默认初始长度16）和<font color='red'>**链表**</font>实现的，对元素的哈希值（**```hashCode```**方法）进行运算，然后决定元素在数组中的位置，同时也会通过元素的**```equals()```**方法来判断两个元素是否相同，如果相同则不会添加重复的元素（<font color='red'>**注意**</font>：是在元素的哈希值运算之后的值相同的时候，才会调用**```equals()```**方法，否则不会调用**```equals()```**方法）

- 如果经过对元素的hash值进行计算得到值相同，并且调用**```equals()```**方法也返回true，那么就会在该元素的位置（实际上是一个链表的节点）上生成一个链表（单向链表）把元素放到链表的下一个位置上，这就是前面提到的“底层是用<font color='red'>**数组**</font>（默认初始长度16）和<font color='red'>**链表**</font>实现的”

- 成员变量

  ```java
  private transient HashMap<E, Object> map;
  // Dummy value to associate with an Object in the backing Map
  // 即把key-value对里面的value固定给一个无意义的值，那么map就变成了set
  private static final Object PRESETN = new Object();
  ```

  

- HashSet中允许有null元素

- 利用Hash算法（散列算法）

- 因为是无序的，所以不能通过index索引来访问（其实和C++中的一模一样）

- 常见操作

  ```java
  public static void test() {
      Set<String> sset = new HashSet<>();
      sset.add("k"); sset.add("o"); sset.add("m"); sset.add("z");
      for (String s : sset) {
          System.out.println(s);
      }
  
      System.out.println(sset.contains("o") ? "Value exist" : "Value not found");
      System.out.println(sset.remove("z"));
      System.out.println(sset.remove("p"));
      
      Set<Users> uset = new HashSet<>();
  	Users u = new Users("Pyrad", 18);
  	Users v = new Users("Pyrad", 18);
  	// 只有一个元素在uset中，因为Users类里面重写了hashCode和equals方法
      for (Users cu : uset) {
           System.out.println(cu);
      }
  }
  
  // 可以通过重写自定义类的hashCode和equals方法来使用Set，以便达到想要的效果
  class Users {
      private String username;
      private int userage;
  
      public Users(String username, int userage) { this.username = username; this.userage = userage;}
      public Users() {}
      public String getUsername() { return username;}
      public void setUsername(String username) { this.username = username; }
      public int getUserage() { return userage; }
      public void setUserage(int userage) { this.userage = userage; }
  
      @Override
      public String toString() {
          return "Users{" +
                  "username='" + username + '\'' +
                  ", userage=" + userage +
                  '}';
      }
  
      @Override
      public boolean equals(Object o) {
          if (this == o) return true;
          if (o == null || getClass() != o.getClass()) return false;
          Users users = (Users) o;
          return userage == users.userage && Objects.equals(username, users.username);
      }
  
      @Override
      public int hashCode() {
          return Objects.hash(username, userage);
      }
      
      // 如果要用于TreeMap或TreeSet
      // (1) 就要在元素对应的类中实现接口Comparable<E>，并且重写compareTo
      // (2) 或者在外部使用比较器
      @Override
      public int compareTo(Users o) {
          if (this.getUsername().compareTo(o.getUsername()) == 0) {
              return 1;
          }
          if (this.getUserage() > o.getUserage()) {
              return 1;
          }
          return -1;
      }
  }
  ```

## TreeSet容器

- 可以对元素进行排序

- 底层是TreeMap实现的，通过key来存储元素（TreeSet里面显然只使用到了key）

- TreeMap是用红黑树实现的

- 继承关系

  ```java
  public class TreeSet<E> extends AbstractSet<E>
      implements NavigableSet<E>, Cloneable, java.io.Serializable
  // NavigableSet -> NvaigableMap -> SortedMap
  ```

- 成员变量

  ```java
  private transient NavigableMap<E, Object> m;
  private static final Object PRESENT = new Object();
  ```

- 需要给的排序规则

  - 通过元素自身实现比较规则（需要实现元素（就是类自己）Comparable接口中的compareTo方法）```Users```中的compareTo方法见如上

  - 通过比较器定义比较规则

    ```java
    import java.util.Comparator;
    // 如果Users类中没有compareTo方法，可以通过定义一个比较器类，传入其构造函数来实现
    public class UserComparator implements Comparator<Users> {
        @Override
        public int compare(Users o1, Users o2) {
            return o1.compareTo(o2);
        }
    }
    
    public static void test() {
            Set<Users> uset2 = new TreeSet<>(new UserComparator());
            uset2.add(u1); uset2.add(u2);
            for (Users s : uset2) {
                System.out.println(s);
            }     
    }
    ```

- 常用方法

  ```java
  public static void test() {
      Set<String> tset = new TreeSet<>();
      tset.add("d"); tset.add("c"); tset.add("a"); tset.add("c"); tset.add("b");
      // 因为内部是红黑树，对加入的元素会排序，所以输出a,b,c和d
      for (String s : tset) {
          System.out.println(s);
      }
  }
  ```

  

## Map接口

- Map是一个接口

- Map接口定义双例集合，它**不是**Collection的子接口

- 和C++中的std::map, std::unordered_map非常相似，比较理解即可

- 常用

  - TreeMap
  - HashMap

- Map接口中的常用方法

  ```java
  V put(K key, V value);               // 添加键值对，如果key已存在，会覆盖原有的key-value对，然后返回value；如果可以不存在，就返回null
  void putAll(Map m);                  // 复制另一个Map到此Map（并运算）
  V remove(Object key);                // 删除key对应的key-value对
  V get(Object key);                   // 得到key对应的value
  boolean containsKey(Object key);     // 是否有key
  boolean containsValue(Object value); // 是否有value
  Set keySet();                        // 取得所有key，并存储到Set中
  Set<Map.Entry<K,V>> entrySet();      // 返回一个Set，其Set的key是k-v对，在Map中以Map的内部类表示：Map.Entry<K,V>
  void clear();                        // 清空
  ```

## HashMap

- 是Map接口的实现类

- 底层采样哈希表存储数据，key重复的话，后面添加的会覆盖之前已经存在的key-value对

- 遍历方法

  ```java
  Map<String, String> m = new HashMap<>();
  String v = m.put("a", "A"); v = m.put("b", "BBS"); v = m.put("c", "CCS");v = m.put("d", "DDS");
  Set<String> allkeys = m.keySet();
  for (String s : allkeys) {
      String cv = m.get(s);
      System.out.println(cv);
  }
  
  Set<Map.Entry<String, String>> kvs = m.entrySet();
  for (Map.Entry<String, String> kv : kvs) {
      System.out.println(kv.getKey() + ": " + kv.getValue());
  }
  ```

  
