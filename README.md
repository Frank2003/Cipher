# Cipher

It contains various useful tools.

## Available functions:

	Add:			s s :b
	Bin:			s :b
	Hash:			s :s
	Help:			None
	Hex:			s :b
	Subtract:		s s :b
	atbash:			s :b
	base:			s i
	caeser:			s i :b
	decrypt:		s :s :b
	dmorse:			s :s
	encrypt:		s :s :b
	f:(file input)		s
	interpretbf:		s :s
	morse:			s :s
	o:(file output)		s :b
	r:			s
	randint:		i i
	rands:			s :s :b
	raw_atbash:		s
	shift:			s i
	subs:			s s :b :b
	switch_base:		s i :i
	vigenere:		s s :b
	chr:			i
	ord:			s
	eval:			s
	len:			s
	-				(skip an UNECESSARY argument)
	/				(end function)

#### Note:
    s means string
    b means boolean(-/+)
    i means integer or expression
    : means UNECESSARY argument    
### Example:

    $ cipher -o out.txt / -m -f exam.ple

It is equivelent to

    o('out.txt');morse(f('exam.ple'))

It turns file exam.ple to morse code and outputs to out.txt.
