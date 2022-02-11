# Conditionals & Loops

## if 
        if (<cond>) then
            <statements>
        end

## if else
        if (<cond>) then
            <statement1>
        else
            <statement2>
        end

## while loop
        while(<cond>) do
            <statements>
        end


## for loop
        for var = start,end,step do
            <statements>
        end

        e.g
        for i = 10,1,-1 do
            print(i)      -- 10, 9, 8 ... 1
        end


### loop table
        for key,value in ipairs(table) do
            print(key .. " : " .. value)
        end


## repeat until
        repeat
            <statements>
        until(<cond>)

