for file in *.csv
do
    cut -d, -f 1,9 "$file" >> ./boroughs.csv
done
