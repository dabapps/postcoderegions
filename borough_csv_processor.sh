for file in *.csv
do
    cut -d, -f 1,9 "$file" >> ~/Desktop/boroughs3.csv
done
