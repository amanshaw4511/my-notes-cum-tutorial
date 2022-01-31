-- https://www.golinuxcloud.com/awk-examples-with-command-tutorial-unix-linux/
## Syntax
'/ search pattern / { action / awk-commands }/ search pattern / { action / awk-commands }'
...
'
BEGIN { ... }       # beging block, print only once at first
/<pattern>/ { ... }             # body block, print for each line
END { ... }         # end block , print only once at end
'

### variables
NF => no of fileds/columns in current record/row/line
NR => Record/Row/line number it is processing
FS => field/column seperator
OFS => output field/column seperator
ORS => output record seperator
$0 ==> all fields in string
$1 => first field
ARGV => array of arguments passed to awk (accessed by indexing as ARGV[1])
ENVIRON => get enviremnt variable ( ENVIRON["PS"] )
FILENAME => filename parsing


## grep alternative
awk '/<pattern>/'

## head alternative
### print first 10 line
awk 'NR <= 10'

### don't print first line
awk 'NR>1'

### don't print first 2 line
awk 'NR>'

### print 3rd line
awk 'NR==3'

## cut alternative
### print 3rd field only
awk '{ print $3 }'

### print 3rd line with (filed delimter = ',')
awk '{ print $3 }' FS=","

