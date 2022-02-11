# Function

## Syntax
        <optional_func_scope> function <func_name>(<arg1>, <arg2>) 
            <func_body>
            return <var1>, <var2>
        end

- by default function is global scope

- eg
        function add(num1, num2) do
            return num1 + num2
        end

- function with var args
        function sum(...) do
            local args = {...}
            local result = 0
            for i,arg in iparis(args) do
                result = result + arg
            end
            return result
        end
