## Args/kwargs
- They are mostly used in function definitions and allow you to pass a variable number of arguments to a function (variable - you do not know before hand how many arguments can be passed to your function by the user so in this case you use the two keywords)
- It's not necessary to write `*args` and `**kwargs`, only the `*` (aesteric) is necessary.

### Usage of `*args`
- `*args` is used to send a __non-keyworded__ variable length argument list to the function

### Usage of **kwargs
- `**kwargs` allows you to pass __keyworded__ variable length of arguments to a function
- You should use `**kwargs` if you want to handle __named arguments__ in a function

### Order of using `*args`, `**kwargs` and formal args
- If you want to use all three of these in functions then the order is;

	`some_func(fargs, *args, **kwargs)`
