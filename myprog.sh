#!/bin/bash
mkdir temp
echo "...create temp directory..."

cp num1.txt temp
cp num2.txt temp
cp cal.sh temp

echo "...copy files to temp directory..."
echo "1) add"
echo "2) sub"
echo "3) div"
echo "4) mul"
read -p "select menu : " num

if [ "$num" -eq 1 ]; then
    parameter="add"
elif [ "$num" -eq 2 ]; then
    parameter="sub"
elif [ "$num" -eq 3 ]; then
    parameter="div"
elif [ "$num" -eq 4 ]; then
    parameter="mul"
fi
echo "...$parameter selected..."
echo "...run calculator..."

chmod +x cal.sh
./cal.sh $num
