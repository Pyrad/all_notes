# Golang Learnning

## The notes for [A Tour of Go](https://go.dev/tour/welcome/1)

1. Understanding slices

   See this blog which tells some details [Go Slices: usage and internals]([https://go.dev/blog/slices-intro) 

   > A slice cannot be grown beyond its capacity. Attempting to do so will cause a runtime panic, just as when indexing outside the bounds of a slice or array. Similarly, slices cannot be re-sliced below zero to access earlier elements in the array.
   
2. What is a closure

   > A closure is a function that references variable from outside its body

   
