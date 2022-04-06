#!/bin/bash

echo "project management in github"

while read num1; do 
    continue
done < num1.txt
while read num2; do 
    continue
done < num2.txt

declare -a arr=("$num1" "$num2")

if [ $# -le 0 ]; then
    echo "....none operator parameter...."
    echo "1)add"
    echo "2)sub"
    echo "3)div"
    echo "4)mul"
    read -p "select menu : " temp

    if [ "$temp" -eq 1 ]; then
        parameter=add
        anwser=$(("${arr[0]}" + "${arr[1]}"))
    elif [ "$temp" -eq 2 ]; then
        parameter=sub
        anwser=$(("${arr[0]}" - "${arr[1]}"))
    elif [ "$temp" -eq 3 ]; then
        parameter=div
        anwser=$(("${arr[0]}" / "${arr[1]}"))
    elif [ "$temp" -eq 4 ]; then
        parameter=mul
        anwser=$(("${arr[0]}" * "${arr[1]}"))
    fi
    echo "num1 : $num1"
    echo "num2 : $num2"
    echo "op : $parameter"
    echo "result : $anwser"
else
    if [ "$1" -eq 1 ]; then
        parameter=add
        anwser=$(("${arr[0]}" + "${arr[1]}"))
elif [ "$1" -eq 2 ]; then
        parameter=sub
        anwser=$(("${arr[0]}" - "${arr[1]}"))
elif [ "$1" -eq 3 ]; then
        parameter=div
        anwser=$(("${arr[0]}" / "${arr[1]}"))
elif [ "$1" -eq 4 ]; then
        parameter=mul
        anwser=$(("${arr[0]}" * "${arr[1]}"))
fi
    echo "num1 : $num1"
    echo "num2 : $num2"
    echo "op : $parameter"
    echo "result : $anwser"
fi

exit
