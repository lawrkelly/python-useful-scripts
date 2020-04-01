#/usr/bin/bash

file=`ls`
#for f in $file
array=($file)
#do
	#printf $f
	#echo ${array[@]}
	#echo "NEW VALUE"
	#echo ${array [(1),(2),(3)}
	for g in ${array[@]}
	do
		#cp $g "tl_"$g
		cp $g ${g:(3):(60)}
		# cut -c3- $g > "tl_"$g	
	done
	#print $array
	#print $f(1)
#done
