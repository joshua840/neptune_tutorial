for LAMB1 in 1 2 3 4 5
do
for LAMB2 in 3 10
do

python main.py --lambda1 $LAMB1 --lambda2 $LAMB2 &

done
done