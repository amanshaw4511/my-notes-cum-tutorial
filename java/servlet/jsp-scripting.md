

## Expression
    <%= ... %>

    <%= 2*5 %>
    <%= myVar %>


## Scriptlet
    <% ... %>

    <% out.println("Hello"); %>
    <% 
        if (request.getParameter("x") == null) 
        out.println("no value");
    %>

## Declaration
    <%! ... %>

    <%! public int count = 0; %>
    <%! 
        public int add(int x, int y) {
            return x + y;
        }
    %>

## Directive
    <%@ ... %>
    


## Comment
    <%-- ... --%>



