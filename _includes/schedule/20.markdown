	<td markdown="block">
Second Midterm

* [Sample Exam Questions](resources/handouts/midterm_2/midterm_2_practice.pdf)
* [Sample Exam Solutions](resources/handouts/midterm_2/midterm_2_practice_solutions.pdf)

Class Notes from Review

* [Stacks](activities/stacks.html)
* [Bubble Sort, Selection Sort, Sorting Objects](activities/sort.html)
* [String and StringBuilder Example](http://www.pythontutor.com/visualize.html#code=public+class+Foo+%7B%0A++++//+PLEASE+READ+THROUGH+SECTION+10.10+on+the+String+Class!%0A++++public+static+void+main(String%5B%5D+args)+%7B%0A++++++++//+STRINGS+ARE+IMMUTABLE%0A++++++++%0A++++++++//+note+that+s+and+t+point+to+the+same+hello!+this+is%0A++++++++//+interning%0A++++++++String+s+%3D+%22hello%22%3B%0A++++++++String+t+%3D+%22hello%22%3B%0A++++++++%0A++++++++//+but+usuing+the+constructor,+I+get+an+entirely+different%0A++++++++//+object!%0A++++++++String+u+%3D+new+String(%22hello%22)%3B%0A++++++++%0A++++++++//+if+I+assign+and+increment,+I+get+a+new+object+as+well%0A++++++++//+(the+original+is+not+modified,+strings+are+immutable)%0A++++++++s+%3D+s+%2B+%22+there%22%3B%0A++++++++%0A++++++++//+compareTo+returns+an+integer+based+on+lexicographic%0A++++++++//+ordering+of+the+first+differing+characters+between+%0A++++++++//+two+strings%3A%0A++++++++//+%22hello%22.compareTo(%22heart%22)+-%3E+positive+int%0A++++++++//+%22heart%22.compareTo(%22hello%22)+-%3E+negative+int%0A++++++++int+result+%3D+s.compareTo(%22heart%22)%3B%0A++++++++System.out.println(result)%3B%0A++++++++%0A++++++++//+split+breaks+up+a+string+into+an+Array+based+on%0A++++++++//+the+string+delimiter+passed+in%3A%0A++++++++String%5B%5D+parts+%3D+%22foo,bar,baz%22.split(%22,%22)%3B%0A++++++++System.out.println(parts%5B0%5D)%3B%0A++++++++%0A++++++++//+STRING+BUILDERS+*ARE*+MUTABLE%0A++++++++//+(they're+better+than+concatenation,+because+adding%0A++++++++//+continually+creates+new+String+objects!)%0A++++++++StringBuilder+sb+%3D+new+StringBuilder(%22The+variable,+parts,+contains+%22)%3B%0A++++++++sb.append(parts%5B0%5D)%3B%0A++++++++sb.append(%22+and+%22)%3B%0A++++++++sb.append(parts%5B1%5D)%3B%0A++++++++%0A++++++++//+see+the+output+window...%0A++++++++System.out.println(sb)%3B%0A++++%7D%0A%7D&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=java&rawInputLstJSON=%5B%5D&curInstr=0)
</td>
	<td markdown="block">
</td>
	<td markdown="block">
<!--
* [](assignments/.html)
-->
</td>
