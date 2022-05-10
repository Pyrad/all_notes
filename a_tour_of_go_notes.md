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

### if

- xxx
- xxx
- 











> Started 2022-May-10 23:25
>
> End 2022-May-10 23:29
