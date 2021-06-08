// iterator
function range(start = 0, end = Infinity, step = 1) {
    let current = start;
    let itCount = 0;

    return {
        next: function next() {
            if (current < end) {
                let result = { value: current, done: false };
                current += step;
                itCount += 1;
                return result;
            }
            return {value: itCount, done: true}
        }
    }
}


console.log(range(0,10))
const it = range(0,10);
let res = it.next();
while (! res.done) {
    console.log(res.value);
    res = it.next();
}




// generator
function* xrange(start=0, end=Infinity, step=1) {
    let itCount = 0;
    for (let i = start; i < end; i += step) {
        itCount += 1;
        yield i;
    }
    return itCount;
}


console.log(xrange(1,10,2));
const xit = xrange(1,10, 2);
let xres = xit.next();
while (! xres.done) {
    console.log(xres.value);
    xres = xit.next();
}


// we can use for each looping in generator
console.log("\nfor each");
for (let x of xrange(1,10,2)) {
    console.log(x);
}
