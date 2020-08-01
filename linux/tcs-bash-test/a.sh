awk 'BEGIN{FS=";"}
    NR>1{id[$2]=$1; name[$2]=$2; salary[$2]=$3;n++}
    END{
        totalsal=0;
        for(j in salary){totalsal+=salary[j];}
        avg=totalsal/n;
        for(j in salary){
            if(salary[j]<avg){count++;}
        }
        print count;
        }' $1
