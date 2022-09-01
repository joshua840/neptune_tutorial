for LAMB1 in 1 2
do
for LAMB2 in 2 3
do
for LAMB3 in 0.1 0.5
do

python main.py --lamb1 $LAMB1 --lamb2 $LAMB2 --lamb3 $LAMB3 &

done
done
done