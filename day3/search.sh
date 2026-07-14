search_word(){
	file=$1
	word=$2

	if grep -qi "$word" "$file"
	then
		echo "$word is found in $file"
	else
		echo "$word is not found"
	fi
}
echo "Enter a word: "
read w
search_word file1.txt $w

count_word(){
	file=$1
	word=$2

	count=$(grep -o "$word" "$file" | wc -l)

	echo "Occurance if $word:$count"

}
count_word file1.txt Linux

show_line(){
	file=$1
	word=$2

	grep -n "$word" "$file"
}
show_line file1.txt Linux
