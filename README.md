# Turing
A quick turing machine parser for Penrose's The Emperor's New Mind


In "The Emperor's New Mind" Sir Roger Penrose describes a kind of universal Turing Machine which accepts as its input descriptions of other turing machines, enocded in binary - this program seeks to emulate such a machine
#Mahmoud Ghanem - Summer 2014


Penrose describes a kind of binary notation which sandwiches unary numbers inbetween 0s
	He then interperets unary numbers other than 1s and 0s as punctuation using the following rules

	2 = L
	3 = R
	4 = S

To economise on space, he drops 0s off both ends of the binary input string and in the middle of it, where zeros would otherwise be expected...


This is a quick python program which implements the version of the Universal Turing Machine he describes, and which can run some of the basic programs he lists in his book.


## Example usage

As demonstrated in the python file:

```python
unaryEuclid = loadLogicFromPenrose("00->00R,01->11R,10->01S,11->11R") 
logic_table = unaryEuclid

```
