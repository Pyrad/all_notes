# A Tour of Go (Notes)

Notes for A Tour of Go ([link is here](https://go.dev/tour/welcome/1))

## 章节信息（欢迎使用Go[指南](https://tour.go-zh.org/list)）

### 前言

- [Chapter 1 Welcome](https://tour.go-zh.org/welcome)

  学习使用本指南：包括如何在不同的课程间切换以及运行代码。

### 基础

- [Chapter 2 Packages, variables and functions](https://go.dev/tour/basics/1)

  Go 程序的基本结构。

- [Chapter 3 Flow control statements: for、if、else、switch and defer](https://tour.go-zh.org/flowcontrol)

  学习如何使用条件、循环、分支和推迟语句来控制代码的流程。

- [Chapter 4 More types: struct、slice and maps](https://tour.go-zh.org/moretypes)

  学习如何基于现有类型定义新的类型：本节课涵盖了结构体、数组、切片和映射。

### 方法和接口

学习如何为类型定义方法；如何定义接口；以及如何将所有内容贯通起来。

- [Chapter 5 Methods and interfaces](https://tour.go-zh.org/methods)

  本节课包含了方法和接口，可以用这种构造来定义对象及其行为。

### Generics

- [Chapter 6 Generics](https://go.dev/tour/generics/1)

### 并发

作为语言的核心部分，Go 提供了并发的特性。

这一部分概览了 goroutine 和 channel，以及如何使用它们来实现不同的并发模式。

- [Chapter 7 并发](https://tour.go-zh.org/concurrency)

Go 将并发结构作为核心语言的一部分提供。本节课程通过一些示例介绍并展示了它们的用法。



## Chapter 1 Welcome

### 本地网页版本的tour安装

离线版本使用如下命令安装

```powershell
go install golang.org/x/website/tour@latest
```

它会在`$GOPATH`这个环境变量所代表的目录中生成一个名为`tour`的binary，启动它即可打开本地网页版本的tour guide。



## Chapter 2 Packages, variables and functions

### 包 （Packages）

- Go程序都是由包（packages）组成的，通过关键字`import`导入包

- 包名按照惯例是导入路径（import path）的最后一个元素，比如`import math/rand`导入了`math/rand`这个包，那么这个包中的源代码就是以`package rand`语句开始的

- 程序入口是`main`这个包

- 多个包可以使用分组（factored）形式的导入语句，也可以简单地使用多个`import`语句导入

  ```go
  // 分组导入
  import (
      "fmt"
      "math"
  )
  
  // 常规导入
  import "fmt"
  import "math"
  ```

  

- 导入一个包时，只能使用其中已经导出的名字（变量/函数），而所谓导出，指包中变量/函数名如果是大写字母开头，那么它是导出的，否则就不是导出的。

### 函数

- 以关键字`func`开头，然后跟上函数名，再跟上函数列表（用圆括号括起来）

- 返回值的类型在参数列表的后面

- 可有或无参数，注意go特殊的是参数类型在参数名称的后面

- 参数列表中，如果有两个或以上的参数类型相同时，可以只写最后一个形参的类型，前面其他的可省略

- 可以返回任意数量的返回值，同样的，参数类型列表也必须是同样的数目（并且用括号括起来）

- 返回值可以被命名，并和返回类型放在一起，这样`return`语句就可以省略后面的参数

  ```go
  // 函数
  func add(x int, y int) int {
      return x + y
  }
  
  // 省略连续相同类型形参的类型关键字
  func add(x, y int) int {
  	return x + y
  }
  
  // 返回两个返回值
  func swap(x, y string) (string, string) {
  	return y, x
  }
  
  // 命名返回值（return 省略后面的参数)
  func split(sum int) (x, y int) {
  	x = sum * 4 / 9
  	y = sum - x
  	return
  }
  ```




### 变量

- `var`用来声明一个变量或者一个变量列表，同样的，类型放在最后面

- 变量声明可以包含初始值，每个变量对应一个

- `:=`符号可以用在函数中（函数外面不可以），用来代替`var`声明，叫做简洁赋值语句（既赋值又声明）

- 基本类型

  - `bool`
  - `string`
  - `int int8 int16 in32 int64 uint unit8 uint16 uint32 uint64 uintptr`
  - `byte`（`uint8`的别称）
  - `rune`（`int32`的别称）
  - `float32 float64`
  - `complex64 complex128`
  - 像导入语句，基本类型也可以“分组”成一个语法块

- 没有明确初始值的变量声明会被赋予它们各自类型的**零值**

  - 数值类型的零值：0
  - 布尔类型为 `false`
  - 字符串为 `""`（空字符串）

- 类型转换

  - 表达式用`T(v)`把值`v`转换为类型`T`
  - 可以使用简洁形式`k := T(v)`，该表达式把`v`这个变量转换为类型`T`
  - go中的类型转换必须是显示的转换

- 变量的类型可以由右值推导出来

  - 如果右值是数值常量（即没有指定类型），你们新变量的类型就取决于常量的精度

- 常量

  - 声明和变量类似，但使用`const`关键字，当然可以声明在包里或函数里
  - 常量可以是：字符、字符串、布尔值或数值
  - 常量不能使用简洁赋值语句`:=`
  - 数值常量是高精度的**值**

- 

  ```go
  // 变量（列表）声明，实际上被赋予了各自的零值）
  var c, python, java bool
  
  // 变量声明对应初始值
  var i, j int = 1, 2
  
  // 简洁赋值
  k := 3
  c, python, java := true, false, "no!"
  
  // 分组的变量声明
  var (
     	ToBe   bool       = false
  	MaxInt uint64     = 1<<64 - 1
  	z      complex128 = cmplx.Sqrt(-5 + 12i)
  )
  
  // 类型转换
  var i int = 42
  var f float64 = float64(i)
  var u uint = uint(f)
  // 类型转换的简洁形式
  i := 42
  f := float64(i)
  u := uint(f)
  
  // 类型推导
  var i int
  j := i // j 也是一个 int
  // 根据数值常量的精度推导类型
  i := 42           // int
  f := 3.142        // float64
  g := 0.867 + 0.5i // complex128
  
  // 常量
  const World = "myWorld"
  const Truth = true
  ```




> Start 2022-May-9 20:41:35 Raycom 7F
>
> End 2022-May-9 21:46:28 Raycom 7F



## Chapter 3 Flow control statements: for, if, else, switch and defer

### for

- Go只有`for`这一种循环

- `for`循环由三部分组成，用分号隔开，但这三个部分不用小括号括起来

  - 初始化语句（类似C/C++中，可以省略）
  - 条件表达式
  - 后置语句（类似C/C++中，可以省略）

- 当`for`循环省略了初始化语句和后置语句，这时候就可以去掉分号，相当于Go中的`while`循环

- xxx

  ```go
  // 基本的for循环
  sum := 0
  for i := 0; i < 10; i++ {
  	sum += i
  }
  
  // 省略初始化语句和后置语句的for循环
  sum := 1
  for ; sum < 1000; {
  	sum += sum
  }
  
  // 省略初始化语句和后置语句的for循环，可以去掉分号
  sum := 1
  for sum < 1000 {
  	sum += sum
  }
  
  // 无限循环（死循环）
  for {
  }
  ```



> Started 2022-May-10 23:25
>
> End 2022-May-10 23:29



### if

- 和`for`循环类似，`if`后面的表达式不用小括号，但是更后面的执行语句块必须用大括号

- `if`语句可以在条件表达式前加一个简单语句（和表达式语句用分号`;`隔开），里面声明的变量仅在`if`语句块内有效

  ```go
  // 基本的if语句
  if x < 0 {
  	return sqrt(-x) + "i"
  } else {
      return x
  }
  
  // if表达式前面的简单语句，
  if v := math.Pow(x, n); v < lim {
  	return v
  }
  ```



### switch

- `switch`语句无需再每个case语句后面加上`break`，因为Go会自动提供`break`，以便自动结束分支执行

- `switch`的后面的变量同样不用小括号

- `switch`的后面的变量前面可以加入一个简单的语句，作用域仅限于该`switch`语句

- `switch`语句的case不仅限于常量或整数，其他类型也可以

- `switch`后面也可以不加条件，此时等价于`switch true`

  ```go
  // 基本的switch语句（例子1）
  switch os := runtime.GOOS; os {
  	case "darwin":
  		fmt.Println("OS X.")
  	case "linux":
  		fmt.Println("Linux.")
  	default:
  		// freebsd, openbsd,
  		// plan9, windows...
  		fmt.Printf("%s.\n", os)
  }
  
  // 基本的switch语句（例子2）
  today := time.Now().Weekday()
  	switch time.Saturday {
  	case today + 0:
  		fmt.Println("Today.")
  	case today + 1:
  		fmt.Println("Tomorrow.")
  	case today + 2:
  		fmt.Println("In two days.")
  	default:
  		fmt.Println("Too far away.")
  }
  ```

  

### defer

- `defer`后面**必须**跟的是函数，不能是简单的语句

- `defer`后面的函数会在`defer`所在的函数返回之后再执行，但是其参数会立即求值

- `defer`的函数会被依次压入堆栈，当外层函数返回后，`defere`的函数会按**后进先出**的顺序调用

  ```go
  // 最后打印出来的顺序是Hello, world!
  func print() {
      defer fmt.Println("world!)
      fmt.Println("Hello, ")
  }
  
  // defer的函数按照后进先出的顺序，在外层函数返回后被依次调用
  // 下面的打印结果是（->表示另起一行）:
  // counting->done->9->8->7->6->5->4->3->2->1->0
  
  func print() {
      fmt.Println("counting")
  	for i := 0; i < 10; i++ {
  		defer fmt.Println(i)
  	}
  	fmt.Println("done")
  }
  ```

  

## Chapter 4 More types: structs, slices, and maps

### Pointers

- Go是有指针的，和C一样，它保存值的内存地址

- `*T`是指向`T`类型值的指针，对应的零值是nil

- `&`操作符生成一个指向其操作数的指针

- `*`操作符表示指针的底层值（解引用）

- 和C不同，Go**没有指针的运算**

  ```go
  // 声明一个指针
  var p *int
  
  // &操作符
  i := 42
  p = &i
  
  // *操作符（解引用）
  fmt.Println(*p) // 读取p指针所对应的值
  *p = 21         // 通过p指针设置指向的值
  ```



### Struct

- 一个结构体就是一组字段（A `struct` is a collection of fields）

- 定义结构体，以关键字`type`开头，跟上结构体名字，再跟上关键字`struct`，后面是大括号括起来的一组字段（field）

- 结构体中的字段用点号`.`访问

- 如果有一个结构体指针（比如p指向一个结构体对象），那么字段也通过点号访问，

  - (*p).X ：完全的写法
  - p.X：简洁的写法（语言允许使用隐式间接引用）

- 分配结构体时，通过直接列出字段的值来分配一个结构体

  - `var v Vertext{1, 2}`
  - `v := Vertex{1, 2}`
  
- 可以只列出一部分字段的值，另一部分字段用字段名代替，表示使用其类型对应的零值
  -   `v := Vertex{X, 1}`  X字段的值默认为0(结构体定义见如下)
  -   `v := Vertex{}` X和Y的值默认为0(结构体定义见如下)
  
- 可以通过`&`前缀来直接返回一个结构体指针

  - `p := &Vertex{3, 4}`
  
  ```go
  // 结构体定义
  type Vertex struct {
  	X int
  	Y int
  }
  // 也可以如下，把相同类型的字段写到一起
  type Vertex struct {
  	X, Y int
  }
  
  // 定义结构体的文法
  var v Vertex{1, 2}
  // 或者
  v := Vertex{1, 2}
  
  // 定义结构体的对象，并用点号访问
  v := Vertex{1, 2}
  v.X = 4
  fmt.Println(v.X)
  
  // 结构体指针访问字段
  p := &v
  p.X = 1e9
  
  // 
  v1 = Vertex{1, 2}  // 创建一个 Vertex 类型的结构体
  v2 = Vertex{X: 1}  // Y:0 被隐式地赋予
  v3 = Vertex{}      // X:0 Y:0
  p  = &Vertex{1, 2} // 创建一个 *Vertex 类型的结构体（指针）
  ```
  



### Array

- 类型`[n]T`表示一个有n个T类型值的数组

  - `var a [10]int`

- 和C中一样，数组声明了之后，其长度不能改变

- 可以用花括号列出数组的初始值

  - `primes := [6]int{2, 3, 5, 7, 11, 13}`

- xx

- xx

- xx

  ```go
  // 数组定义
  var a [2]string
  a[0] = "Hello"
  a[1] = "World"
  
  // 数组定义2
  primes := [6]int{2, 3, 5, 7, 11, 13}
  ```

  











