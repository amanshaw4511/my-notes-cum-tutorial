

-F fs
-f file
-v var=value


## variables
    + $0    whole line
    + $1    first field
    + $2    second filed
    + $n    (n)th field


## syntax
    awk 'BEGIN {

        }
        regexp {

        }
        END {

        }' file

## buildin variables
    
    + FS    file separator
    + RS    record separator
    + OFS   output file separator
    + NF    no of fields
    + NR    no of records processed
    + FNR   no of record processed in a file
    + IGNORECASE    ignore case
    
    + ARGC  no of passed parameters
    + ARGV  retrieve command line parameters
    + ENVIRON array of shell variables
    + FILENAME name of file processing


